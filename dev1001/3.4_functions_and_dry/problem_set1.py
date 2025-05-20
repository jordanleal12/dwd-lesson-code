"""Functions for converting temperature"""

celsius_to_fahrenheit = lambda x: x * 9 / 5 + 32

fahrenheit_to_celsius = lambda x: (x - 32) * 5 / 9

def conversion_fn(temperature, degrees_unit, callback_fn):
    """processes and prints conversion"""
    reverse_unit = "C" if degrees_unit == "F" else "F"
    print(f"\n{temperature}°{degrees_unit} is {callback_fn(temperature):.2f}°{reverse_unit}")

while True:
    to_convert = input("Enter temperature to convert as a number then 'C' or 'F', ie. '50C': ")
    temp = to_convert[:-1]
    unit = to_convert[-1]
    try:
        temp = float(temp)
    except ValueError:
        print("\nInvalid input, try again.")
        continue
    if unit.upper() not in ("C", "F"):
        print("\nInvalid input, try again.")
        continue
    unit = unit.upper()
    break

conversion_lambda = celsius_to_fahrenheit if unit =="C" else fahrenheit_to_celsius
conversion_fn(temp, unit, conversion_lambda)
