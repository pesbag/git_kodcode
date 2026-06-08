from fastapi import FastAPI
app=FastAPI()

@app.get("/greet")
def print_hello(name = "world"):
    return {"message": f"Hello, {name}!"}