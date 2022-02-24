from entities import Direction, FacingDirection, Position


class Rover:
    facing: str
    position: Position

    def __init__(self, facing: str, position: Position) -> None:
        self.facing = facing
        self.position = position

    def move(self, direction: Direction):
        if direction == Direction.R:
            if self.facing == FacingDirection.N:
                self.facing = FacingDirection.E
                return
            if self.facing == FacingDirection.E:
                self.facing = FacingDirection.S
                return
            if self.facing == FacingDirection.S:
                self.facing = FacingDirection.W
                return
            if self.facing == FacingDirection.W:
                self.facing = FacingDirection.N
                return
        if direction == Direction.L:
            if self.facing == FacingDirection.N:
                self.facing = FacingDirection.W
                return
            if self.facing == FacingDirection.W:
                self.facing = FacingDirection.S
                return
            if self.facing == FacingDirection.S:
                self.facing = FacingDirection.E
                return
            if self.facing == FacingDirection.E:
                self.facing = FacingDirection.N
                return
        if direction == Direction.F:
            if self.facing == FacingDirection.N:
                self.position.y += 1
                return
            if self.facing == FacingDirection.E:
                self.position.x += 1
                return
            if self.facing == FacingDirection.S:
                self.position.y -= 1
                return
            if self.facing == FacingDirection.W:
                self.position.x -= 1
                return
        if direction == Direction.B:
            if self.facing == FacingDirection.N:
                self.position.y -= 1
                return
            if self.facing == FacingDirection.E:
                self.position.x -= 1
                return
            if self.facing == FacingDirection.S:
                self.position.y += 1
                return
            if self.facing == FacingDirection.W:
                self.position.x += 1
                return
