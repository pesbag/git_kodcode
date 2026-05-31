import uvicorn
from fastapi import FastAPI
app = FastAPI()

# @app.get("/")
@app.get("/ping")
def print_pong():
    return {"status":"pong"}

@app.get("/greet/{name}")
def hello_name(name):
    return {"message": f"Hello, {name}!"}
if __name__ == "__main__":
    uvicorn.run("level1:app", host="127.0.0.1", port=8000, reload=True)