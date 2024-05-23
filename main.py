from fastapi import FastAPI
from typing import List, Optional

app = FastAPI()

db = [
    {"id":1, "size" : "s", "fuel":"petrol", "doors":4},
    {"id":2, "size" : "m", "fuel":"Deisel", "doors":3},
    {"id":3, "size" : "l", "fuel":"petrol", "doors":2},
    {"id":4, "size" : "s", "fuel":"electrix", "doors":2},
    {"id":5, "size" : "l", "fuel":"petrol", "doors":4},
]


@app.get("/")
def get_cars(size: Optional[str]= None, fuel: Optional[str]= None):
    filter_db = db

    if size:
        filter_db = [car for car in filter_db if car["size"] == size]
    if fuel:
        filter_db = [car for car in filter_db if car["fuel"] == fuel]
    return filter_db

@app.post("/add_cars/")
def add_cars(size:str, fuel:str, doors:int):
    new_car={
        "id":len(db) + 1,
        "size": size,
        "fuel": fuel,
        "doors": doors
    }
    db.append(new_car)
    return add_cars