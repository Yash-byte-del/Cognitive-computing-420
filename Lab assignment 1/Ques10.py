#10.1
import sys
try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(num1 * num2)
except IndexError:
    print("Error: Provide two numbers as command-line arguments.")
except ValueError:
    print("Error: Ensure both inputs are numbers.")


#10.2
string = sys.argv[1]
print(len(string))
