from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Homepage"])
def main():
    """Homepage"""
    return {"Hello from": "server"}
