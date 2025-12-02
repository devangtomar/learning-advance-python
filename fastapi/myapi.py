from fastapi import FastAPI, Path, HTTPException
import uvicorn

app = FastAPI()

students = {1: {"name": "john", "age": 17, "class": "year 12"}}


@app.get("/")
def index():
    return {"name": "First data"}


@app.get("/get-student/{student_id}")
def get_student(
    student_id: int = Path(..., description="The ID of the student you want to view!")
):
    if student_id in students:
        return students[student_id]
    else:
        raise HTTPException(status_code=404, detail="Student not found")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
