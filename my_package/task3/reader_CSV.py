import csv


class MyDialect(csv.Dialect):
    delimiter = ","
    quotechar = '"'
    lineterminator = "\n"
    quoting = csv.QUOTE_ALL


csv.register_dialect("dialect", MyDialect)

mas_grade = []


def reading_grade():
    """Reads student grades from a CSV file.
    This function opens the "file_students.csv" file, reads student data,
    and extracts the grades into a list."""
    try:
        with open("file_students.csv", encoding="utf-8") as csv_file:
            data = csv.reader(csv_file, dialect="dialect", delimiter=",")
            next(data)
            for row in data:
                name, age, grade = row
                mas_grade.append(int(grade))

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    return mas_grade


def average_grade(grads: list[int]) -> float:
    """Calculates the average grade from a list of grades.
    Handles empty lists and potential ZeroDivisionError.
    If the input list is empty, returns 0. If a ZeroDivisionError occurs, returns "No grades available".
    """
    if not grads:
        return 0
    try:
        sum_grade = sum(float(i) for i in grads)
        return sum_grade / len(grads)
    except ZeroDivisionError:
        return 0


def add_student(name: str, age: int, grade: int) -> None:
    """Adds a new student's information to the CSV file.
    Appends a new row with the student's name, age, and grade to "file_students.csv".
    """
    with open("file_students.csv", "a", newline="", encoding="utf-8") as file:
        writen = csv.writer(file)
        writen.writerow([name, age, grade])


if __name__ == "__main__":
    print(average_grade(reading_grade()))
    add_student("Lera", 20, 5)
    print(average_grade(reading_grade()))
