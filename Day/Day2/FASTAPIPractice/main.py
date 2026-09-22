from fastapi import FastAPI
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