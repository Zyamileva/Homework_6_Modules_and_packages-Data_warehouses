import json
from json import JSONDecodeError


def reading_books():
    """Reads book data from a JSON file.
    Loads book data from "file_books.json" and returns it as a list of dictionaries.
    Handles FileNotFoundError and JSONDecodeError gracefully.
    """
    try:
        with open("file_books.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def sample_data(data_books: dict) -> list:
    """Return books that are currently available.
    Filters a list of books to include only those marked as available.
    """
    return [book for book in data_books if book["наявність"]]


def add_book(title: str, author: str, year: int, availability: bool = "true") -> None:
    """Adds a new book to the library.
    Appends a new book entry to the books data and saves it to a JSON file.
    """
    books = reading_books()
    books.append(
        {"назва": title, "автор": author, "рік": year, "наявність": availability}
    )
    try:
        with open("file_books.json", "w", encoding="utf-8") as open_file:
            json.dump(books, open_file, indent=4, ensure_ascii=False)
    except JSONDecodeError as e:
        print(f"Error occurred during writing data: {e}")
    print(f"book {title} added to library")


if __name__ == "__main__":
    data_result = reading_books()
    print(sample_data(data_result))
    add_book("Книга 4", "Автор 4", 3000)
    print(sample_data(data_result))
