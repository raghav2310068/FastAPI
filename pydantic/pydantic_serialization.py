from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pincode:str

class Patient(BaseModel):
    name:str
    age:int
    gender:str
    address:Address

address_dict={"city":"ghaziabad","state":"Uttar Pradesh","pincode":"203001"}

address1=Address(**address_dict)

patient_info={"name":"raghav","age":32,"gender":"M","address":address1}

patient1=Patient(**patient_info)

temp=patient1.model_dump_json()
print(temp)
print(type(temp))