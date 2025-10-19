from fastapi import FastAPI,Query,Path,HTTPException
from pydantic import BaseModel,Field,computed_field
from fastapi.responses import JSONResponse
import json
from typing import Annotated,Literal
class Patient(BaseModel):
    id:Annotated[str,Field(...,description="ID of the patient",examples=["P001","P002"])]
    name:Annotated[str,Field(...,description="Name of the patient",examples=["krish","keshav"])]
    city:Annotated[str,Field(...,description="native place of the patient",examples=["ghaziabad","bulandshahr"])]
    age:Annotated[int,Field(...,gt=0,lt=120,description="age of the person")]
    gender:Annotated[Literal["male","female","others"],Field(...,description="gender of the patient")]
    height:Annotated[float,Field(...,gt=0,description="height of the patient in meters")]
    weight:Annotated[float,Field(...,gt=0,description="weight of the patient in kilograms")]
    
    @computed_field
    @property
    def bmi(self)-> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)-> str:
        if self.bmi<18:
            return "underweight"
        elif self.bmi<30:
            return "normal"
        else:
            return "Obese"


app=FastAPI()

def load_data():
    with open("patients.json","r") as f:
        data=json.load(f)
    
    return data 

def save_data(data):
    with open("patients.json","w") as f:
        json.dump(data,f)
    

@app.get("/")
def home():
    return {"message":"this is the welcome home page"}

@app.get("/about")
def info():
    return {"message":"this page give the information about the website"}

@app.get("/view")
def view():
    data=load_data()
    return data        

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str=Path(...,description="id of the patient in database",example="P001")):
    data=load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="patient id not found in the database")

@app.get("/sort")
def sort(sort_by:str=Query(...,description="sort on the basis of height,weight and BMI"),order: str=Query("asc",description="sort in ascending and descending order")):
    valid_field=["height","weight","bmi"]
    if sort_by not in valid_field:
        raise HTTPException(status_code=400,detail=f"invalid field selectd from {valid_field}")
    
    if order not in ["asc","desc"]:
        raise HTTPException(status_code=400,detail="invalid order selected from asc and desc")
    
    data=load_data()
    sort_order=True if order=="desc" else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data

@app.post("/create")
def  create_patient(patient: Patient):
    # load existing data
    data=load_data()
    # check if patient already exists or not 
    if patient.id in data:
        HTTPException(status_code=400,detail="patient already exists")
    # new patient add to database
    patient_dict=patient.model_dump(exclude=["id"])
    data[patient.id]=patient_dict
    # save data
    save_data(data)

    return JSONResponse(status_code=201,content={"message":"patient created successfully"})