#8.1
def divide_numbers(num1, num2):
    try:
        result=num1 / num2
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
numerator=10
denominator=0
result = divide_numbers(numerator, denominator)
print(f"The result of division is: {result}")


#8.2
def get_number(prompt):
    while True:
        try:
            num=float(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")
number = get_number("Enter a number: ")
print(f"You entered: {number}")


#8.3
def divide_numbers(num1,num2):
    try:
        result = num1/num2
        print(f"The result of division is:{result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Execution of the try-except block is complete.")
numerator=10
denominator=0
divide_numbers(numerator,denominator)
