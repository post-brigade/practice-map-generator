from .enums import 7kColumn, NoteType


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
        self.bpm = 1 / meter * 1000 * 60


class Note:
    def __init__(
        x: int,
        y: int = 192,
        time: int,
        type: NoteType,
        hitsound: str = "0:0:0:0:",
    ):
        self.x = x
        self.y = y
        self.time = time
        self.type = type
        self.hitsound = hitsound


class LongNote(Note):
    def __init__(
        x: int,
        y: int = 192,
        time: int,
        type: NoteType,
        hitsound: str = "0:0:0:0:",
        end_time: int
    ):
        super().__init__(x, y, time, type, hitsound)
        self.end_time = end_time
