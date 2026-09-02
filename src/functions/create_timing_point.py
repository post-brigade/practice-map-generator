from src.classes import TimingPoint

def create_timing_point(timing_point_list: list[str]) -> TimingPoint:
    time = float(timing_point_list[0])
    beat_length = float(timing_point_list[1])
    meter = int(timing_point_list[2])
    sample_set = int(timing_point_list[3])
    sample_index = int(timing_point_list[4])
    volume = int(timing_point_list[5])
    uninherited = int(timing_point_list[6])
    effects = int(timing_point_list[7])
    line_number = int(timing_point_list[8])

    new_timing_point = TimingPoint(
        time,
        beat_length,
        meter,
        sample_set,
        sample_index,
        volume,
        uninherited,
        effects,
        line_number
    )

    return new_timing_point
