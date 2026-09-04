from src.classes import Note


def create_note(note_list: list[str]) -> Note:
    column = int(note_list[0])
    y = int(note_list[1])
    time = int(note_list[2])
    note_type = int(note_list[3])
    hit_sound = int(note_list[4])
    hit_sample = note_list[5]

    new_note = Note(
        column,
        y,
        time,
        note_type,
        hit_sound,
        hit_sample,
    )
    return new_note
