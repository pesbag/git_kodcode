from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def read_root():
    return {"massage":"Hello word"}
@app.get("/user/{parm}")
def targil2(parm):
    return {"user_id":parm,"massage":"Hello word"}