# Example 1

# The main() function is defined. This is the entry point of the program.
def main():
    
    # The fahr_temps list is initialized with a set of Fahrenheit temperatures.
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # The Fahrenheit temperatures are printed using the print() function.
    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    # An empty list cels_temps is created to store the Celsius temperatures.
    cels_temps = []
    
    # A for loop is used to iterate over each Fahrenheit temperature in fahr_temps.
    for fahr in fahr_temps:
        
        # Inside the loop, the cels_from_fahr() function is called to convert the Fahrenheit temperature to Celsius.
        cels = cels_from_fahr(fahr)
        
        # The converted Celsius temperature is appended to the cels_temps list using the append() method.
        cels_temps.append(cels)

    # Print the Celsius temperatures.
    # After the loop, the Celsius temperatures are printed using the print() function.
    print(f"Celsius: {cels_temps}")


def cels_from_fahr(fahr):
    """Convert a Fahrenheit temperature to
    Celsius and return the Celsius temperature.
    """
    # The cels_from_fahr(fahr) function is defined. It takes a Fahrenheit temperature as an argument and converts it to Celsius using the formula (fahr - 32) * 5 / 9. The result is rounded to one decimal place using the round() function.
    cels = (fahr - 32) * 5 / 9
    return round(cels, 1)


# Call main to start this program.
if __name__ == "__main__":
    
    # Finally, the main() function is called to start the program.
    main()
    
