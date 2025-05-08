from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import Book
from app.database.schemas import BookBase, BookPut

router = APIRouter()

@router.get("")
async def get_all(db: Session = Depends(get_db)):
    return db.query(Book).all()

@router.get("/{id}")
async def get(id: int, db: Session = Depends(get_db)):
    return db.query(Book).filter(Book.id == id).first()


@router.post("")
async def post(book: BookBase, db: Session = Depends(get_db)):
    book = Book(**book.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)

    return book

@router.put("/{id}")
async def put(id: int, payload: BookPut, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    
    if book is None:
        return None
    
    book.title = payload.title

    db.commit()
    db.refresh(book)

    return book

@router.delete("/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        return "failed"
    db.delete(book)
    db.commit()
    return "ok"