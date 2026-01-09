from sqlalchemy.orm import Session
from .schemas import BookCreate
from .models import book

def create_book(database: Session, data: BookCreate):
    book_instance = book(**data.model_dump())
    database.add(book_instance)
    database.commit()
    database.refresh(book_instance)
    return book_instance

def get_all_books(database: Session):
    return database.query(book).all()

def get_book_by_id(database: Session, book_id: int):
    return database.query(book).filter(book.id == book_id).first()


def update_book(database: Session, book_data: BookCreate, book_id: int):
    book_queryset = database.query(book).filter(book.id == book_id).first()
    if book_queryset:
        for key, val in book_data.model_dump().items():
            setattr(book_queryset, key, val)
        database.commit()
        database.refresh(book_queryset)
    return book_queryset


def delete_book(database: Session,id: int):
    book_queryset = database.query(book).filter(book.id == id).first()
    if book_queryset:
        database.delete(book_queryset)
        database.commit()
    return book_queryset