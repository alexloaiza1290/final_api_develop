from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

class EstudianteCreate(BaseModel):
    nombre: str
    apellido: str
    aprobado: bool
    nota: float
    fecha: datetime

class EstudianteBase(BaseModel):
    id: Optional[str] = Field(alias="_id", default=None)
    nombre: str = Field(..., min_length=1, max_length=20)
    apellido: str = Field(..., min_length=1, max_length=255)
    aprobado: bool = Field(...)
    nota: float = Field(..., ge=0, le=10)
    fecha: datetime = Field(...)