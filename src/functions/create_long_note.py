from src.classes import LongNote


def create_long_note(note_list: list[str]) -> LongNote:
    column = int(note_list[0])
    y = int(note_list[1])
    time = int(note_list[2])
    note_type = int(note_list[3])
    hit_sound = int(note_list[4])
    end_time = int(note_list[5])
    hit_sample = note_list[6]
    line_num = str(note_list[7])
    new_note = LongNote(
        column,
        y,
        time,
        note_type,
        hit_sound,
        end_time,
        hit_sample,
        line_num,
    )
    return new_note
