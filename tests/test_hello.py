from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))

import importlib

def test_team_slug_basic_cases():
    m = importlib.import_module("hello")
    assert m.team_slug("Alabama Crimson Tide") == "alabama-crimson-tide"
    assert m.team_slug("Georgia Bulldogs") == "georgia-bulldogs"
    assert m.team_slug("LSU") == "lsu"

def test_is_sec_true_and_false():
    m = importlib.import_module("hello")
    assert m.is_sec("alabama-crimson-tide") is True
    assert m.is_sec("georgia-bulldogs") is True
    assert m.is_sec("not-a-team") is False

def test_sec_division_values():
    m = importlib.import_module("hello")
    assert m.sec_division("alabama-crimson-tide") == "West"
    assert m.sec_division("georgia-bulldogs") == "East"
    assert m.sec_division("not-a-team") is None

def test_greeting():
    m = importlib.import_module("hello")
    assert m.greeting().lower().startswith("welcome")

def test_module_has_expected_symbols():
    m = importlib.import_module("hello")
    for sym in ("team_slug", "is_sec", "sec_division", "greeting", "TEAMS"):
        assert hasattr(m, sym)
