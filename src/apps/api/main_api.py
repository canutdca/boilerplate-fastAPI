from fastapi import FastAPI
from apps.api.routers.users_router import router as users_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI!"}


app.include_router(users_router)
