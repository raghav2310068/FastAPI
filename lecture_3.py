from fastapi import FastAPI,Path,HTTPException,Query
import json

def load_data():
    with open("patients.json","r") as f:
        data=json.load(f)
    
    return data

app=FastAPI()



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