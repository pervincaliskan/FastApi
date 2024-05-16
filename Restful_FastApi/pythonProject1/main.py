from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Örnek veritabanı yerine basit bir liste kullanıyoruz
authors_db = []
books_db = []
comments_db = []
users_db = []
categories_db = []


# Modeller
class Author(BaseModel):
    name: str
    nationality: str


class Book(BaseModel):
    title: str
    author: str
    year: int
    genre: Optional[str] = None
    category: Optional[str] = None


class Comment(BaseModel):
    book_title: str
    text: str
    user: str


class User(BaseModel):
    username: str
    email: str
    password: str


class Category(BaseModel):
    name: str


# Fonksiyonlar
def get_author(author_id: int):
    if author_id >= len(authors_db):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Author not found")
    return authors_db[author_id]


def get_book(book_title: str):
    for book in books_db:
        if book.title == book_title:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


def get_user(username: str):
    for user in users_db:
        if user.username == username:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


# Yazarlar Servisi
@app.get("/authors/", response_model=List[Author])
def get_authors():
    return authors_db


@app.post("/authors/")
def create_author(author: Author):
    authors_db.append(author)
    return author


@app.put("/authors/{author_id}")
def update_author(author_id: int, author: Author):
    authors_db[author_id] = author
    return {"message": "Author updated successfully"}


@app.delete("/authors/{author_id}")
def delete_author(author_id: int):
    del authors_db[author_id]
    return {"message": "Author deleted successfully"}


# Kitaplar Servisi
@app.get("/books/", response_model=List[Book])
def get_books():
    return books_db


@app.post("/books/")
def create_book(book: Book):
    books_db.append(book)
    return book


@app.put("/books/{book_title}")
def update_book(book_title: str, book: Book):
    old_book = get_book(book_title)
    old_book.title = book.title
    old_book.author = book.author
    old_book.year = book.year
    old_book.genre = book.genre
    old_book.category = book.category
    return {"message": "Book updated successfully"}


@app.delete("/books/{book_title}")
def delete_book(book_title: str):
    book = get_book(book_title)
    books_db.remove(book)
    return {"message": "Book deleted successfully"}


# Yorumlar Servisi
@app.get("/comments/", response_model=List[Comment])
def get_comments():
    return comments_db


@app.post("/comments/")
def create_comment(comment: Comment, username: str = Depends(get_user)):
    comments_db.append(comment)
    return comment


# Kullanıcılar Servisi
@app.get("/users/", response_model=List[User])
def get_users():
    return users_db


@app.post("/users/")
def create_user(user: User):
    users_db.append(user)
    return user


# Kategoriler Servisi
@app.get("/categories/", response_model=List[Category])
def get_categories():
    return categories_db


@app.post("/categories/")
def create_category(category: Category):
    categories_db.append(category)
    return category
