from pydantic import BaseModel
from datetime import datetime, date
import uuid
from src.reviews.schemas import ReviewModel
from typing import List
class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at:datetime
    updated_at:datetime

class BookDetailModel(Book):
    reviews:List[ReviewModel]
    

class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date:date
    page_count: int
    language: str
    
class BookUpdate(BaseModel):
    
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
