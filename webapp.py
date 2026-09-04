from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"id": item_id, "name": f"item-{item_id}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
