from fastapi import FastAPI

app = FastAPI(
  title="Vremya Bank API",
  description="Vremya Bank application built with FastAPI"
)

@app.get("/")
def home():
    return {"message": "Welcome to the Vremya Bank API"}