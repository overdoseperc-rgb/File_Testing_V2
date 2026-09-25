"""Намеренно ошибочные алгоритмы. Запускать отдельно от основной серии."""
import csv
from pathlib import Path
import pytest

@pytest.mark.parametrize("bug", ["floor_division", "wrong_divisor", "skip_last"])
def test_known_bug(bug):
    path = Path(__file__).resolve().parents[1] / "data/grades.csv"
    with path.open(encoding="utf-8", newline="") as stream:
        values = [float(row["grade"]) for row in csv.DictReader(stream)]
    if bug == "floor_division":
        actual = sum(values) // len(values)
    elif bug == "wrong_divisor":
        actual = sum(values) / (len(values) + 1)
    else:
        actual = sum(values[:-1]) / len(values[:-1])
    assert actual == pytest.approx(3.75)
