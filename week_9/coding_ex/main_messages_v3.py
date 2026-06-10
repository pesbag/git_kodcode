from idlelib.query import Query

from intel_messages import IntelMessagesDAL
from fastapi import FastAPI,HTTPException,Query
from pydantic import BaseModel
import logging
import uvicorn

logging.basicConfig(filename="sql_server.log",level=logging.INFO)
logger=logging.getLogger(__name__)

app=FastAPI()

manager=IntelMessagesDAL("localhost",3306,"root","secret","soldiers_db",logger)

class Message(BaseModel):
    unit: str
    classification:str
    content:str
    source:str

app=FastAPI()

@app.get("/schema")
def get_schema_messages():
    return manager.get_schema()

@app.get("/messages")
def get_messages(
                unit:str|None=Query(default=None),
                classification:str|None=Query(default=None)
            ):
    if not unit and not classification:
        return {"soldiers":manager.get_all()}
    elif unit and not classification:
        return {"unit":manager.get_by_unit()}
    elif not unit and classification:
        return {"classification":manager.get_by_classification()}
    else:
        return {"unit and classification":manager.get_by_unit_and_classification()}

@app.post("/messages")
def add_massage_to_table(unit: str, classification: str, content: str, source: str| None):
    new_id = manager.create(unit, classification, content, source)
    return {"new_id":new_id,"messages":"created successfully"}

@app.get("/messages/search")
def search_content(term: str):
    if not str:
        raise HTTPException(status_code=400,detail="content to found was not found")
    result= manager.get_by_id(term)
    if not result:
        raise HTTPException(status_code=400,detail="content to found was not found")
    return result

@app.put("/messages/{message_id}")
def update_message(message_id:int,data:dict):
    result= manager.update(message_id,data)
    if not result:
        raise HTTPException(status_code=404,detail="message id was not found, nothing updated")
    return result

@app.delete("/messages/{message_id}")
def delete_message(message_id):
    result=manager.delete(message_id)
    if not result:
        raise HTTPException(status_code=404,detail="message id was not found, nothing deleted")
    return result

@app.get("/messages/units")
def all_unit_messages(unit_name:str):
    """
    get all the unit messages
    :param unit_name: unit to find his message
    :return: messages or error
    """
    result=manager.get_by_unit(unit_name)
    if not result:
        raise HTTPException(status_code=400,detail="unit was not found, nothing returned")
    return result

@app.get("/messages/classification/{level}")
def return_message_classify(level:str):
    result= manager.get_by_classification(level)
    return result

@app.get("/messages/{message_id}")
def return_messages(message_id:int):
    result = manager.get_by_id(message_id)
    if not result:
        raise HTTPException(status_code=404, detail="message id was not found, nothing updated")
    return result

@app.get("/messages/missing-source")
def return_missing_source():
    result=manager.get_missing_source()
    return {"missing-source": result}


if __name__=="__main__":
    uvicorn.run("main_messages_v3:app",host="localhost",port=8000,reload=True)
