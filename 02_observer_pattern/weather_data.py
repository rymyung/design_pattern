from observer import Observer
from subject import Subject

class WeatherData(Subject):

    def __init__(self) -> None:
        self.observers = []

    
    def register_observer(self, observer: Observer):
        self.observers.append(observer)
    
    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            # observer.update(self.temperature, self.humidity, self.pressure) # push
            observer.update() # pull
    
    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.notify_observers()

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure
