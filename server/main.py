from fastapi import FastAPI, Depends
from server.database.client import get_client

app = FastAPI()

@app.get("/", tags=["Homepage"])
def main():
    """Homepage"""
    return {"Hello from": "server"}


@app.get("/collections")
def get_collections(client=Depends(get_client)):
    collections = client.list_collections()
    print("Collections:", collections)
    collection_names = [getattr(c, "name", str(c)) for c in collections]

    return {"collections": collection_names}
