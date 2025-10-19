from fastapi import FastAPI
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