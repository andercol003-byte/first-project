# Mini Project: Simple Calculator

print("Welcome to the mini calculator!")

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "undefined"

# Show results
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Division:", div_result)
