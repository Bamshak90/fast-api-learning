from fastapi import FastAPI, Path


app = FastAPI()

students = {
  1: { 
    "name": "Mark",
    "age": 25,
    "class": "final year"
  },
  2: {
     "name":"Nanmen",
     "age": 20,
     "class": "300 level"
  }
}

@app.get("/")
def index():
  return {"message": "Welcome to Task Manager API!"} 


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description= "The ID of the student you want to view",gt = 0, le = 10)):

    return students[student_id]
     
    return {"The student data does not exist"}
  # raise HTTPException(status_code=404, detail="Student not found")




# @app.get("/get")



 










































# @app.post("/")
# def message_update():
#   return {"animal": "blue-wahale"}


# @app.put("/")
# def updated():
#   return {"mad": "This is crazy and fuck"}


# @app.delete("/")
# def remove_info():
#   return {"name": "I have just seen something wonderful"}