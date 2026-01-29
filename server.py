from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
database = []

class Mahasiswa(BaseModel):
    nama: str
    nim: str
    jurusan: str

@app.post("/tambah")
def tambah_mahasiswa(mhs: Mahasiswa):
    database.append(mhs.dict())
    return {"message": "Data mahasiswa ditambahkan"}

@app.get("/mahasiswa")
def get_mahasiswa():
    return database
