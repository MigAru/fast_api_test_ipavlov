from fastapi import FastAPI
from tortoise import Tortoise
from fastapi.middleware.cors import CORSMiddleware
from src.database.config import TORTOISE_ORM
from src.database.register import register_tortoise


Tortoise.init_models(["src.database.models"], "models")


from src.routers import items


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=True)
