import random


def column_to_x(column: int, key_count: int) -> int:
    if column not in range(1, key_count + 1):
        raise ValueError("Invalid column.")
    x = ((column - 1) * 512 + 256) // key_count

    return x


def create_row(is_barline: bool, key_count: int, barline_color, default_color) -> list[str]:
    column = f"{barline_color}▁▁▁▁▁{default_color}" if is_barline else "     "
    row = [column for _ in range(key_count)]
    return row


def random_column(banned_columns, key_count):
    allowed = [x for x in range(1, key_count + 1) if x not in banned_columns]
    if not allowed:
        raise ValueError("No valid columns")
    return random.choice(allowed)


def rgb_to_console_color(r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m"
