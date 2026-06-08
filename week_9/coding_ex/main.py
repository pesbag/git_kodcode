from fastapi import FastAPI
from pydantic import BaseModel

import db_massages
import uvicorn

class Message(BaseModel):
    unit: str
    classification:str
    content:str
    source:str

app=FastAPI()
@app.get("/schema")
def get_schema():
    return db_massages.get_schema()
@app.get("/messages")
def get_messages():
    return db_massages.get_all_messages()
@app.post("/setup")
def post_set_up():
    return {"status":"ok"}


@app.post("/messages")
def add_massage_to_table(data:Message):
    data = data.model_dump()
    new_id = db_massages.add_massage(data)
    return {"new_id":new_id,"messages":"created successfully"}

@app.get("/messages/{message_id}")
def return_message(message_id):
    return db_massages.get_specific_message(message_id)

@app.put("/messages/{message_id}")
def update_message(message_id):
    return db_massages.update_specific_message(message_id)

@app.delete("/messages/{message_id}")
def delete_message(message_id):
        return db_massages.delete_specific_massage(message_id)

if __name__=="__main__":
    uvicorn.run("main:app",host="localhost",port=8001,reload=True)
