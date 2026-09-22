from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message":"Hello world","number":44,"is_fun":True}