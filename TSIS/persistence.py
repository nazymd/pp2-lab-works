import json
from datetime import datetime

SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"


def load_settings():
    try:
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    except:
        data = {
            "sound": True,
            "car_color": [0, 100, 255],
            "difficulty": "normal"
        }
        save_settings(data)
        return data


def save_settings(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_score(name, score, distance):
    data = load_leaderboard()

    data.append({
        "name": name,
        "score": int(score),
        "distance": int(distance),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)