import random

from src.classes import LongNote, Note, TimingPoint

from .column_to_x import column_to_x


def random_except(start, stop, excluded):
    allowed = [n for n in range(start, stop + 1) if n not in excluded]
    if not allowed:
        raise ValueError("No allowed values")
    return random.choice(allowed)


def randomize_notes(notes: list[Note | LongNote]) -> list[Note | LongNote]:
    notes_no_chords: list[Note | LongNote] = []

    for i in range(len(notes)):
        current_note = notes[i]
        if i < len(notes) - 1 and current_note.time == notes[i + 1].time:
            continue

        notes_no_chords.append(current_note)

    random_notes: list[Note | LongNote] = []

    for i in range(len(notes_no_chords)):
        banned_columns: set[int] = set()
        current_note = notes_no_chords[i]
        banned_columns.add(notes_no_chords[i - 1].column)

        if i > 0:
            banned_columns.add(notes_no_chords[i - 1].column)

        current_note.column = random_except(1, 7, banned_columns)
        current_note.x = column_to_x(current_note.column)
        random_notes.append(current_note)

    return random_notes
