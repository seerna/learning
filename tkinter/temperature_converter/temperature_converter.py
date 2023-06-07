# temperature_converter.py

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    return round(celsius, 2)

def celsius_to_fahrenheit(celsius):
    fahrenheit = (9 / 5) * float(celsius) + 32
    return round(fahrenheit, 2)