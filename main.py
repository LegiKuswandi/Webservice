from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Mahasiswa(BaseModel):
    id: str
    name: str
    nim: str
    jenis_kelamin: str
    umur: str
    asal_kota: str

mahasiswa_data = {"data":[
    {"id": "1", "name": "Legi Kuswandi", "nim": "2203335","jenis_kelamin":"L", "umur":"20", "asal_kota":"Sukabumi"},
    {"id": "2", "name": "Shidiq Arifin Sudrajat", "nim": "2201143","jenis_kelamin":"L", "umur":"20", "asal_kota":"Bandung"},
    {"id": "3", "name": "Iqbal Fadhilah", "nim": "2202255","jenis_kelamin":"L", "umur":"19", "asal_kota":"Jakarta"},
], "message":"success", "error":"false"}

@app.get("/daftar_mahasiswa")
async def get_mahasiswa():
    return mahasiswa_data


@app.get("/detil_mahasiswa/{mahasiswa_id}", response_model=Mahasiswa)
async def get_mahasiswa_detail(mahasiswa_id: str):
    for mahasiswa in mahasiswa_data["data"]:
        if mahasiswa["id"] == mahasiswa_id:
            return mahasiswa
    return {"message": "Mahasiswa not found"}
