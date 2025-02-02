import csv


class MyDialect(csv.Dialect):
    delimiter = ","
    quotechar = '"'
    lineterminator = "\n"
    quoting = csv.QUOTE_ALL


csv.register_dialect("dialect", MyDialect)

mas_grade = []


def reading_grade():
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


def average_grade(grads):
    if not grads:
        return 0
    try:
        sum_grade = sum(float(i) for i in grads)
        return sum_grade / len(grads)
    except ZeroDivisionError:
        return "No grades available"


def add_student(name, age, grade):
    with open("file_students.csv", "a", newline="", encoding="utf-8") as f:
        writen = csv.writer(f)
        writen.writerow([name, age, grade])


if __name__ == "__main__":
    print(average_grade(reading_grade()))
    add_student("Lena", 20, 5)
    print(average_grade(reading_grade()))
