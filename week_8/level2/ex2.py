from fastapi import FastAPI
from datetime import datetime

app=FastAPI()
@app.get("/")
def service_version():
    return {"service": "my-api", "version": "1.0"}

@app.get("/users/admin")
def reach_correctly():
    return {"role": "admin", "access": "full"}

@app.get("/users/{user_id}")
def hard_coded_dict(user_id: int):
    return {"user_id":user_id,"name":"name","email":"email"}

@app.get("/calc/{a}/{op}/{b}")
def clac(a:int,op,b:int):
    if op =="add":
        return {"operation": op, "result":a+b}
    elif op =="sub":
        return {"operation": op, "result":a-b}
    elif op =="div":
        try:
            return {"operation": op, "result":a/b}
        except ZeroDivisionError:
            return "Error cannot divide by zero"
    elif op =="mul":
        return {"operation": op, "result":a*b}
    else:
        return f"Error: command {op} was not found"

@app.get("/status")
def get_status():
    return {"time":datetime.now(),"status":"ex2"}