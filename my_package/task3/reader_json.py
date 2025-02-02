import json
from json import JSONDecodeError


def reading_books():
    try:
        with open("file_books.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def sample_data(data_books):
    return [book for book in data_books if book["наявність"]]


def add_book(title, author, year, availability="true"):
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
    add_book("Книга 3", "Автор 3", 2000)
    print(sample_data(data_result))
