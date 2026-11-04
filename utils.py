def format_profile(profile):
    return [
        ("Name", profile.get("name", "")),
        ("Age", profile.get("age", "")),
        ("Background", profile.get("background", "")),
        ("Interests", profile.get("interests", "")),
        ("Skill Level", profile.get("skill_level", "")),
        ("Preference", profile.get("preference", "")),
        ("Goal", profile.get("goal", "")),
        ("No. of Items", profile.get("num_items", 5)),
    ]
