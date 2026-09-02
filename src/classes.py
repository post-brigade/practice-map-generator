from enum import enum


class TimingPoint:
    def __init__(
        time: float,
        beat_length: float,
        meter: int,
        sample_set: int = 0,
        sample_index: int = 0,
        volume: int = 0,
        uninherited: int,
        effects: int
    ):
        self.time = time
        self.beat_length = beat_length
        self.meter = meter
        self.sample_set = sample_set
        self.volume = volume
        self.uninherited = uninherited
        self.effects = effects


class NoteType(Enum):
    NOTE = 1
    LONG_NOTE = 128


class Note:
    def __init__(
        x: int,
        y: int = 192,
        time: int,
        type: NoteType,
        hitsound: list[int] = [0, 0, 0, 0],
    ):
        self.x = x
        self.y = y
        self.time = time
        self.type = type
        self.hitsound = hitsound


class LongNote:
    def __init__(
        x: int,
        y: int = 192,
        time: int,
        type: NoteType,
        hitsound: list[int] = [0, 0, 0, 0],
        end_time: int
    ):
        super().__init__(x, y, time, type, hitsound)
        self.end_time = end_time
