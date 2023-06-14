from pydantic import BaseModel
from datetime import datetime
from datetime import date

class Cliente(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: date
    genero: str
    correo_electronico: str
    telefono: str
    correo_electronico: str
    direccion: str
    ciudad: str
    estado: str
    pais: str
    codigo_postal: str
    telefono: str
    saldo_ahorros: str
    class Config:
        orm_mode = True
        datetime_format = '%Y-%m-%d'