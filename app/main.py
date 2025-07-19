from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    attendance: str  # "Present" or "Absent"

# In-memory storage
employees: List[Employee] = []

@app.post("/add")
def add_employee(emp: Employee):
    employees.append(emp)
    return {"message": "Employee added successfully"}

@app.get("/list")
def list_employees():
    return employees