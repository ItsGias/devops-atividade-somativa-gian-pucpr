from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))


import importlib

def test_team_slug_basic_cases():
    m = importlib.import_module("hello")
    assert m.team_slug("Alabama Crimson Tide") == "alabama-crimson-tide"
    assert m.team_slug("Georgia Bulldogs") == "georgia-bulldogs"
    assert m.team_slug("LSU") == "lsu"


def test_team_slug_ignores_case_and_spaces():
    assert m.team_slug("   georgia   bulldogs  ") == "georgia-bulldogs"
    assert m.team_slug("FlOrIdA Gators") == "florida-gators"

def test_is_sec_team_true_false():
    assert m.is_sec_team("Tennessee Volunteers") is True
    assert m.is_sec_team("Ohio State Buckeyes") is False

def test_rankings_top3():
    r = ["Georgia Bulldogs", "Alabama Crimson Tide", "LSU", "Florida Gators"]
    assert m.rankings_top3(r) == ["Georgia Bulldogs", "Alabama Crimson Tide", "LSU"]
    assert m.rankings_top3(r[:2]) == ["Georgia Bulldogs", "Alabama Crimson Tide"]

def test_format_score_ok_and_error():
    assert m.format_score(24, 20) == "24-20"
    import pytest
    with pytest.raises(TypeError):
        m.format_score("24", 20)
