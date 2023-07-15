# Example 3

from functools import reduce


def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    
    def func_add(a, b): 
        return a + b
   
    total = reduce(func_add, numbers)
    
    average = total / len(numbers)
    
    print(f"average: {average:.2f}")


# Call main to start this program.
if __name__ == "__main__":
    main()
