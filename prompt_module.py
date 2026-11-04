import json

def build_prompt(profile, analysis, count, feedback=""):
    return f"""You are a personalized learning recommendation assistant.
User profile: {json.dumps(profile)}
Preference analysis: {json.dumps(analysis)}
Feedback: {feedback or "None"}
Recommend exactly {count} suitable learning topics/resources.
Return valid JSON: an array of objects with name, reason, score (0-100).
Rank highest suitability first. Be realistic and explain each recommendation briefly.
"""
