from pathlib import Path
from grades import average_grade
from superheroes import create_superhero_file

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    print("Средняя оценка:", average_grade(root / "data/grades.csv"))
    print("Создан:", create_superhero_file(root / "data/SuperHero.json", root / "superhero_new.json"))
