import re

from src.classes import LongNote, Note, TimingPoint
from src.functions import (
    create_long_note,
    create_note,
    create_timing_point,
    get_timing_changes,
    group_notes_by_timing_changes,
    read_map,
)


def main():
    map_path = "./maps/hazy_moon_night/hazy_test.osu"
    new_map_path = "./maps/hazy_moon_night/hazy_test_convert.osu"

    normal_lines, timing_points, unsorted_notes = read_map(map_path)
    notes = sorted(
        unsorted_notes,
        key = lambda unsorted_notes: (
            unsorted_notes.time,
            unsorted_notes.column
        )
    )

    timing_changes = get_timing_changes(timing_points)
    start_time = timing_changes[0].time

    timing_note_groups = group_notes_by_timing_changes(notes, timing_changes)
    change_index = 0

    for note_group in timing_note_groups:
        print(timing_changes[change_index])
        change_index += 1
        for note in note_group:
            print(note)

    print(start_time)

if __name__ == "__main__":
    main()
