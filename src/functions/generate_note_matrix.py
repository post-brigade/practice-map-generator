from src.classes import LongNote, Note


def create_row(is_barline: bool) -> list[str]:
    column = "▁▁▁▁▁" if is_barline else "     "
    row = [column for _ in range]



def generate_note_matrix(notes: list[Note | LongNote], key_count: int = 7):
    if not notes:
        return


    def create_row(is_barline: bool) -> list[str]:
        column = "▁▁▁▁▁" if is_barline else "     "
        row = [column for _ in range(key_count)]
        return row


    time_index = 0
    is_barline = time_index % 8 == 0
    note_matrix = [create_row(is_barline)]

    for i in range(len(notes)):
        current_note = notes[i]
        note_matrix[time_index][current_note.column - 1] = " ▆▆▆ "

        if i < len(notes) - 1 and current_note.time != notes[i + 1].time:
            time_index += 1
            is_barline = time_index % 8 == 0
            note_matrix.append(create_row(is_barline))

    for i in range (len(note_matrix) - 1, -1, -1):
        print("".join(note_matrix[i]))
        print()
