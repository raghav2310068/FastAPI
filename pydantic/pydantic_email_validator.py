from pydantic import EmailStr,BaseModel,validate_email,Field,field_validator,model_validator
from typing import Dict,List,Annotated,Optional

# class Patient(BaseModel):
#     name:str
#     age:int
#     email:EmailStr
#     weight:float
#     married:Optional[bool]=False
#     allergies:Optional[List[str]]=None
    
#     @field_validator("email")
#     @classmethod
#     def email_validator(cls,value):
#         valid_domains=["hdfc.com","icici.com"]
#         domain_name=value.split("@")[-1]
#         if domain_name not in valid_domains:
#             raise ValueError("not a valid domain")
        
#         return value
    
#     @field_validator("name")
#     @classmethod
#     def transform_name(cls,value):
#         return value.upper()
    

# patient_info={
# "name":"raghav",
# "age":25,
# "email":"raghav@hdfc.com",
# "weight":39.5,
# }

# patient1=Patient(**patient_info)
# def insert_patient(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print(patient.married)
#     print(patient.allergies)
#     print("inserted")

# insert_patient(patient1)



class SocietyForm(BaseModel):
    name: str
    student_number: str
    email: EmailStr
    branch: str

    # Field-level validator
    @field_validator("student_number")
    @classmethod
    def validate_student_number(cls, value):
        if value.startswith("24"):
            return value
        raise ValueError("Not a valid student number")

    # Model-level validator
    @model_validator(mode="after")
    def validate_email(model):
        expected_email = model.name.split()[0] + model.student_number + "@akgec.ac.in"
        if model.email != expected_email:
            raise ValueError("Please enter a valid email")
        return model  # Must return model

# Test
student_info = {
    "name": "raghav mittal",
    "student_number": "2410068",
    "email": "raghav24100068@akgec.ac.in",
    "branch": "SS"
}

s1 = SocietyForm(**student_info)
print(s1)