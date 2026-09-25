import csv
import math
from pathlib import Path

def average_grade(filename: str | Path) -> float:
    """Среднее по всем строкам столбца grade; допустимы оценки от 2 до 5."""
    grades = []
    with Path(filename).open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or "grade" not in reader.fieldnames:
            raise ValueError("Нет столбца grade")
        for number, row in enumerate(reader, start=2):
            try:
                grade = float(row["grade"])
            except (ValueError, TypeError) as error:
                raise ValueError(f"Некорректная оценка в строке {number}") from error
            if not math.isfinite(grade) or not 2 <= grade <= 5:
                raise ValueError(f"Оценка вне диапазона 2..5 в строке {number}")
            grades.append(grade)
    if not grades:
        raise ValueError("Нет оценок")
    return math.fsum(grades) / len(grades)
