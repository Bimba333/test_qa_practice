def classify_weight(kg):
    if kg <= 0:
        return None
    elif kg < 1:
        return "light"
    elif 1 <= kg <= 10:
        return "medium"
    elif kg > 10:
        return "heavy"

    