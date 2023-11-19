import msvcrt  # Importing Windows-specific library for keyboard input

def calculator():
    while True:  # Infinite loop until user presses the escape key
        x = float(input("Enter 1st value: "))
        operator = input("Please select operator (+, -, *, /): ")
        y = float(input("Enter 2nd Value: "))

        if operator == '+':
            result = x + y
        elif operator == '-':
            result = x - y
        elif operator == '*':
            result = x * y
        elif operator == '/':
            if y != 0:
                result = x / y
            else:
                print('Error: Division by zero')
                return None
        else:
            print('Invalid input')

        print("Result:", result)
        print("Press ESC to exit or any other key to continue...")
        
        # Check if ESC key is pressed to exit the loop
        if msvcrt.kbhit() and ord(msvcrt.getch()) == 27:  # 27 is the ASCII code for ESC
            break  # Break out of the while loop if ESC key is pressed

    return result

result = calculator()
if result is not None:
    print("Final Result:", result)
