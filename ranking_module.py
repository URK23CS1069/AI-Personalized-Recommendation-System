def rank_recommendations(items):
    return sorted(items, key=lambda item: float(item.get("score", 0)), reverse=True)
