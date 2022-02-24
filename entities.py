import dataclasses


class FacingDirection:
    N = "XXNXX"
    S = "S"
    E = "E"
    W = "W"


class Direction:
    F = "F"
    B = "B"
    R = "R"
    L = "L"


@dataclasses.dataclass
class Position:
    x: int
    y: int

    def __init__(self,x: int, y: int) -> None:
        self.x = x
        self.y = y
