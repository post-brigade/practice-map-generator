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
    key_count = 7
    map_path = "./maps/hazy_moon_night/hazy_test.osu"
    new_map_path = "./maps/hazy_moon_night/hazy_test_output.osu"

    normal_lines, timing_points, notes = read_map(map_path, key_count)
    timing_changes = get_timing_changes(timing_points)
    random_notes = randomize_notes(notes, key_count)
    timing_note_groups = group_notes_by_timing_changes(random_notes, timing_changes)
    notes_with_chords = add_chords(random_notes, key_count)

    generate_note_matrix(notes_with_chords, timing_changes, key_count)

    new_map = build_new_map(normal_lines, timing_points, notes_with_chords)
    write_map(new_map, new_map_path)

if __name__ == "__main__":
    main()
