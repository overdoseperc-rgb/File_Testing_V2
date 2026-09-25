import json
from pathlib import Path

NEW_HEROES = [
    {"name": "Night Owl", "age": 25, "secretIdentity": "Anna North", "powers": ["Night vision"]},
    {"name": "Solar Guard", "age": 38, "secretIdentity": "Ivan Sun", "powers": ["Solar energy"]},
]

def create_superhero_file(source: str | Path, target: str | Path) -> Path:
    """Сохранить метаданные команды, добавить героев и сортировать members по возрасту."""
    data = json.loads(Path(source).read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict) or not isinstance(data.get("members"), list):
        raise ValueError("Ожидается JSON-объект с массивом members")
    members = data["members"]
    for hero in members:
        if (not isinstance(hero, dict) or not isinstance(hero.get("name"), str)
                or type(hero.get("age")) is not int or hero["age"] < 0):
            raise ValueError("У героя должны быть name и неотрицательный целый age")
    members.extend(NEW_HEROES)
    data["members"] = sorted(members, key=lambda hero: hero["age"])
    target = Path(target)
    if target.resolve() == Path(source).resolve():
        raise ValueError("Результат должен быть новым файлом")
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return target
