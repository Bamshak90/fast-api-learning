from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel



app = FastAPI()

students = {}

class Student(BaseModel):
  name: str
  age: int
  year: str
  department: str
  cgpa: float

class Update(BaseModel):
  name: Optional[str] = None
  age: Optional[int] = None
  year: Optional[str] = None
  department: Optional[str] = None
  cgpa: Optional[float] = None


@app.get("/get-student{student_id}")

def get_student(student_id: int = Path(description="This is to get the student record using the student id")):
  if student_id in students:
    return students[student_id]
  return {"message": "Error, student id does not exist"}


@app.post("/create-student/{student_id}")

def create_student(student_id: int, student: Student):
  if student_id in students:
    return {"message": "student id already exist"}
  students[student_id] = student
  return students[student_id]

@app.put("/update-student/{student_id}")

def update_student(student_id: int, student: Update):
  if student_id  in students:

    if student.name != None:
      students[student_id].name = student.name

    if student.age != None:
      students[student_id].age = student.age

    if student.year != None:
      students[student_id].year = student.year

    if student.department != None:
      students[student_id].department = student.department

    if student.cgpa != None:
      students[student_id].cgpa = student.cgpa
    return students[student_id]
  
  return {"message": "id does not exist"}


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
  if student_id in students:
    del students[student_id]
    return {"message": "record deleted"}
  return {"message": "id does not exist"}
    