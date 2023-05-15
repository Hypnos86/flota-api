from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CarShema(BaseModel):
    name: str


@app.get("/cars")
async def index(page: int = 0):
    return {"message": f"lista aut - strona {page}"}


@app.get("/cars/{car_id}")
async def get(car_id: int):
    return {"message": f"dodanie auta {car_id}"}


@app.delete("/cars/{car_id}")
async def delete(car_id: int):
    return {"message": f"usuniecie auta {car_id}"}


@app.put("/cars/<id>")
async def put():
    return {"message": "put dla auta"}


@app.post("/cars")
async def add(car: CarShema) -> dict[str, str]:
    print(car)
    return {"message": f"post dla auta {car.name}"}
