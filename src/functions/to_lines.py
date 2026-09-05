from src.classes import LongNote, Note, TimingPoint


def note_to_line(note: Note) -> list [str]:
    x = str(note.x)
    y = str(note.y)
    time = str(round(note.time))
    type = str(note.type)
    hit_sound = str(note.hit_sound)
    hit_sample = note.hit_sample

    note_line = [
        x, y, time, type, hit_sound, hit_sample
    ]
    return note_line


def long_note_to_line(note: LongNote) -> list [str]:
    x = str(note.x)
    y = str(note.y)
    time = str(round(note.time))
    type = str(note.type)
    hit_sound = str(note.hit_sound)
    end_time = str(note.end_time)
    hit_sample = note.hit_sample

    note_line = [
        x, y, time, type, hit_sound, end_time, hit_sample
    ]
    return note_line


def timing_point_to_line(timing_point: TimingPoint) -> list[str]:
    time = str(timing_point.time)
    beat_length = str(timing_point.beat_length)
    meter = str(timing_point.meter)
    sample_set = str(timing_point.sample_set)
    sample_index = str(timing_point.sample_index)
    volume = str(timing_point.volume)
    uninherited = str(timing_point.uninherited)
    effects = str(timing_point.effects)

    timing_point_line = [
        time, beat_length, meter, sample_set, sample_index, volume, uninherited, effects
    ]
    return timing_point_line


def to_lines(notes_points: list[Note | LongNote] | list[TimingPoint]):
    line_list: list[list[str]] = []

    for note_or_point in notes_points:

        match note_or_point:
            case LongNote():
                long_note_line = long_note_to_line(note_or_point)
                line_list.append(long_note_line)

            case Note():
                note_line = note_to_line(note_or_point)
                line_list.append(note_line)

            case TimingPoint():
                timing_point_line = timing_point_to_line(note_or_point)
                line_list.append(timing_point_line)

            case _:
                raise TypeError("Invalid type: not Note or TimingPoint")

    return line_list
