from datetime import date


def calculate_volume(width, aspect_ratio, diameter):
    volume = (3.14159 * width**2 * aspect_ratio *
              (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return round(volume, 2)


def main():
    num_entries = int(input("\nEnter the number of tire measurements you want to enter: "))

    with open("volumes.txt", "a") as file:
        
        for _ in range(num_entries):
            width = int(input("\nEnter the width of the tire in mm (ex 205): "))
            aspect_ratio = int(
                input("Enter the aspect ratio of the tire (ex 60): "))
            diameter = int(
                input("Enter the diameter of the wheel in inches (ex 15): "))

            volume = calculate_volume(width, aspect_ratio, diameter)
            print("\nThe approximate volume is", volume, "liters")

            today = date.today().strftime("%Y-%m-%d")
            data = f"{today}, {width}, {aspect_ratio}, {diameter}, {volume}\n"
            file.write(data)
            print(data)


# Call the main function
main()

"""
In this updated version, the user is prompted to enter the number of tire measurements they want to enter. The code then enters a loop that runs num_entries times. Inside the loop, the user is prompted for the width, aspect ratio, and diameter of each tire. The volume is calculated, displayed, and then appended to the "volumes.txt" file along with the date. Each set of data is written on a new line in the file.
"""
