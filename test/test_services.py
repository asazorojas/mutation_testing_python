from services import ClockService

clock_Service = ClockService()

def test_twelve_and_zer0():
    assert clock_Service.between(12, 0) == 0

def test_three_and_zero():
    assert clock_Service.between(3, 0) == 90

def test_six_and_zero():
    assert clock_Service.between(6, 0) == 180

def test_nine_and_zero():
    assert clock_Service.between(9, 0) == 270

def test_one_and_thirty():
    assert clock_Service.between(1, 30) == 135

def test_two_and_thirty():
    assert clock_Service.between(2, 30) == 105

def test_two_and_fourty():
    assert clock_Service.between(2, 40) == 160

def test_five_and_fourty_five():
    assert clock_Service.between(5, 45) == 98

def test_six_and_fifty_five():
    assert clock_Service.between(6, 55) == 123