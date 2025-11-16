from fastapi import FastAPI, Path


app = FastAPI()

students = {
  1: {
    "name": "Mark",
    "age": "25",
    "class": "final year"
  }
}

@app.get("/")
def index():
  return {"message": "Welcome to Task Manager API!"} 


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description= "The ID of the student you want to view")):
  for student in students:
    if student["id"] == student_id:
      return student
  raise HTTPException(status_code=404, detail="Student not found")














































# @app.post("/")
# def message_update():
#   return {"animal": "blue-wahale"}


# @app.put("/")
# def updated():
#   return {"mad": "This is crazy and fuck"}


# @app.delete("/")
# def remove_info():
#   return {"name": "I have just seen something wonderful"}