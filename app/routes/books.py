from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models import Book
from app.database.schemas import PostBase

router = APIRouter()

@router.get("")
async def get(db: Session = Depends(get_db)):
    return db.query(Book).all()


@router.post("")
async def post(book: PostBase, db: Session = Depends(get_db)):
    book = Book(**book.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)

    return book