from typing import Optional, Any, Dict
from sqlmodel import Field, SQLModel

class anime(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    at_id: Any = Field(default=None, unique=True) #  anime_themes_id        
    mal_id: Any = Field(default=None, unique=True)
    title: str = Field(default="", nullable=False)
    slug: str = Field(default="", unique=True, nullable=False)
    description: str = Field(default="")
    media: str = Field(default="")
    year: Optional[int] = Field(default="")


class songs(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    at_id: Any = Field(unique=True) #  anime_themes_id    
    slug: str = Field(nullable=False)
    anime_title: str = Field(nullable=False)
    anime_id: str = Field(nullable=False)
    anime_slug: str = Field(nullable=False)
    song_type: str = Field()
    episodes: str = Field()
    filename: str = Field(nullable=False)
    basename: str = Field(nullable=False)
    path: str = Field(nullable=False)
    link: str = Field(nullable=False)
    filename_backup: Optional[str] = Field(default=None, nullable=True)
    basename_backup: Optional[str] = Field(default=None, nullable=True)
    path_backup: Optional[str] = Field(default=None, nullable=True)
    link_backup: Optional[str] = Field(default=None, nullable=True)

