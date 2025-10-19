from pydantic import BaseModel,Field,AnyUrl,EmailStr
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=25,description="give th name of the person in less then 25 chars",examples=["raghav","rajeev"])]
    age:int=Field(gt=1,le=100)
    email:EmailStr
    weight:float
    married:bool=False
    allergies:Optional[List[str]]=None
    contact_info:Dict[str,str]
    
patient_info={
    "name":"raghav",
    "age":45,
    "weight":59.5,
    # 'married':0,
    # "allergies":["pollen","dust"],
    "contact_info":{
        "email":"abc@gmail.com",
        "mobile_number":"9456675400"
    }
}
patient_1=Patient(**patient_info)

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print("inserted")

insert_patient(patient_1)