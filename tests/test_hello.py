import importlib

m = importlib.import_module("hello")

def test_team_slug_basic_cases():
    assert m.team_slug("Alabama Crimson Tide") == "alabama-crimson-tide"
    assert m.team_slug("Georgia Bulldogs") == "georgia-bulldogs"
    assert m.team_slug("LSU") == "lsu"

def test_is_sec_true():
    assert m.is_sec("lsu") is True

def test_is_sec_false():
    assert m.is_sec("ohio-state") is False

def test_sec_division_known():
    assert m.sec_division("lsu") in ("West", "East")

def test_greeting():
    assert m.greeting() == "Welcome to the SEC!"
