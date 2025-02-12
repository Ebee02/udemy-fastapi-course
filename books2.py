from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    decripion: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, decription, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.decription = decription
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="Id is not require on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    decription: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2026)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "New Book",
                "author": "John Doe",
                "decription": "Lorem",
                "rating": 5,
                "published_date": 2001,
            }
        }
    }


BOOKS = [
    Book(1, "Computer Science Pro", "CodingWithLawrence", "A very nice book", 5, 2010),
    Book(2, "Be Fast with FastAPI", "CodingWithLawrence", "A great book", 5, 2001),
    Book(3, "Master Endpoints", "CodingWithLawrence", "A awesome book", 5, 2003),
    Book(4, "HP1", "Author 1", "Book Decription", 2, 2007),
    Book(5, "HP2", "Author 2", "Book Decription", 3, 2002),
    Book(6, "HP3", "Author 3", "Book Decription", 1, 2010),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get("/book/publish/", status_code=status.HTTP_200_OK)
async def read_book_by_publish_date(published_date: int = Query(gt=1999, lt=2026)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


@app.post("/create_books", status_code=status.HTTP_201_CREATED)
async def create_books(book_req: BookRequest):
    new_book = Book(**book_req.model_dump())
    BOOKS.append(find_book_id(new_book))


@app.put("/update_books", status_code=status.HTTP_204_NO_CONTENT)
async def update_books(book_req: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_req.id:
            BOOKS[i] = book_req
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/delete_books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_books(book_id: int = Path(gt=0, lt=6)):
    book_deleted = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_deleted = True
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail="Item not found")


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
