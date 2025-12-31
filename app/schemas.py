from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    description: str
    author: str
    year: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    class config:
        from_attribute = True