from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import Student
from app.database.schemas import StudentBase, StudentPut

router = APIRouter()

@router.get("")
async def get_all(db: Session = Depends(get_db)):
    return db.query(Student).all()

@router.get("/{cccd}")
async def get(cccd: str, db: Session = Depends(get_db)):
    return db.query(Student).filter(Student.cccd == cccd).first()

@router.post("")
async def post(payload: StudentBase, db: Session = Depends(get_db)):
    student = Student(**payload.model_dump())
    db.add(student)
    db.commit()
    db.refresh(student)

    return student

@router.put("/{cccd}")
async def put(cccd: str, payload: StudentPut, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.cccd == cccd).first()
    
    if student is None:
        return None
    
    student.name = payload.name
    student.phone = payload.phone

    db.commit()
    db.refresh(student)

    return student

@router.delete("/{cccd}")
async def delete(cccd: str, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.cccd == cccd).first()
    if student is None:
        return "failed"
    db.delete(student)
    db.commit()
    return "ok"