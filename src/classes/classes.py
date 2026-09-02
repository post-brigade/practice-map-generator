from typing import override

from .enums import SevenKeyColumn, NoteType


class TimingPoint:
    def __init__(self,
        time: float,
        beat_length: float,
        meter: int,
        sample_set: int,
        sample_index: int,
        volume: int,
        uninherited: int,
        effects: int,
        line_number: int
    ):
        self.time = time
        self.beat_length = beat_length
        self.meter = meter
        self.sample_set = sample_set
        self.sample_index = sample_index
        self.volume = volume
        self.uninherited = uninherited
        self.effects = effects
        self.bpm: float = 1 / beat_length * 1000 * 60

    @override
    def __repr__(self):
        if self.uninherited == 1:
                return f"timing point: time:{round(self.time)} bpm: {round(self.bpm, 2)} meter: {self.meter} beat length: {round(self.beat_length)}"
        else:
            return f"timing point: time:{round(self.time)} meter: {self.meter}"


class Note:
    def __init__(self,
        column: int,
        y: int,
        time: int,
        type: int,
        hit_sound: int,
        hit_sample: str,
        line_number: int
    ):
        self.column = column
        self.y = y
        self.time = time
        self.type = type
        self.hit_sound = hit_sound

    @override
    def __repr__(self):
        return f"normal note: column:{self.column} time: {self.time}"


class LongNote(Note):
    def __init__(self,
        x: int,
        y: int,
        time: int,
        type: int,
        hit_sound: int,
        end_time: int,
        hit_sample: str,
        line_number: int
    ):
        super().__init__(x, y, time, type, hit_sound, hit_sample, line_number)
        self.end_time = end_time

    @override
    def __repr__(self):
        return f"long note: column:{self.column} time: {self.time} end time: {self.end_time}"


class chord:
    def __init__(self, time: int, notes: list[Note | LongNote]):
        self.time = time
        self.notes = notes
