import os
from datetime import datetime

def save_recommendations(profile, items):
    os.makedirs("outputs", exist_ok=True)
    path = "outputs/recommendations.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write("PERSONALIZED RECOMMENDATIONS\n")
        f.write("=" * 32 + "\n")
        f.write(f"Name: {profile.get('name', '')}\n")
        f.write(f"Goal: {profile.get('goal', '')}\n")
        f.write(f"Saved: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        for i, item in enumerate(items, 1):
            f.write(f"{i}. {item['name']} - {item['score']}%\n")
            f.write(f"Reason: {item['reason']}\n\n")
    return path
