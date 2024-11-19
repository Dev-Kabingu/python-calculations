
number1 = float (input("Enter the first number :"))
number2 = float (input("Enter the second number :"))
operation = input("Enter the operation to apply :")

# convert the user choosen operation to upper case
operation = operation.upper()
if operation == "addition":
    answer = number1 + number2
    symbol = "+"
elif operation == "divide":
    if number2 == 0:
        answer = "Cannot divide by zero")
        else:
            answer = number1 / number2
            symbol = "/"
elif operation == "subtraction":
    answer = number1 - number2
    symbol = "-"
elif operation == "multiplication":
    answer = number1 * number2
    symbol = "*"
else:
    answer = "operation not valid"
    symbol = ""
print("{number1} {symbol} {number2} =" answer)
   

            
        
