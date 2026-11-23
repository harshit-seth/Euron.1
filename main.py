from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Radhi(BaseModel):
    name: str
    age: int
    hobbies: List[str]
    origin: str


Radhis: List[Radhi] = []


@app.get("/radhis")
def get_radhis():
    return Radhis


@app.post("/radhis")
def create_radhi(radhi: Radhi):
    Radhis.append(radhi)
    return radhi


@app.put("/radhis/{radhid_id}")
def update_radhi(radhid_id: int, radhi: Radhi):
    if radhid_id < 0 or radhid_id >= len(Radhis):
        raise HTTPException(status_code=404, detail="Radhi not found")
    Radhis[radhid_id] = radhi
    return radhi


@app.delete("/radhis/{radhid_id}")
def delete_radhi(radhid_id: int):
    if radhid_id < 0 or radhid_id >= len(Radhis):
        raise HTTPException(status_code=404, detail="Radhi not found")
    deleted_radhi = Radhis.pop(radhid_id)
    return deleted_radhi