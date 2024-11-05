# /backend/app.py
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database.database import SessionLocal, Base, engine
from fastapi.templating import Jinja2Templates

# Database model definition
class StudentModel(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    roll_number = Column(Integer)

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI app initialization
app = FastAPI()

# For rendering templates
templates = Jinja2Templates(directory="../frontend")

# Pydantic model for request body
class Student(BaseModel):
    name: str
    roll_number: int

# Endpoint to submit student data
@app.post("/submit/")
async def submit_student(student: Student):
    db = SessionLocal()
    db_student = StudentModel(name=student.name, roll_number=student.roll_number)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    db.close()
    return {"message": "Student information received", "name": student.name, "roll_number": student.roll_number}

# Endpoint to render the HTML form and display the data
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    db = SessionLocal()
    students = db.query(StudentModel).all()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request, "students": students})
