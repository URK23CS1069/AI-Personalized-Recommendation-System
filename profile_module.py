def analyze_profile(profile):
    interests = [x.strip() for x in profile.get("interests", "").split(",") if x.strip()]
    return {
        "primary_interest": interests[0] if interests else "General technology",
        "secondary_interest": interests[1] if len(interests) > 1 else "Not specified",
        "skill_level": profile.get("skill_level", "Beginner"),
        "goal": profile.get("goal", "Build new skills"),
        "preference": profile.get("preference", "Practical learning"),
        "constraints": "Keep recommendations appropriate to the stated skill level."
    }
