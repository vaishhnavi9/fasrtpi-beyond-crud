from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy import Column

class ReviewModel(BaseModel):
    uid: uuid.UUID
    ratings: int=Field(lt=5)
    review_text:str
    user_uid: Optional[uuid.UUID]
    book_uid:Optional[uuid.UUID]
    created_at:datetime
    updated_at:datetime

class ReviewCreateModel(BaseModel):
    ratings: int=Field(lt=5)
    review_text:str

