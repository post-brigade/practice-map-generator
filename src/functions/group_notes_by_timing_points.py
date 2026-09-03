from src.classes import Note, LongNote, TimingPoint

def group_notes_by_timing_changes(
    notes: list[Note | LongNote],
    timing_changes: list[TimingPoint]
) -> list[list[Note | LongNote]]:

    notes_per_change: list[list[Note | LongNote]] = []

    if len(timing_changes) == 1:
        notes_per_change.append(notes)
        return notes_per_change

    for i in range(len(timing_changes) - 1):
        time_start = timing_changes[i].time
        time_end = timing_changes[i + 1].time
        timing_notes: list[Note | LongNote] = []
        for note in notes:
            if (note.time >= time_start
                and note.time < time_end):
                timing_notes.append(note)

        if timing_notes:
            notes_per_change.append(timing_notes)

    return notes_per_change
