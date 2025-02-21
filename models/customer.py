"""Módulo para el modelo de datos de cliente"""

from typing import Optional

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class CustomerBase(SQLModel):
    """Modelo base de un cliente"""

    name: str = Field(default=None)
    age: int = Field(default=None)
    email: EmailStr = Field(default=None)
    description: Optional[str] = Field(default=None)


class CustomerCreate(CustomerBase):
    """Modelo de cliente para usar en la creación de clientes"""


class Customer(CustomerBase, table=True):
    """Modelo de cliente para usar en datos recibidos desde la BD"""

    id: Optional[int] = Field(default=None, primary_key=True)
