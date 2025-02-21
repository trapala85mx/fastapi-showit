"""Mñodulo para confgigurar la BD"""

from typing import Annotated

from fastapi import Depends, FastAPI
from sqlmodel import Session, SQLModel, create_engine

sqlite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine(sqlite_url)


def create_all_tables(app: FastAPI):
    """Generador para creación de base de datos y tablas

    Args:
        app (FastAPI): Instancia de FastAPI para que pueda usarla.

    Yields:
        None
    """
    SQLModel.metadata.create_all(engine)
    yield


def get_session():
    """Generador para que FastAPI obtenga sesiones

    Yields:
        Session: sesión de la base de datos.
    """
    with Session(engine) as session:
        yield session


SessionDependency = Annotated[Session, Depends(get_session)]
