import csv
import json

JSON_FILE = "file_books.json"
CSV_FILE = "file_books.scv"


def converter():
    """Converts a CSV file to a JSON file.
    Reads data from the CSV file specified by CSV_FILE, converts it to JSON format,
    and writes the JSON data to the file specified by JSON_FILE.
    """
    try:
        with open(CSV_FILE, "r", encoding="utf-8") as file_csv:
            reader = csv.DictReader(file_csv)
            data = list(reader)
            if not data:
                return "There is no data in the file."

        with open(JSON_FILE, "w", encoding="utf-8") as file_json:
            json.dump(data, file_json, indent=4, ensure_ascii=False)
        return "File converted!"
    except FileNotFoundError:
        return "There is no file"
    except json.JSONDecodeError as e:
        return f"Error {e}"


if __name__ == "__main__":
    converter()
