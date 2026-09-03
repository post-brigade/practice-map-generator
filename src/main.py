import re

from src.classes import LongNote, Note, TimingPoint
from src.functions import create_long_note, create_note, create_timing_point, read_map, get_timing_changes


def main():
    map_path = "./maps/hazy_moon_night/hazy_test.osu"
    new_map_path = "./maps/hazy_moon_night/hazy_test_convert.osu"

    normal_lines, timing_points, notes = read_map(map_path)

    timing_changes = get_timing_changes(timing_points)
    start_time = timing_changes[0].time

    print(start_time)

if __name__ == "__main__":
    main()
