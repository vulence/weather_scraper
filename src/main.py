from scraper import get_weather2umbrella, get_accuweather
from forecast import Forecast

def main():
    weathers1 = get_weather2umbrella()
    weathers2 = get_accuweather()
    combined = Forecast.combine([weathers1, weathers2])
    for forecast in combined:
        print(forecast)

if __name__ == "__main__":
    main()