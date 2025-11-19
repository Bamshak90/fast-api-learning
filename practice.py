from fastapi import FastAPI, Path
from pydantic import BaseModel


app = FastAPI()

students = {
  1: {
    "name": "mark",
    "age": 2
  },
  2: {
    "name": "grace",
    "age": 2
  },
  3: {
    "name": "steve",
    "age": 2
  },
  4: {
    "name": "jason",
    "age": 2
  },
  5: {
    "name": "dorcas",
    "age": 2
  }
}

class Student(BaseModel):
  name: str
  age: int
  year: str
@app.get("/")

def root():
  return {"Welcome": "user"}

# by using path parameter

@app.get("/get-student{student_id}")

def student_record(student_id: int = Path(description="Enter student id to view student record", gt = 0, le = 100 )):
  if student_id in students:
    return students[student_id]
  else:
    return {"Student_id": "Does not exist"}
  

"""
in case you want to use for loop to loop through the dictionary this is another way to go about it


def student_record(student_id: int = Path(description="Enter student id to view student record", gt = 0, le = 20 )):
  for student, value in students.items():
    if student == student_id:
      return student, value
  return {"student_id": "Does not exist"}

"""

#using query parameter


@app.get("/get-by-name")
def get_student(name: str):
  for student_id in students:
    if students[student_id]["name"] == name:
      return students[student_id]
  return {"Data": "Not found"}





@app.post("/create-post{student_id}")

def create_post(student_id: int, student: Student):
  if student_id in students:
    return {"Error": "Data already exist"}
  students[student_id] = student
  return students[student_id]























































































