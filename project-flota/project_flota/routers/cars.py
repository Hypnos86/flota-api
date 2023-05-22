from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/cars",
    tags=["cars"]
)

class CarShema(BaseModel):
    name: str


cars: List[CarShema] = [{"name":"Porshe"}]


# @router.post("/")
# async def add(car: CarShema) -> CarShema:
#     print(car)
#     return {"message": f"post dla auta {car.name}"}

@router.post('/', status_code=201)
async def add(car: CarShema) -> List[CarShema]:
    cars.append(car)
    return cars

# ----------------------------------------------------------


# @router.get("/")
# async def index(page: int = 0):
#     return {"message": f"lista aut - strona {page}"}

@router.get('/')
async def index(page: int = 0) -> List[CarShema]:
    return cars

# ----------------------------------------------------------
# @router.get("/{car_id}")
# async def get(car_id: int):
#     return {"message": f"dodanie auta {car_id}"}

@router.get("/{car_id}")
async def get(car_id: int) -> CarShema:
    try:
        return cars[car_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Nie ma takiego samochodu")

# ----------------------------------------------------------
@router.delete("/{car_id}")
async def delete(car_id: int) -> List[CarShema]:
    get_car(car_id)
    del cars[car_id]
    return cars

@router.put("/<id>")
async def update(car_id: int, car: CarShema) -> List[CarShema]:
    get_car(car_id)
    return cars
def get_car(car_id: int) -> CarShema:
    try:
        return cars[car_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="nie ma takiego statku")
