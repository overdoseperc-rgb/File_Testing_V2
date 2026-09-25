import json
from pathlib import Path
import pytest
from superheroes import create_superhero_file, NEW_HEROES

def test_sorted_file(tmp_path):
    source = Path(__file__).resolve().parents[1] / "data/SuperHero.json"
    original = source.read_bytes()
    target = create_superhero_file(source, tmp_path / "superhero_new.json")
    data = json.loads(target.read_text(encoding="utf-8"))
    before = json.loads(original)
    assert [hero["age"] for hero in data["members"]] == [19, 25, 31, 38, 45]
    assert len(data["members"]) == len(before["members"]) + 2
    for hero in before["members"] + NEW_HEROES:
        assert hero in data["members"]
    assert {k: v for k, v in data.items() if k != "members"} == {k: v for k, v in before.items() if k != "members"}
    assert source.read_bytes() == original

@pytest.mark.parametrize("data", [{}, {"members": [{"name": "A", "age": "9"}]}, {"members": [{"name": "A", "age": -1}]}])
def test_invalid_json_schema(tmp_path, data):
    source = tmp_path / "input.json"
    source.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(ValueError):
        create_superhero_file(source, tmp_path / "out.json")
    assert not (tmp_path / "out.json").exists()
