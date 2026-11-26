import pytest
from temperature_processor import TemperatureProcessor
def test_basic_functionality():
    processor = TemperatureProcessor(min_temp=10, max_temp=30)
    result = processor.process_sensor_data(25)
    assert result == 25.0
    assert isinstance(result, float)
def test_invalid_type_raises_error():
    processor = TemperatureProcessor(min_temp=10, max_temp=30)
    with pytest.raises(TypeError):
        processor.process_sensor_data("двадцять")
def test_invalid_value_raises_error():
    processor = TemperatureProcessor(min_temp=10, max_temp=30)
    with pytest.raises(ValueError):
        processor.process_sensor_data(-300)
@pytest.mark.parametrize("input_value, expected_result", [
    (0, 32),
    (100, 212),
    (-40, -40)
])
def test_with_parametrize(input_value, expected_result):
    processor = TemperatureProcessor(min_temp=10, max_temp=30)
    result = processor.celsius_to_fahrenheit(input_value)
    assert result == expected_result
@pytest.fixture
def ready_object():
    """Фікстура"""
    return TemperatureProcessor(min_temp=15, max_temp=25)
def test_scenario_1_with_fixture(ready_object):
    result = ready_object.get_relay_status(10)
    assert result == "HEATING"
def test_scenario_2_with_fixture(ready_object):
    result = ready_object.get_relay_status(30)
    assert result == "COOLING"
def test_scenario_3_with_fixture(ready_object):
    result = ready_object.get_relay_status(20)
    assert result == "IDLE"
    pass