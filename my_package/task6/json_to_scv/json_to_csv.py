import csv
import json

JSON_FILE = "file_books.json"
CSV_FILE = "file_books.scv"


def converter():
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file_json:
            data = json.load(file_json)
            if not data:
                return "There is no data in the file."
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        return "File converted!"
    except FileNotFoundError:
        return "There is no file"
    except json.JSONDecodeError as e:
        return f"Error {e}"


if __name__ == "__main__":
    converter()
