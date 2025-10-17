from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI(title="simple fastApi App", version ="1.0.0")
data=[{"name": "sam larry", "age":20, "track": "Ai Developer"},
{"name": "Bahuballi", "age":21, "track": "Backend Developer"},
{"name": "John Doe", "age":22, "track": "frontend Developer"}]



class Item(BaseModel):
    name: str = Field(..., example="perpetual")
    age: int = Field(..., example= 25)
    name: str = Field(..., example="fullstack developer")
@app.get("/", description="this endpoint just returns a welcome message")
def root():
    return{"message": "Welcome to my fastapi Application"}
@app.get("/get-data")
def get_data():
    return data

@app.post("/create-data")
def create_data(req:Item):
    data.append(req.dict())
    print(data)
    return{"message": "Data Received", "Data": data}


@app.put("/update-date/{id}")
def update_data(id: int,req:Item):
    data[id] = req.dict()
    print(data)
    return{"message": "data updated", 'data': data}

#write an endpost to patch  and delete article from the server


if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))
