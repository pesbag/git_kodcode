from fastapi import FastAPI,HTTPException
from fastapi import Body
import uvicorn
import db
from pydantic import BaseModel

class Soldier(BaseModel):
    name:str
    soldier_rank:str
    unit:str
    active:bool

app = FastAPI()
@app.post("/setup")
def run_setup():
    return {"status":"setup triggered"}
@app.get("/schema")
def get_schema():
    columns=db.get_schema()
    return {"columns":columns}

@app.get("/soldiers")
def get_all_soldiers():
    result=db.get_all()
    return {"soldiers":result}

@app.delete("/soldier/{soldier_id}")
def remove_soldier(soldier_id:int):
    result= db.delete(soldier_id)
    if not result:
        raise HTTPException(status_code=404,detail="Soldier id was not found")
    else:
        return result

@app.put("/update/{soldier_id}")
def update_soldier(soldier_id:int,data:dict):
    result=db.update(soldier_id,data)
    if not result:
        raise HTTPException(status_code=404, detail="soldier id was not found")
    else:
        return result

@app.post("/create")
def create_soldier(data:Soldier):
    data=data.model_dump()
    new_id=db.create(**data)
    return {"id":new_id,"message": "Soldier creates successfully"}
@app.get("/get-names-and-ranks")
def return_names_and_ranks():
    result=db.get_names_and_ranks()
    return result

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)