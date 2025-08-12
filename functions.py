num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def add():
    sum_result = num1 + num2
    return sum_result

def multiply():
    product_result = num1 * num2
    return product_result

def divide():
    if num2 == 0 or num1 == 0:
        return "Error: Division by zero is not allowed."
    quotient_result = num1 / num2
    return quotient_result

print(f"Sum for numbers {num1} and {num2}: {add()}")
print(f"Product for numbers {num1} and {num2}: {multiply()}")
print(f"Quotient for numbers {num1} and {num2}: {divide()}")
print("-----------------")