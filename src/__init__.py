from fastapi import FastAPI,status
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.errors import register_all_errors
from .middleware import register_middleware
from fastapi import status
from .errors import (
   create_exception_handler,
   InvalidCredentials,
   BookNotFound,
   UserAlreadyExists,
   UserNotFound,
   InsufficientPermission,
   AccessTokenRequired,
   InvalidToken,
   RefreshTokenRequired,
   RevokedToken
)
@asynccontextmanager
async def life_span(app:FastAPI):
   print(f"Server is starting....") 
   from src.db.models import Book
   await init_db()
   yield
   print(f"server has stopped")

version="v1"

app=FastAPI(
    title="Bookly",
    description="A REST Api for a book  review web service",
    version=version
   

)
register_all_errors(app)
register_middleware(app)






app.include_router(book_router,prefix=f"/api/{version}/books", tags=['books'])
app.include_router(auth_router,prefix=f"/api/{version}/auth", tags=['auth'])
app.include_router(review_router,prefix=f"/api/{version}/reviews", tags=['reviews'])


