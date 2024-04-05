from typing import Any
from sqlmodel import SQLModel, create_engine
from decouple import config

SQL_URL: Any = config("SQL_URL")

connect_args = {"check_same_thread": False}
engine = create_engine(SQL_URL, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()