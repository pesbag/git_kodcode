from fastapi import FastAPI, HTTPException

app=FastAPI()
data_dict={"101": "Moshe", "102": "Yosef"}
@app.get("/students/{id}")
def get_student(id:str):
    result=get_student_name(id,data_dict)
    if not result:
        raise HTTPException(status_code=404,detail="error student was not found")
    return {"name":data_dict[id]}
def get_student_name(id,data_dict):
    if id not in data_dict:
        return False
    return True

@app.post("/students/{id}")
def post_student(id:int):
    result=insert_student(id)


def insert_stusent