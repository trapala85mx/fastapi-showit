"""Módulo principal"""

from typing import List

import uvicorn
from fastapi import FastAPI
from sqlmodel import select

from database.db_config import SessionDependency, create_all_tables
from models.customer import Customer, CustomerCreate

app = FastAPI(lifespan=create_all_tables)


@app.get("/customers", response_model=List[Customer])
async def get_clients(session: SessionDependency):
    """Obtiene todo los clientes de la base de datos.

    Args:
        session (SessionDependency): Sesión de conexión a la BD.

    Returns:
        List[Customer]: Lista de Clientes
    """
    customers = session.exec(select(Customer)).all()
    return customers


@app.post("/customers", response_model=Customer)
async def add_client(customer_data: CustomerCreate, session: SessionDependency):
    """Agrega un nuevo cliente.

    Args:
        customer_data (CustomerCreate): Modelo de datos basados en un cliente sin el id.
        session (SessionDependency): sesión para interactuar con la BD.

    Returns:
        Customer: Modelo de dato de un Customer que ya contiene el id.
    """
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)
