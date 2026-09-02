import re

def main():

    with open("./maps/hazy_moon_night/hazy_test.osu") as file:
        map = file.read()

    normal_notes = re.findall(r"\d+,\d+,\d+,1,\d,\d:\d:\d:\d{1,3}:", map)
    long_notes = re.findall(r"\d+,\d+,\d+,128,\d,\d+,\d:\d:\d:\d{1,3}:", map)
    timing_points = re.findall(r"\d+,-?\d+(?:\.\d+)?,\d{1},\d{1},\d,\d{1,3},\d,\d{1,2}", map)
    note0 = normal_notes[0].split(",")
    print (note0)

if __name__ == "__main__":
    main()
