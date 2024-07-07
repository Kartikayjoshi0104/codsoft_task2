# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function to take user input and perform the operation
def calculator():
    print("Welcome to the simple calculator!")
    
    # Taking user input for the numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Taking user input for the operation choice
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice(1/2/3/4): ")
    
    # Performing the calculation based on user choice
    if choice == '1':
        result = add(num1, num2)
        print(f"The result of addition is: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The result of subtraction is: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"The result of multiplication is: {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"The result of division is: {result}")
    else:
        print("Invalid input! Please enter a valid choice.")

# Running the calculator function
if __name__ == "__main__":
    calculator()
