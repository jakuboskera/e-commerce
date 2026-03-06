import os

from fastapi import FastAPI

APP_NAME = os.getenv("APP_NAME", "order-api")

app = FastAPI(title=APP_NAME)


@app.get("/")
def root():
    return {"app": APP_NAME, "status": "ok"}


@app.get("/healthz")
def health():
    return {"status": "healthy"}
