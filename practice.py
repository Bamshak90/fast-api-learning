from fastapi import FastAPI, Path


app = FastAPI()

students = {
  1: {
    "name": "mark",
    "age": 2
  }
}
@app.get("/")

def home():
  return {"Welcome": "user"}


@app.get("/get-student{student_id}{student_name}")

def student_record(student_id: int = Path(description="Enter student id to view student record", gt = 0, le = 10 )):
  if student_id in students:
    return students[student_id]
  

def student_greet(student_name: str = Path(description="using student name to greet")):
  if student_name in students:
    return students[student_id]["name"]





























































































# from fastapi import FastAPI, Path


# app =  FastAPI()


# students = {
#     1: {
#         "name": "Mark",
#         "age": 20,
#         "year": "Final year",
#         "gender": "Male"
#     }
# }


# @app.get("/get-student/{student_id}")
# def get_students(student_id: int = Path(description = "The id of the student you want to view")):
#    if students["id"] == student_id:
#     return students[student_id]
#    return {"Welcome": "But student id does not exist in the database"}