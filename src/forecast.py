from typing import Self
from sys import stderr
from datetime import datetime
from math import floor
from statistics import mean

class Forecast:
    OUTPUT_DATE_FORMAT = "%d. %B %Y."

    def __init__(self, date: datetime, min_temp: int, max_temp: int) -> None:
        self.date = date
        self.min_temp = min_temp
        self.max_temp = max_temp
    
    @classmethod
    def create_forecast(cls, day: int, month: int | str, min_temp: int | str, max_temp: int | str) -> Self:
        date = Forecast.get_full_date(day, month)
        min_temp = Forecast.cast_temp_to_int(min_temp) if not isinstance(min_temp, int) else min_temp
        max_temp = Forecast.cast_temp_to_int(max_temp) if not isinstance(max_temp, int) else max_temp

        if None in (min_temp, max_temp):
            invalid_temp = min_temp if min_temp is None else max_temp
            stderr.write(f"The value ({invalid_temp}) is not valid as a temperature. Will omit the value entirely.")
        
        if isinstance(min_temp, int) and isinstance(max_temp, int) and min_temp > max_temp:
            raise ValueError(f"Invalid temperature range: min temperature ({min_temp}) is higher that max temperature ({max_temp})")
        
        return cls(date, min_temp, max_temp)
    
    @staticmethod
    def combine(forecasts: list) -> list:
        combined_forecasts = []
        zipped_forecasts = zip(*forecasts)

        for day_forecasts in zipped_forecasts:
            date, *rest = day_forecasts[0].date, *zip(*[(forecast.min_temp, forecast.max_temp) for forecast in day_forecasts])
            min_temp = floor(mean(rest[0]))
            max_temp = floor(mean(rest[1]))
            combined_forecasts.append(Forecast(date, min_temp, max_temp))

        return combined_forecasts



    @staticmethod
    def cast_temp_to_int(value) -> int | None:
        try:
            return int(value)
        except ValueError:
            return None
        
    # Receives days as a number and months either as a number or a full-length month string
    @staticmethod
    def get_full_date(day: int, month: int | str) -> datetime:
        year = datetime.now().year

        if isinstance(month, int):
            date = datetime.strptime(f"{day}/{month}/{year}", "%d/%m/%Y")
        elif isinstance(month, str):
            date = datetime.strptime(f"{day}/{month}/{year}", "%d/%B/%Y")
        else:
            raise TypeError(f"The arguments are invalid.")

        return date
    
    def format_date(self) -> str:
        if self.date:
            return self.date.strftime(self.OUTPUT_DATE_FORMAT)
        else:
            return "Invalid date"

        
    def __str__(self) -> str:
        return f"{self.format_date()}\nMax temprature: {self.max_temp}, min temperature: {self.min_temp}"