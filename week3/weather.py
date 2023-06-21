# weather.py
def cels_from_fahr(fahr):

    """Convert a temperature in Fahrenheit to
        Celsius and return the Celsius temperature.
    """
    cels = (fahr - 32) * 5 / 9
    return cels

print(cels_from_fahr(-12))
print(cels_from_fahr(0))
print(cels_from_fahr(12))
