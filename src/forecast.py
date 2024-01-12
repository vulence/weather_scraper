from typing import Self
from sys import stderr

class Forecast:
    def __init__(self, day: str, min_temp: int, max_temp: int) -> None:
        self.day = day
        self.min_temp = min_temp
        self.max_temp = max_temp
    
    @classmethod
    def create_forecast(cls, day: str, min_temp: int | str, max_temp: int | str) -> Self:
        if isinstance(min_temp, str):
            min_temp = Forecast.cast_temp_to_int(min_temp)
            if min_temp is None:
                stderr.write(f"The value ({min_temp}) is not valid as a temperature. Will omit the value entirely.")

        if isinstance(max_temp, str):
            max_temp = Forecast.cast_temp_to_int(max_temp)
            if max_temp is None:
                stderr.write(f"The value ({min_temp}) is not valid as a temperature. Will omit the value entirely.")
        
        if isinstance(min_temp, int) and isinstance(max_temp, int) and min_temp > max_temp:
            raise ValueError(f"Invalid temperature range: min temperature ({min_temp}) is higher that max temperature ({max_temp})")
        
        return cls(day, min_temp, max_temp)


    @staticmethod
    def cast_temp_to_int(value) -> int | None:
        try:
            return int(value)
        except ValueError:
            return None
        
    def __str__(self) -> str:
        return f"{self.day}: Max temprature: {self.max_temp}, min temperature: {self.min_temp}"