from pathlib import Path
import pytest
from grades import average_grade

DATA = Path(__file__).resolve().parents[1] / "data"

def test_real_average():
    # Независимый эталон: (5 + 4 + 2 + 4) / 4 = 3.75.
    assert average_grade(DATA / "grades.csv") == pytest.approx(3.75)

@pytest.mark.parametrize("values, expected", [("2", 2), ("5", 5), ("2\n5", 3.5), ("4\n4\n4", 4)])
def test_average_cases(tmp_path, values, expected):
    path = tmp_path / "grades.csv"
    path.write_text("grade\n" + values, encoding="utf-8")
    assert average_grade(path) == pytest.approx(expected)

@pytest.mark.parametrize("content", ["grade\n", "score\n5", "grade\nabc", "grade\n1", "grade\n6", "grade\nnan", "grade\ninf", "student,grade\nAnna,"])
def test_bad_data(tmp_path, content):
    path = tmp_path / "bad.csv"
    path.write_text(content, encoding="utf-8")
    with pytest.raises(ValueError):
        average_grade(path)
