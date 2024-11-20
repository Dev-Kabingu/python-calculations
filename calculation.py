
number1 = float(input("Enter the number1: "))
number2 = float(input("Enter the number2: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if second_number != 0:
        result = number1 / number2
    else:
        result = "Cannot divide by zero."
else:
    result = "Invalid operation"

print(f"Your input was: {number1} {operation} {number2}")
print(f"The answer is: {result}")



number1 = float (input("Enter the number1 :"))
number2 = float (input("Enter the number2 :"))
operation = input("Enter the operation to apply :")

