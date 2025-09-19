SEC_TEAMS = {
    "Alabama Crimson Tide": "alabama-crimson-tide",
    "Georgia Bulldogs": "georgia-bulldogs",
    "LSU": "lsu",
    "Florida Gators": "florida-gators",
    "Tennessee Volunteers": "tennessee-volunteers",
}

def hello():
    return "Hello, DevOps!"

def team_slug(name: str) -> str:
    n = " ".join(name.split()).strip()
    for k, v in SEC_TEAMS.items():
        if k.lower() == n.lower():
            return v
    return n.lower().replace(" ", "-")

def is_sec_team(name: str) -> bool:
    n = " ".join(name.split()).strip().lower()
    return any(k.lower() == n for k in SEC_TEAMS)

def rankings_top3(ranking: list[str]) -> list[str]:
    return ranking[:3]

def format_score(home: int, away: int) -> str:
    if not isinstance(home, int) or not isinstance(away, int):
        raise TypeError("scores must be integers")
    return f"{home}-{away}"

if __name__ == "__main__":
    print(hello())
