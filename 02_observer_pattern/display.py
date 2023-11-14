from display_element import DisplayElement
from observer import Observer
from weather_data import WeatherData

class CurrentConditionDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: WeatherData) -> None:
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def display(self):
        print(f"현재 상태: 온도 {self.temperature}F, 습도 {self.humidty}%")
    
    def update(self):
        self.temperature = self.weather_data.get_temperature()
        self.humidty = self.weather_data.get_humidity()
        self.pressure = self.weather_data.get_pressure()
        self.display()
