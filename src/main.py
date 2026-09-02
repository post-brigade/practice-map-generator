import re

from src.functions import generate_note, generate_long_note, generate_chord


def main():
    normal_note_pattern = re.compile(r"\d+,\d+,\d+,1,\d,\d:\d:\d:\d{1,3}:")
    long_note_pattern = re.compile(r"\d+,\d+,\d+,128,\d,\d+,\d:\d:\d:\d{1,3}:")
    timing_point_pattern = re.compile(r"\d+,-?\d+(?:\.\d+)?,\d{1},\d{1},\d,\d{1,3},\d,\d{1,2}")

    with open("./maps/hazy_moon_night/hazy_test.osu") as map:
        with open("./maps/hazy_moon_night/hazy_test_conversion.osu", "w") as new_map:
            note_count = -1
            for line in map:
                line = line.strip()

                if line == "":
                    new_map.write("\n")
                    continue
                match_t = timing_point_pattern.search(line)
                match_n = normal_note_pattern.search(line)
                match_ln = long_note_pattern.search(line)

                if match_n:
                    note = line.split(",")
                    print(note)
                    note_count += 1
                    if note_count % 4 == 0:
                        generate_chord(note)
                        continue
                    generate_note(note)
                elif match_ln:
                    generate_long_note(note)
                elif match_t:
                    new_map.write(f"{line}\n")
                else:
                    new_map.write(f"{line}\n")



if __name__ == "__main__":
    main()
