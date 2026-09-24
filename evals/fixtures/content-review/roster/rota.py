from dataclasses import dataclass


@dataclass(frozen=True)
class Slot:
    start: int
    end: int
    owner: str


def owner_at(slots: list[Slot], instant: int) -> str | None:
    ordered = sorted(slots, key=lambda slot: slot.start)
    for index, slot in enumerate(ordered):
        if slot.end <= slot.start:
            raise ValueError("invalid interval")
        if index and slot.start < ordered[index - 1].end:
            raise ValueError("overlapping intervals")
    for slot in ordered:
        if slot.start <= instant < slot.end:
            return slot.owner
    return None
