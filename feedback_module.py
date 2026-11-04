def refine_recommendations(items, feedback):
    feedback_lower = feedback.lower()
    if not feedback_lower.strip():
        return items
    excluded = []
    if "no web" in feedback_lower or "don't want web" in feedback_lower or "do not want web" in feedback_lower:
        excluded.append("web")
    if "more beginner" in feedback_lower:
        items = [x for x in items if "fundamental" in x["name"].lower() or "python" in x["name"].lower()] + items
    return [x for x in items if not any(term in x["name"].lower() for term in excluded)]
