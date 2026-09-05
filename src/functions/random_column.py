import random


def random_column(start, stop, banned_columns):
    allowed = [x for x in range(start, stop + 1) if x not in banned_columns]
    if not allowed:
        raise ValueError("No valid columns")
    return random.choice(allowed)
