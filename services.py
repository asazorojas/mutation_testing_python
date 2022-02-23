from typing import Union


class ClockService:
    def __hours_hand(self, hour: int, minutes: int) -> float:
        base = (hour % 12) * (360 // 12)
        correction = int((minutes / 60) * (360 // 12))
        return base + correction

    def __minutes_hand(self, minutes: int) -> int:
        return minutes * (360 // 60)

    def between(self, hour: int, minutes: int) -> Union[float, int]:
        return abs(self.__hours_hand(hour, minutes) - self.__minutes_hand(minutes))
