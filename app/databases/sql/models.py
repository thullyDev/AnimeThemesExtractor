from typing import Optional, Any, Dict,Type, Union
from sqlmodel import Field, SQLModel

class anime(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    at_id: Optional[int] = Field(default=None, unique=True) #  anime_themes_id        
    mal_id: Optional[int] = Field(default=None, unique=True)
    title: str = Field(default="", nullable=False)
    image: str = Field(default="", nullable=False)
    slug: str = Field(default="", unique=True, nullable=False)
    description: str = Field(default="")
    media: str = Field(default="")
    year: Optional[int] = Field(default="")
    status: str = Field(default="")
    episodes: Optional[int] = Field()
    score: Optional[int] = Field(default="")

class songs(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    at_id: Optional[int] = Field(unique=True) #  anime_themes_id    
    slug: str = Field(nullable=False)
    episodes: Optional[str] = Field()
    anime_image: str = Field(default="", nullable=False)
    anime_id: str = Field(nullable=False)
    song_type: str = Field()
    filename: str = Field(nullable=False)
    basename: str = Field(nullable=False)
    path: str = Field(nullable=False)
    link: str = Field(nullable=False)
    filename_backup: Optional[str] = Field(default=None, nullable=True)
    basename_backup: Optional[str] = Field(default=None, nullable=True)
    path_backup: Optional[str] = Field(default=None, nullable=True)
    link_backup: Optional[str] = Field(default=None, nullable=True)

def get_models() -> Dict[ str, Union[ Type[anime], Type[songs] ]]:
    return {
        "anime": anime,
        "songs": songs,
    }

def get_model(unit: str) -> Union[ Type["anime"], Type["songs"] ]: 
    models = get_models()
    model = models.get(unit)

    if model:
        return model
    
    raise Exception(f"No model name: {unit}") 


