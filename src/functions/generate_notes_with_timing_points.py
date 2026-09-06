from src.classes import LongNote, Note, TimingPoint

from .generate_note import generate_note
from .map_generation_helpers import column_to_x, create_row, rgb_to_console_color


def generate_notes_with_timing_points(timing_changes: list[TimingPoint], end_note: Note | LongNote, key_count: int):
    sixteenth_tick = timing_changes[0].beat_length / 4
    notes: list[Note] = []
    banned_columns = set()

    for i in range(len(timing_changes)):
        current_time = timing_changes[i].time

        while(
            current_time >= timing_changes[i].time
            and current_time < timing_changes[i + 1].time

            if i < len(timing_changes) - 1 else

            current_time >= timing_changes[i].time
            and current_time <= end_note.time
        ):
            note = generate_note(current_time, 1, key_count, banned_columns)
            banned_columns = {note.column}
            notes.append(note)
            current_time += sixteenth_tick

    return notes
