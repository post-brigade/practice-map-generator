import random


def random_column(banned_columns, key_count):
    allowed = [x for x in range(1, key_count + 1) if x not in banned_columns]
    if not allowed:
        raise ValueError("No valid columns")
    return random.choice(allowed)
