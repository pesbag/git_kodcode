from fastapi import FastAPI
import db_massages
import uvicorn
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
if __name__=="__name__":
    uvicorn.run(app,host="localhost",port=8001)
