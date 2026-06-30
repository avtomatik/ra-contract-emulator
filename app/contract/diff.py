def diff_objects(a, b):
    if a == b:
        return None

    return {"expected": a, "actual": b}
