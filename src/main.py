from scraper import get_weather2umbrella, get_accuweather, get_yrno
from forecast import Forecast

def main():
    forecasts = [get_weather2umbrella(), get_accuweather(), get_yrno()]
    combined = Forecast.combine(forecasts)
    for forecast in combined:
        print(forecast)

if __name__ == "__main__":
    main()