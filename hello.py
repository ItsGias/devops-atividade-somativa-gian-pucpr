import re

def team_slug(name: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

TEAMS = {
    "alabama-crimson-tide": {"conf": "SEC", "div": "West"},
    "georgia-bulldogs": {"conf": "SEC", "div": "East"},
    "lsu": {"conf": "SEC", "div": "West"},
    "tennessee-volunteers": {"conf": "SEC", "div": "East"},
    "florida-gators": {"conf": "SEC", "div": "East"},
}

def is_sec(slug: str) -> bool:
    return slug in TEAMS

def sec_division(slug: str):
    t = TEAMS.get(slug)
    return t["div"] if t else None

def greeting() -> str:
    return "Welcome to the SEC!"
