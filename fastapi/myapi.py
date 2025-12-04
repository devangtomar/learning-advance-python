from fastapi import FastAPI, Path, HTTPException
import uvicorn
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {1: {"name": "john", "age": 17, "class": "year 12"}}


class Student(BaseModel):
    name: str
    age: str
    year: str


@app.get("/")
def index():
    return {"name": "First data"}


@app.get("/get-student/{student_id}")
def get_student(
    student_id: int = Path(
        ...,
        description="The ID of the student you want to view!",
        gt=0,
        lt=3,
    )
):
    if student_id in students:
        return students[student_id]
    else:
        raise HTTPException(status_code=404, detail="Student not found")


@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found!"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists!"}

    students[student_id] = student
    return students[student_id]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
