from entities import Direction, FacingDirection, Position
from rover import Rover


def test_rover_facing_north_at_origin_ends_up_pointing_north_at_zero_three():
    rover = Rover(
        facing=FacingDirection.N,
        position=Position(0, 0)
    )

    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)

    assert rover.facing == FacingDirection.N
    assert rover.position == Position(0, 3)


def test_rover_facing_north_at_origin_ends_up_pointing_west_at_origin():
    rover = Rover(
        facing=FacingDirection.N,
        position=Position(0, 0)
    )

    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.R)

    assert rover.facing == FacingDirection.W
    assert rover.position == Position(0, 0)


def test_rover_facing_north_at_origin_ends_up_pointing_east_at_origin():
    rover = Rover(
        facing=FacingDirection.N,
        position=Position(0, 0)
    )

    rover.move(Direction.L)
    rover.move(Direction.L)
    rover.move(Direction.L)

    assert rover.facing == FacingDirection.E
    assert rover.position == Position(0, 0)


def test_rover_facing_north_at_origin_ends_up_pointing_west():
    rover = Rover(
        facing=FacingDirection.N,
        position=Position(0, 0)
    )

    rover.move(Direction.L)
    rover.move(Direction.L)
    rover.move(Direction.L)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)

    assert rover.facing == FacingDirection.W
    assert rover.position == Position(-1, 0)


def test_rover_facing_north_at_origin_ends_up_pointing_south():
    rover = Rover(
        facing=FacingDirection.N,
        position=Position(0, 0)
    )

    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)

    assert rover.facing == FacingDirection.S
    assert rover.position == Position(0, -7)


def test_rover_facing_north_at_5_5_ends_up_pointing_south_at_5_3():
    rover = Rover(
        facing=FacingDirection.N,
        position=Position(5, 5)
    )

    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)

    assert rover.facing == FacingDirection.S
    assert rover.position == Position(5, 3)


def test_rover_facing_north_at_5_minuts_5_ends_up_pointing_west_at_2_minus_4():
    rover = Rover(
        facing=FacingDirection.N,
        position=Position(5, -5)
    )

    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)

    assert rover.facing == FacingDirection.W
    assert rover.position == Position(2, -4)


def test_rover_facing_north_at_origin_ends_up_pointing_north_at_0_minus_14():
    rover = Rover(
        facing=FacingDirection.S,
        position=Position(0, 0)
    )

    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.R)
    rover.move(Direction.R)

    assert rover.facing == FacingDirection.N
    assert rover.position == Position(0, -14)


def test_rover_facing_west_at_20_0_ends_up_pointing_north_at_8_minus_5():
    rover = Rover(
        facing=FacingDirection.W,
        position=Position(20, 0)
    )

    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.R)
    rover.move(Direction.L)
    rover.move(Direction.L)
    rover.move(Direction.L)
    rover.move(Direction.L)
    rover.move(Direction.L)
    rover.move(Direction.L)
    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.B)
    rover.move(Direction.B)
    rover.move(Direction.B)
    rover.move(Direction.B)
    rover.move(Direction.B)
    rover.move(Direction.B)
    rover.move(Direction.F)

    assert rover.facing == FacingDirection.N
    assert rover.position == Position(8, -5)


def test_rover_facing_east_at_20_100_ends_up_pointing_north_at_32_95():
    rover = Rover(
        facing=FacingDirection.E,
        position=Position(20, 100)
    )

    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.F)
    rover.move(Direction.R)
    rover.move(Direction.L)
    rover.move(Direction.L)
    rover.move(Direction.L)
    rover.move(Direction.L)
    rover.move(Direction.L)
    rover.move(Direction.L)
    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.R)
    rover.move(Direction.B)
    rover.move(Direction.B)
    rover.move(Direction.B)
    rover.move(Direction.B)
    rover.move(Direction.B)
    rover.move(Direction.B)
    rover.move(Direction.F)

    assert rover.facing == FacingDirection.N
    assert rover.position == Position(32, 95)


def test_facing_south_at_100_minus_100_ends_up_pointing_north_at_101_minus_100():
    rover = Rover(
        facing=FacingDirection.S,
        position=Position(100, -100)
    )

    for d in range(100):
        rover.move(Direction.F)
    rover.move(Direction.L)
    for d in range(100):
        rover.move(Direction.F)
    rover.move(Direction.L)
    for d in range(100):
        rover.move(Direction.F)
    rover.move(Direction.L)
    for d in range(100):
        rover.move(Direction.F)
    rover.move(Direction.B)
    rover.move(Direction.L)
    rover.move(Direction.L)
    rover.move(Direction.L)

    assert rover.facing == FacingDirection.N
    assert rover.position == Position(101, -100)


def test_square_starting_at_origin_facing_east():
    rover = Rover(
        facing=FacingDirection.E,
        position=Position(0, 0)
    )

    for times in range(4):
        for d in range(100):
            rover.move(Direction.F)
        rover.move(Direction.L)
    rover.move(Direction.B)
    for times in range(3):
        for d in range(200):
            rover.move(Direction.F)

    assert rover.facing == FacingDirection.E
    assert rover.position == Position(599, 0)

