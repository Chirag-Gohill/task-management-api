from fastapi import FastAPI, Depends, HTTPException
from app import schemas, models, services
from .database import engine, get_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/books/", response_model=list[schemas.Book])
def get_all_books(database: Session = Depends(get_db)):
    return services.get_all_books(database)

@app.get('/books/{id}', response_model=schemas.Book)
def get_book_by_id(id: int,database: Session = Depends(get_db)):
    book_queryset = services.get_book_by_id(database,id)
    if book_queryset:
        return book_queryset
    raise HTTPException(status_code=404, detail="Invalid Book id Provided")

@app.put('/books/{id}', response_model=schemas.Book)
def update_book(book: schemas.BookCreate, id:int ,database: Session = Depends(get_db)):
    db_update = services.update_book(database, book, id)
    if not db_update:
        raise HTTPException(status_code=404, detail="Book Not Found")
    return db_update

@app.post('/books/', response_model=schemas.Book)
def create_new_book(book: schemas.BookCreate, database: Session = Depends(get_db)):
    return services.create_book(database, book)

@app.delete('/books/{id}', response_model= schemas.Book)
def delete_book(id:int, database: Session = Depends(get_db)):
    delete_entry = services.delete_book(database, id)
    if delete_entry:
        return delete_entry
    raise HTTPException(status_code=404, detail="Book Not FOund")