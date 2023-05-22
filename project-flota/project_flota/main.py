from fastapi import FastAPI
from project_flota.routers import cars

app = FastAPI()
app.include_router(cars.router)




