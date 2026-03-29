# Multiply function
def multiply(a, b):
    return a * b

# Divide function (handle divide by zero)
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


# Test the functions
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))