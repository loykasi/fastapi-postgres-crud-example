from fastapi import APIRouter
from app.routes import books, students

router = APIRouter()

router.include_router(books.router, tags=["books"], prefix="/books")
router.include_router(students.router, tags=["students"], prefix="/students")