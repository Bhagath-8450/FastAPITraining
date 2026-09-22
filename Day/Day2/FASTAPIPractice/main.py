from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
@app.get("/")
def home():
    return {"page":"Home"}

@app.get("/about")
def about():
    return {"page":"About","author":"Bhagath"}

@app.get("/health")
def health():
    return {"status":"ok"}

#post request
@app.post("/create")
def create_something():
    return {"message":"Created"}
@app.get("/students/{usn}")
def get_result(usn):
    return {"Result":"Distinction","usn":usn}

#type hint
@app.get("/candidate/{rollno}")
def get_result(rollno:int): 
    return {"Result":"Distinction","rollno":rollno,"type":str(type(rollno))}  

#pydantic model
class Item(BaseModel):
    name:str
    price:float
    in_stock : bool = True


@app.post("/items")
def create_item(item:Item):
    return {"recieved":item,"total_price":item.price*1.18}