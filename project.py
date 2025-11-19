from fastapi import FastAPI, Path
from pydantic import BaseModel


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

@app.get("/")
def root():
  return {"Welcome": "student"}


@app.get("/get-by-id{student_id}")

def get_student(student_id: int = Path(description="Enter the student id you wish to view records") ):
  if student_id in students:
    return students[student_id]


@app.post("/create-post{student_id}")

def create_post(student_id: int, student: Student):
  if student_id in students:
    return {"Error": "ID exist"}
  students[student_id] = student
  return students[student_id]