from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Starter",
    description="A minimal FastAPI application.",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
