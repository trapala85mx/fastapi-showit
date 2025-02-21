# **Nivel 1: Fundamentos**

## **Crear un endpoint para listar clientes**

- Endpoint: `GET /customers`
- Retorna una lista de clientes almacenados en la base de datos.

1. debo crear una función , será `get_customers`
2. estará decorada por `app.get('/customers')`
3. implica crear un modelo para clientes, como viene de la base de datos, debe traer el id: `Customer(BaseModel)`.
4. Dentro de la función:
    1. acceder a la sesión de la BD
    2. hacer la petición de todos los clientes
    3. iterar la respuesta de la BD y crear un `Customer` para cada cliente y agregarlo a una lista
    4. retornar la lista de clientes
5. la función, por lo tanto, retorna un modelo `Customer` por lo que en el decorador irá `response_model=list[Customer]`

## **Crear un endpoint para agregar clientes**

- Endpoint: `POST /customers`
- Recibe un JSON con los datos del cliente y los almacena en la base de datos.

1. crear una función, será `add_customer`
2. decorada con `app.post('/customers')`
3. Ya tenemos un modelo `Customer` que tiene un atributo `id` pero este atributo no lo podemos agregar cuando estamos creando uno nuevo. Esto es responsabilidad de la BD. Por lo tanto, debemos crear un nuevo modelo `CustomerCreate` que no recibirá el `id` y, será entonces, este modelo el que recibe. Por lo que la función sería: `add_customer(customer_data: CustomerCreate)`
4. Dentro de la función:
    1. recibimos los datos y validamos el modelo
    2. insertamos en la BD la info
    3. retornamos el cliente creado en la BD que ya incluye el id
5. la función, por lo tanto, retorna un `Customer` por lo que el decorador queda con `response_model=Customer`

## **Validar los datos de entrada con Pydantic**

- Asegúrate de que los datos del cliente (nombre, email, etc.) sean válidos antes de almacenarlos.

Esto implica usar el `model_validate()`

# Nivel 2.