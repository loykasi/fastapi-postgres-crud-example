# CRUD API with FastAPI + PostgreSQL

A simple API built with [FastAPI](https://fastapi.tiangolo.com/) and [PostgreSQL](https://www.postgresql.org/), containerized using Docker.

## Run the App

1. **Create .env** 
```
DB_USER=
DB_PASSWORD=
DB_NAME=
```

2. **Start the services**
```bash
docker-compose up --build
```

3. **Visit the API**:

    - Swagger UI: `http://localhost:8000/docs`