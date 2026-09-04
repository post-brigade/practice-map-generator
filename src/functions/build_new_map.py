from src.classes import LongNote, Note, TimingPoint

from .to_lines import to_lines


def build_new_map(
    normal_lines: list[list[str]],
    timing_points: list[TimingPoint],
    notes: list[Note | LongNote]
) -> str:
    note_point_lines = to_lines(timing_points + notes)
    all_lines = normal_lines + note_point_lines
    sorted_lines = sorted(all_lines, key = lambda line: int(line[-1]))
    joined_lines : list[str] = []

    for line in sorted_lines:
        line.pop()
        joined_lines.append(",".join(line))

    map = "\n".join(joined_lines)


    return map
