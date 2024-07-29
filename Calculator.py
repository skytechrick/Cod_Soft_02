num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error!"
    else:
        return num1 / num2
    
def calculator():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)
    else:
        result = "Invalid choice!"
    
    print("Result:", result)

if _name_ == "_main_":
    calculator()
