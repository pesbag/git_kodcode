from fastapi import FastAPI
import uvicorn
import db
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
    return {"soldiers":[]}

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)