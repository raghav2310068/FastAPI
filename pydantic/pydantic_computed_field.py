from pydantic import BaseModel,EmailStr,computed_field
from typing import Dict,List,Optional

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact_details:Optional[Dict[str,str]]=None
    
    @computed_field
    @property
    def bmi(self)-> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi 
    
    
patient_info={
    "name":"raghav",
    "email":"raghav@gmail.com",
    "age":25,
    "weight":60.2,
    "height":1.69,
    "married":0,
    "allergies":["pollen"],
}

patient1=Patient(**patient_info)
def update_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.height)
    print(patient.weight)
    print(patient.bmi)

update_patient(patient1)