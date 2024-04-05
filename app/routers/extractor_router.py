from fastapi import APIRouter
from typing import Any, Dict, List, Optional

from sqlmodel import SQLModel
from ..services import get_top_animes, get_animes
from ..databases import Sql, anime, songs
from pprint import pprint

router = APIRouter(prefix="/extract")
anime_table: Sql = Sql(model=anime)
songs_table: Sql = Sql(model=songs)

@router.get("/start")
async def start() -> Dict[str, Any]:
     animes: List[Dict[str, Any]] = await get_top_animes()
     processed_animes: List[Dict[str, str]] = [] 

     for anime in animes:
          data: Optional[Dict[str, Any]] = await process_anime(anime)

          if not data: continue
          
          processed_animes.append(data)
          break
     return {"animes": processed_animes }


async def process_anime(anime: Dict[str, Any]) -> Optional[Dict[str, Any]]:
     mal_id: Optional[str] = anime.get("mal_id")
     title: Optional[str] = anime.get("title")
     data = {
          "mal_id": mal_id,
          "title": title,
          "media": anime.get("type"),
          "status": anime.get("status"),
          "description": anime.get("synopsis"),
          "episodes": anime.get("episodes"),
          "score": anime.get("score"),
          "year": anime.get("year"),
          "image": anime.get("images", {}).get("jpg", {}).get("image_url")
     }

     anime_themes = await get_animes(filter_data={
          "filter[has]": "resources", 
          "filter[site]": "MyAnimeList", 
          "filter[external_id]": mal_id, 
     })

     if len(anime_themes): return 

     anime_theme: Dict[str, Any] = anime_themes[0]
     data["at_id"] = anime_theme["id"] 
     data["slug"] = anime_theme["slug"] 

     anime_instance: SQLModel = anime_table.sql_set(data)
     songs: List[Dict[str, Any]] = []

     anime_id = anime_instance.id

     for theme in anime_theme["animethemes"]:
          theme_data: Dict[str, Any] = {
               "at_id": theme["id"],
               "slug": theme["slug"],
               "song_type": theme["type"],
               "anime_id": anime_id,
          } 
          entry: Dict[str, Any] = theme["animethemeentries"][0]
          theme_data["episodes"] = entry["episodes"]
          videos: List[Dict[str, Any]] =  entry["videos"]
          videos_amount: int = len(videos)
          video: Dict[str, Any] = videos[0]
          backup_video: Dict[str, Any] = {} if videos_amount < 2 else videos[1]
          theme_data["filename"] = video["filename"]
          theme_data["basename"] = video["basename"]
          theme_data["path"] = video["path"]
          theme_data["link"] = video["link"]
          theme_data["filename_backup"] = backup_video.get("filename")
          theme_data["basename_backup"] = backup_video.get("basename")
          theme_data["path_backup"] = backup_video.get("path")
          theme_data["link_backup"] = backup_video.get("link")

          songs.append(theme_data)

     data["songs"] = songs

     return data
