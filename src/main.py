import re

from src.classes import LongNote, Note, TimingPoint
from src.functions import create_long_note, create_note, create_timing_point, read_map


def main():
    map_path = "./maps/hazy_moon_night/hazy_test.osu"
    new_map_path = "./maps/hazy_moon_night/hazy_test_convert.osu"

    normal_lines, timing_points, long_notes, notes = read_map(map_path)

    print(timing_points)


if __name__ == "__main__":
    main()
