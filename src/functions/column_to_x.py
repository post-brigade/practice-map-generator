


def column_to_x(column: int, key_count: int) -> int:
    if column not in range(1, key_count + 1):
        raise ValueError("Invalid column.")
    x = ((column - 1) * 512 + 256) // key_count

    return x
