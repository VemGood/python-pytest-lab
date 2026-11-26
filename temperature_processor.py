
class TemperatureProcessor:
    def __init__(self, min_temp, max_temp):
        """
        Ініціалізує процесор з цільовим діапазоном температур.
        """
        if min_temp >= max_temp:
            raise ValueError(
                "Мінімальна температура має бути меншою за максимальну."
            )

        self.min_temp = min_temp
        self.max_temp = max_temp

    def process_sensor_data(self, raw_data):
        """
        Приймає та перевіряє дані з датчика.
        """
        if not isinstance(raw_data, (int, float)):
            raise TypeError("Дані з датчика повинні бути числом.")

        if raw_data < -273.15:
            raise ValueError(
                "Температура не може бути нижчою за абсолютний нуль."
            )

        if raw_data > 1000:
            raise ValueError(
                "Апаратна помилка: датчик не підтримує вимірювання понад 1000°C."
            )

        return float(raw_data)

    def get_relay_status(self, current_temp):
        """
        Визначає стан реле кліматичної системи.
        """
        if current_temp < self.min_temp:
            return "HEATING"
        elif current_temp > self.max_temp:
            return "COOLING"
        else:
            return "IDLE"

    def celsius_to_fahrenheit(self, celsius):
        """
        Конвертує градуси Цельсія у Фаренгейти.
        """
        return (celsius * 9 / 5) + 32