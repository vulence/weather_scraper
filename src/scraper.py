import requests
from bs4 import BeautifulSoup  
from forecast import Forecast

def get_soup(url: str) -> BeautifulSoup:
    headers = {"User-Agent":"Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    response_text = response.text
    return BeautifulSoup(response_text, features='html.parser')

def get_weather2umbrella() -> list:
    forecasts = []
    data = get_soup('https://www.weather2umbrella.com/weather-forecast-belgrade-serbia-en/7-days')
    week_days = data.find("div", attrs={"class": "seven_days_data"}).findNext("div", attrs={"class": "inline_block_fix"}).findAll("a", attrs={"data-id": True})

    for day in week_days:
        day_date = day.findNext("div", attrs={"class": "day_label"}).text.strip()
        temperatures = day.findNext("div", attrs={"class": "day_temperatures"})
        max_temp = int(temperatures.findNext("p", attrs={"class": "day_max"}).text.strip()[:-1])
        min_temp = int(temperatures.findNext("p", attrs={"class": "day_min"}).text.strip()[:-1])
        _, day, month = day_date.split()
        day = day[:-1]
        forecasts.append(Forecast.create_forecast(day, month, min_temp, max_temp))

    return forecasts
        
        
def get_accuweather() -> list:
    forecasts = []
    data = get_soup('https://www.accuweather.com/en/rs/belgrade/298198/daily-weather-forecast/298198')
    week_days = data.find("div", attrs={"class": "page-content content-module"}).findAll("div", attrs={"data-qa": True}, limit=7)

    for day in week_days:
        day_date = day.findNext("h2", attrs={"class": "date"}).text.strip().split("\n")[1]
        temperatures = day.findNext("div", attrs={"class": "temp"})
        max_temp = int(temperatures.findNext("span", attrs={"class": "high"}).text.strip()[:-1])
        min_temp = int(temperatures.findNext("span", attrs={"class": "low"}).text.strip()[1:-1])
        month, day = (int(value) for value in day_date.split("/"))
        forecasts.append(Forecast.create_forecast(day, month, min_temp, max_temp))

    return forecasts