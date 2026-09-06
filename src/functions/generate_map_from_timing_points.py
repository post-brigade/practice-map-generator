from src.classes import LongNote, Note, TimingPoint

from .helpers import create_row, rgb_to_console_color


def generate_map_from_timing_window(timing_changes: list[TimingPoint], end_note: Note | LongNote):
