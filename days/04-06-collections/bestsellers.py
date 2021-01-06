import csv
from collections import defaultdict, namedtuple, Counter
from pathlib import Path
from pprint import pprint as pp

base_dir = Path(__file__).resolve().parent

fname = 'bestsellers.csv'
local = base_dir / fname

BOOK_DATA = local

Book = namedtuple('Book', 'name rating reviews price year genre')


def get_books_by_author():
    """Extracts all books from csv and stores them in a dict,
        where keys are authors, and values are a list of books"""
    books = defaultdict(list)
    with open(BOOK_DATA, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                author = row['Author']
                book = Book(name=row['Name'],
                            rating=float(row['User Rating']),
                            reviews=int(row['Reviews']),
                            price=int(row['Price']),
                            year=int(row['Year']),
                            genre=row['Genre'],
                            )
                books[author].append(book)
            except ValueError:
                continue
        return books


def get_multiyear_books(books):
    """
        Get books that have been bestsellers in more than one year"""
    multi_books = defaultdict(list)
    cnt = Counter()
    for author, books in books.items():
        cnt.clear()
        for book in books:
            cnt[book.name] += 1
        for book, count in cnt.items():
            if count > 1:
                multi_books[author].append(book)
    return multi_books


if __name__ == '__main__':
    books = get_books_by_author()
    mbooks = get_multiyear_books(books)
    pp(mbooks)
