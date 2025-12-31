from database import base
from sqlalchemy import Column, Integer, String

class book(base):
    __tablename__ = "books"

    id = Column(Integer, primary_key = True, index = True)
    description = Column(String, index = True)
    title = Column(String, index = True)
    year = Column(Integer)
    author = Column(String, index = True)
