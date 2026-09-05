import copy

from src.classes import LongNote, Note

from .column_to_x import column_to_x
from .random_column import random_column


def create_chord_note(note: Note | LongNote, banned_columns: set[int]) -> Note | LongNote:
    new_note = copy.copy(note)
    new_note.column = random_column(1, 7, banned_columns)
    new_note.x = column_to_x(note.column)

    return new_note
