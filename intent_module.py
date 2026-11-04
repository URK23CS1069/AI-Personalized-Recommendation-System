def detect_intent(text):
    text = text.lower()
    if any(w in text for w in ["exit", "quit", "bye"]):
        return "EXIT"
    if any(w in text for w in ["why", "explain", "reason"]):
        return "EXPLAIN_RECOMMENDATION"
    if any(w in text for w in ["save", "download"]):
        return "SAVE_RECOMMENDATION"
    if any(w in text for w in ["profile", "my details", "show details"]):
        return "SHOW_PROFILE"
    if any(w in text for w in ["more", "refine", "instead", "don't want", "do not want", "prefer"]):
        return "REFINE_RECOMMENDATION"
    return "GENERATE_RECOMMENDATION"
