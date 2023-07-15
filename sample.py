
# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
sum_result = num1 + num2
print(f"Sum: {num1} + {num2} = {sum_result}")

# Subtraction
diff_result = num1 - num2
print(f"Difference: {num1} - {num2} = {diff_result}")

# Multiplication
prod_result = num1 * num2
print(f"Product: {num1} * {num2} = {prod_result}")

# Division
if num2 != 0:
    div_result = num1 / num2
    print(f"Division: {num1} / {num2} = {div_result}")
else:
    print("Cannot divide by zero.")
