from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


students = {
  1: {
    "name": "Mark",
    "age": 12,
    "year": "final"
  }
}

class Student(BaseModel):
  name: str
  age: int
  year: str

class Update(BaseModel):
  name: Optional[str] = None
  age: Optional[int] = None
  year: Optional[str] = None


@app.get("/")
def root():
  return {"Welcome": "student"}


@app.get("/get-by-id{student_id}")

def get_student(student_id: int = Path(description="Enter the student id you wish to view records") ):
  if student_id in students:
    return students[student_id]
  
  return {"Error": "Student data does not exist"}


@app.post("/create-post{student_id}")

def create_post(student_id: int, student: Student):
  if student_id in students:
    return {"Error": "ID exist"}
  students[student_id] = student
  return students[student_id]


@app.put("/update{student_id}")

def update_post(student_id: int, student: Update):
  if student_id in students:
    if student.name != None:
      students[student_id].name = student.name

    if student.age != None:
      students[student_id].age = student.age

    if student.year != None:
      students[student_id].year = student.year
    return students[student_id]
  
  return {"Error": "student ID does not exist"}


@app.delete("/delete{student_id}")
def delete_student(student_id: int):
  if student_id in students:
    del students[student_id]
    return {"ID": "succefully deleted"}
  return {"ID": "Does not exist"}