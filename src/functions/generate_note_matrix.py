from src.classes import LongNote, Note


def rgb_to_console_color(r: int, g: int, b: int) -> str:
    return f"\033[38;2;{r};{g};{b}m"


def generate_note_matrix(notes: list[Note | LongNote], key_count: int = 7):
    if not notes:
        return


    def create_row(is_barline: bool) -> list[str]:
        column = f"{GRAY}▁▁▁▁▁{RESET}" if is_barline else "     "
        row = [column for _ in range(key_count)]
        return row

    GRAY = rgb_to_console_color(100,100,100)
    NEON_BLUE = rgb_to_console_color(0, 200, 255)
    RESET = "\033[0m"

    time_index = 0
    is_barline = time_index % 8 == 0
    note_matrix = [create_row(is_barline)]
    note = " ▆▆▆ "
    note_tail = "▃▃▃"
    barline_note = f"{GRAY}▁{RESET}▆▆▆{GRAY}▁{RESET}"

    for i in range(len(notes)):
        current_note = notes[i]
        note_matrix[time_index][current_note.column - 1] = barline_note if is_barline else note

        if i < len(notes) - 1 and current_note.time != notes[i + 1].time:
            time_index += 1
            is_barline = time_index % 8 == 0
            note_matrix.append(create_row(is_barline))

    for i in range (len(note_matrix) - 1, -1, -1):
        print("".join(note_matrix[i]))
        print()
