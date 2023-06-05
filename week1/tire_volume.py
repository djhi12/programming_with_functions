from datetime import date

def calculate_volume(width, aspect_ratio, diameter):
    volume = (3.14159 * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return round(volume, 2)

def main():
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    volume = calculate_volume(width, aspect_ratio, diameter)
    print("The approximate volume is", volume, "liters")

    # Append volume data to the file
    with open("volumes.txt", "a") as file:
        today = date.today().strftime("%Y-%m-%d")
        print(f"{today}, {width}, {aspect_ratio}, {diameter}, {volume}\n")

# Call the main function
main()
