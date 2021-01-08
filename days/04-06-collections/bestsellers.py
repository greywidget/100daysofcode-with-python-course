import csv
from collections import defaultdict, namedtuple, Counter
from pathlib import Path

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


def get_book_count(books):
    """
        Get books that have been bestsellers in more than one year"""
    cnt = Counter()
    for author, books in books.items():
        for book in books:
            cnt[(author, book.name)] += 1
    return cnt


def print_n_most_common_books(books, book_count, n_most_common=3):
    years = defaultdict(list)
    for (author, book_name), count in book_count.most_common(n_most_common):
        print(author)
        years.clear()
        for book in sorted(books[author], key=lambda x: x.year):
            if book.name == book_name:
                years[book_name].append(book.year)
        print("\t", book_name)
        print(f'\t{years[book_name]} {count=}')


if __name__ == '__main__':
    books = get_books_by_author()
    book_count = get_book_count(books)
    print_n_most_common_books(books, book_count, 10)
