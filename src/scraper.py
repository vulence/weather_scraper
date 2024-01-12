import requests
from bs4 import BeautifulSoup  

def get_soup(url: str) -> BeautifulSoup:
    headers = {"User-Agent":"Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    response_text = response.text
    return BeautifulSoup(response_text, features='html.parser')

def get_weather2umbrella() -> None:
    data = get_soup('https://www.weather2umbrella.com/weather-forecast-belgrade-serbia-en/7-days')
    week_days = data.find("div", attrs={"class": "seven_days_data"}).findNext("div", attrs={"class": "inline_block_fix"}).findAll("a", attrs={"data-id": True})

    for day in week_days:
        day_date = day.findNext("div", attrs={"class": "day_label"}).text.strip()
        temperatures = day.findNext("div", attrs={"class": "day_temperatures"})
        max_temp = temperatures.findNext("p", attrs={"class": "day_max"}).text.strip()
        min_temp = temperatures.findNext("p", attrs={"class": "day_min"}).text.strip()
        print(day_date)
        print(f"Max temp: {max_temp}, min temp: {min_temp}")
        
def get_accuweather() -> None:
    data = get_soup('https://www.accuweather.com/en/rs/belgrade/298198/daily-weather-forecast/298198')
    week_days = data.find("div", attrs={"class": "page-content content-module"}).findAll("div", attrs={"data-qa": True}, limit=7)

    for day in week_days:
        day_date = day.findNext("h2", attrs={"class": "date"}).text.strip()
        temperatures = day.findNext("div", attrs={"class": "temp"})
        max_temp = temperatures.findNext("span", attrs={"class": "high"}).text.strip()
        min_temp = temperatures.findNext("span", attrs={"class": "low"}).text.strip()[1:]
        print(day_date)
        print(f"Max temp: {max_temp}, min temp: {min_temp}")