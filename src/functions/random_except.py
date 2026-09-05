import random


def random_except(start, stop, excluded):
    allowed = [n for n in range(start, stop + 1) if n not in excluded]
    if not allowed:
        raise ValueError("No allowed values")
    return random.choice(allowed)
