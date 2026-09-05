import re

from src.classes import LongNote, Note, TimingPoint
from src.functions import (
    add_chords,
    build_new_map,
    create_long_note,
    create_note,
    create_timing_point,
    generate_note_matrix,
    get_timing_changes,
    group_notes_by_timing_changes,
    randomize_notes,
    read_map,
    to_lines,
    write_map,
)


def main():
    map_path = "./maps/hazy_moon_night/hazy_moon_night_7k.osu"
    new_map_path = "./maps/hazy_moon_night/hazy_moon_night_7k_conversion.osu"

    normal_lines, timing_points, notes = read_map(map_path)
    random_notes = randomize_notes(notes)
    notes_with_chords = add_chords(random_notes)
    generate_note_matrix(notes_with_chords)

    # will probably need later
    # timing_changes = get_timing_changes(timing_points)
    # timing_note_groups = group_notes_by_timing_changes(random_notes, timing_changes)

    new_map = build_new_map(normal_lines, timing_points, notes_with_chords)

    write_map(new_map, new_map_path)

if __name__ == "__main__":
    main()
