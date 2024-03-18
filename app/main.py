from fastapi import FastAPI

import os
from dotenv import load_dotenv

from . import models
from .database import engine
from .routers import post, user, auth

load_dotenv()

POSTGRES_PWD = os.getenv('POSTGRES_PWD')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}