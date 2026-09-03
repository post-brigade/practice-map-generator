from src.classes import TimingPoint


def get_timing_changes(timing_points: list[TimingPoint]) -> list[TimingPoint]:
    time_changes: list[TimingPoint] = []
    for timing_point in timing_points:
        if timing_point.uninherited == 1:
            time_changes.append(timing_point)

    return time_changes
