import json, os, re
from prompt_module import build_prompt

def _fallback(profile, count, feedback=""):
    interests = profile.get("interests", "Python, Artificial Intelligence")
    goal = profile.get("goal", "learn AI")
    level = profile.get("skill_level", "Beginner")
    topics = [
        ("Python for AI Projects", "Builds practical Python skills through small AI applications.", 96),
        ("Machine Learning with Scikit-Learn", "Introduces beginner-friendly ML projects using real datasets.", 94),
        ("Data Cleaning and Visualization for AI", "Develops essential data preparation skills using Pandas and Matplotlib.", 89),
        ("AI Portfolio Project (Predictive Model)", "Creates an end-to-end project that can demonstrate job-ready skills.", 98),
        ("AI Job Search Strategy", "Explains portfolios, applications and interview preparation for AI roles.", 92),
        ("Statistics for Machine Learning", "Builds the mathematical foundation needed to understand ML models.", 87),
        ("Deep Learning Fundamentals", "Introduces neural networks after the core ML foundations.", 85),
        ("Generative AI Applications", "Explores practical uses of modern generative AI tools and models.", 90),
    ]
    excluded = []
    fb = feedback.lower()
    if "no web" in fb or "don't want web" in fb or "do not want web" in fb:
        excluded.append("web")
    filtered = [t for t in topics if not any(x in t[0].lower() for x in excluded)]
    result = []
    for name, reason, score in filtered[:count]:
        result.append({
            "name": name,
            "reason": f"{reason} This matches your interest in {interests} and goal to {goal}, at a {level.lower()} level.",
            "score": score
        })
    return sorted(result, key=lambda x: x["score"], reverse=True)

def generate_recommendations(profile, analysis, count=5, feedback=""):
    key = os.getenv("OPENAI_API_KEY")
    if key:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=key)
            prompt = build_prompt(profile, analysis, count, feedback)
            response = client.chat.completions.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4o"),
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5
            )
            raw = response.choices[0].message.content
            match = re.search(r"\[.*\]", raw, re.S)
            if match:
                items = json.loads(match.group(0))
                items = sorted(items, key=lambda x: float(x.get("score", 0)), reverse=True)
                return items[:count]
        except Exception:
            pass
    return _fallback(profile, count, feedback)
