from src.classes import LongNote, Note

from .column_to_x import column_to_x
from .create_chord_note import create_chord_note
from .create_note import create_note
from .random_column import random_column


def add_chords(notes: list[Note | LongNote]) -> list[Note | LongNote]:
    notes_with_chords:list[Note | LongNote] = []
    banned_columns: set[int] = set()

    for i in range(len(notes)):
        notes_with_chords.append(notes[i])
        banned_columns = {notes[i].column}

        if i > 0:
            banned_columns.add(notes[i - 1].column)

        if i < len(notes) - 1:
            banned_columns.add(notes[i + 1].column)

        if i % 8 == 0:
            chord:list[Note | LongNote] = []

            note_1 = create_chord_note(notes[i], banned_columns)
            banned_columns.add(note_1.column)
            chord.append(note_1)

            note_2 = create_chord_note(notes[i], banned_columns)
            banned_columns.add(note_2.column)
            chord.append(note_2)

            note_3 = create_chord_note(notes[i], banned_columns)
            banned_columns.add(note_3.column)
            chord.append(note_3)

            sorted_chord = sorted(chord, key = lambda note: note.column)

            notes_with_chords.extend(sorted_chord)
            continue

        if i % 4 == 0:
            small_chord:list[Note | LongNote] = []

            note_1 = create_chord_note(notes[i], banned_columns)
            banned_columns.add(note_1.column)
            small_chord.append(note_1)

            note_2 = create_chord_note(notes[i], banned_columns)
            banned_columns.add(note_2.column)
            small_chord.append(note_2)

            sorted_chord = sorted(small_chord, key = lambda note: note.column)

            notes_with_chords.extend(sorted_chord)
            continue

        if i % 2 == 0:
            smaller_chord:list[Note | LongNote] = []

            note_1 = create_chord_note(notes[i], banned_columns)
            banned_columns.add(note_1.column)
            smaller_chord.append(note_1)

            sorted_chord = sorted(smaller_chord, key = lambda note: note.column)

            notes_with_chords.extend(sorted_chord)
            continue

    return notes_with_chords
