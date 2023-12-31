from display import CurrentConditionDisplay
from weather_data import WeatherData


if __name__ == "__main__":
    weather_data = WeatherData()
    current_condition_display = CurrentConditionDisplay(weather_data=weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)
