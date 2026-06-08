from fastapi import APIRouter
import requests
from fastapi import FastAPI,HTTPException
app=FastAPI()
@app.get("/numbers/{n}")
def is_negative(n:int):
    result=check_negative(n)
    if result:
        raise HTTPException(status_code=400,detail='Number must be non-negative')
    return {"value": n}

def check_negative(n):
    if n<0:
        return True
    return False

response=requests.get("http://127.0.0.1:8000/students/101")
print(response.text)