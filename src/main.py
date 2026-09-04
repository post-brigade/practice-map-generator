import re

from src.classes import LongNote, Note, TimingPoint
from src.functions import (
    build_new_map,
    create_long_note,
    create_note,
    create_timing_point,
    generate_note_matrix,
    get_timing_changes,
    group_notes_by_timing_changes,
    read_map,
    to_lines,
    write_map,
)


def main():
    map_path = "./maps/hazy_moon_night/hazy_test.osu"
    new_map_path = "./maps/hazy_moon_night/hazy_test_output.osu"

    normal_lines, timing_points, notes = read_map(map_path)

    generate_note_matrix(notes)

    timing_changes = get_timing_changes(timing_points)
    start_time = timing_changes[0].time

    timing_note_groups = group_notes_by_timing_changes(notes, timing_changes)

    new_map = build_new_map(normal_lines, timing_points, notes)

    write_map(new_map, new_map_path)

if __name__ == "__main__":
    main()
