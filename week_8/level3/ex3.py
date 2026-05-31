from fastapi import FastAPI

grades = {
"1": {"name": "Moshe", "grade": 88},
"2": {"name": "Yaakov", "grade": 75},
"3": {"name": "David", "grade": 92},
}

app=FastAPI()
@app.get("/students")
def return_all_students():
    student_lst=[]
    for student_id, student_info in grades.items():
        student_lst.append(student_info["name"])
    return student_lst

@app.get("/students/top")
def highest_grade():
    return {"max grade":max(grades.values(),key=lambda high:high["grade"])}

@app.get("/students/average")
def find_avg():
    total=0
    for k,v in grades.items():
        total+=v["grade"]
    return {"average":total/len(grades)}

@app.get("/students/count")
def count_students():
    return {"num of student":len(grades)}

@app.get("/students/{student_id}")
def find_student(student_id:str):
    return grades[student_id]

