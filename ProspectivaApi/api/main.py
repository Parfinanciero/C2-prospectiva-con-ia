from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def health_chech():
    return "Camilo es gay"