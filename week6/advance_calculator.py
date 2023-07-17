import math


def display_menu():
    print("Advanced Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Trigonometric Functions")
    print("8. Quit")


def get_user_choice():
    try:
        choice = int(input("Enter your choice (1-8): "))
        if 1 <= choice <= 8:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
            return get_user_choice()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_choice()


def add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Result:", num1 + num2)


def subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Result:", num1 - num2)


def multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Result:", num1 * num2)


def divide():
    num1 = float(input("Enter the dividend: "))
    num2 = float(input("Enter the divisor: "))
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print("Result:", num1 / num2)


def exponentiate():
    num1 = float(input("Enter the base: "))
    num2 = float(input("Enter the exponent: "))
    print("Result:", num1 ** num2)


def square_root():
    num = float(input("Enter the number: "))
    if num < 0:
        print("Invalid input. Cannot calculate the square root of a negative number.")
    else:
        print("Result:", math.sqrt(num))


def trigonometric_functions():
    print("Trigonometric Functions:")
    print("1. Sine")
    print("2. Cosine")
    print("3. Tangent")
    choice = get_user_choice()
    angle = float(input("Enter the angle in degrees: "))
    if choice == 1:
        print("Result:", math.sin(math.radians(angle)))
    elif choice == 2:
        print("Result:", math.cos(math.radians(angle)))
    elif choice == 3:
        print("Result:", math.tan(math.radians(angle)))


def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            add()
        elif choice == 2:
            subtract()
        elif choice == 3:
            multiply()
        elif choice == 4:
            divide()
        elif choice == 5:
            exponentiate()
        elif choice == 6:
            square_root()
        elif choice == 7:
            trigonometric_functions()
        else:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
