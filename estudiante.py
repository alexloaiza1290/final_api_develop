from fastapi import APIRouter, Depends, HTTPException, Form, Path, Query, Request
from datetime import datetime
from bson import ObjectId
from database import get_db
from models import EstudianteBase, EstudianteCreate  # Asegúrate de tener este modelo
from typing import List, Optional

router = APIRouter(prefix="/estudiante", tags=["Estudiantes"])

@router.post("/create-json", response_model=EstudianteBase)
async def create_one_estudiante_json(
    estudiante: EstudianteCreate,
    db=Depends(get_db)
):
    try:
        data = estudiante.model_dump(by_alias=True)
        data["_id"] = ObjectId()
        result = db["estudiante"].insert_one(data)
        created_estudiante = db["estudiante"].find_one({"_id": result.inserted_id})
        if created_estudiante:
            created_estudiante["_id"] = str(created_estudiante["_id"])
            return EstudianteBase(**created_estudiante)
        raise HTTPException(status_code=500, detail="Error retrieving created estudiante")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creando estudiante: {e}")

@router.post("/create-form", response_model=EstudianteBase)
def create_one_estudiante_form(
    nombre: str = Form(..., min_length=1, max_length=20),
    apellido: str = Form(..., min_length=1, max_length=20),
    aprobado: bool = Form(...),
    nota: float = Form(...),
    fecha: datetime = Form(...),
    db=Depends(get_db)
):
    try:
        estudiante_data = {
            "nombre": nombre,
            "apellido": apellido,
            "aprobado": aprobado,
            "nota": nota,
            "fecha": fecha
        }
        result = db["estudiante"].insert_one(estudiante_data)
        created_estudiante = db["estudiante"].find_one({"_id": result.inserted_id})
        if created_estudiante:
            created_estudiante["_id"] = str(created_estudiante["_id"])  # Convierte ObjectId a string
            return EstudianteBase(**created_estudiante)
        raise HTTPException(status_code=500, detail="Error retrieving created estudiante")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creando estudiante: {e}")

def convert_objectid_to_str(data):
    if isinstance(data, dict):
        if "_id" in data and isinstance(data["_id"], ObjectId):
            data["_id"] = str(data["_id"])
        for key, value in data.items():
            data[key] = convert_objectid_to_str(value)
    elif isinstance(data, list):
        data = [convert_objectid_to_str(item) for item in data]
    return data

@router.get("/", response_model=List[EstudianteBase])
def get_all_estudiantes(db=Depends(get_db)):
    try:
        estudiante_list = db["estudiante"].find()
        return [EstudianteBase(**convert_objectid_to_str(estudiante)) for estudiante in estudiante_list]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error obteniendo estudiantes: {e}")

@router.get("/buscar", response_model=List[EstudianteBase])
def buscar_estudiantes(
    nombre: Optional[str] = Query(None, min_length=1, max_length=255),
    db=Depends(get_db)
):
    try:
        filtro = {"nombre": {"$regex": nombre, "$options": "i"}} if nombre else {}
        estudiante_list = db["estudiante"].find(filtro)
        return [EstudianteBase(**convert_objectid_to_str(estudiante)) for estudiante in estudiante_list]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error buscando estudiantes: {e}")

@router.get("/{estudiante_id}", response_model=EstudianteBase)
def get_one_estudiante(
    estudiante_id: str = Path(..., min_length=24, max_length=24, pattern="^[0-9a-fA-F]{24}$"),
    db=Depends(get_db)
):
    try:
        estudiante = db["estudiante"].find_one({"_id": ObjectId(estudiante_id)})
        if not estudiante:
            raise HTTPException(status_code=404, detail="estudiante no encontrado")
        return EstudianteBase(**convert_objectid_to_str(estudiante))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error obteniendo estudiante: {e}")

@router.patch("/edit/{estudiante_id}", response_model=EstudianteBase)
def edit_one_estudiante(estudiante_id: str, estudiante: EstudianteBase, db=Depends(get_db)):
    try:
        existing_estudiante = db["estudiante"].find_one({"_id": ObjectId(estudiante_id)})
        if not existing_estudiante:
            raise HTTPException(status_code=404, detail="estudiante no encontrado")

        update_data = estudiante.model_dump(by_alias=True, exclude_unset=True)
        if "_id" in update_data:
            del update_data["_id"]

        db["estudiante"].update_one({"_id": ObjectId(estudiante_id)}, {"$set": update_data})

        updated_estudiante = db["estudiante"].find_one({"_id": ObjectId(estudiante_id)})
        if updated_estudiante:
            return EstudianteBase(**convert_objectid_to_str(updated_estudiante))
        raise HTTPException(status_code=500, detail="Error retrieving updated estudiante")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error editando estudiante: {e}")

@router.delete("/delete/{estudiante_id}")
def delete_one_estudiante(estudiante_id: str, db=Depends(get_db)):
    try:
        estudiante = db["estudiante"].find_one({"_id": ObjectId(estudiante_id)})
        if not estudiante:
            raise HTTPException(status_code=404, detail="estudiante no encontrado")
        db["estudiante"].delete_one({"_id": ObjectId(estudiante_id)})
        return {"message": "estudiante eliminado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error eliminando estudiante: {e}")
