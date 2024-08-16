def calculator():
    keep_calculating = True
    output = None  # Initialize output to handle the first calculation

    while keep_calculating:
        if output is None:
            first_num = float(input("What's the first number?: "))
        else:
            first_num = output
        
        print("+\n-\n*\n/\n")
        operation = input("Pick an operation: ")

        if operation in "+-*/":
            next_num = float(input("What's the next number?: "))

            # Perform the operation
            if operation == "+":
                output = first_num + next_num
            elif operation == "-":
                output = first_num - next_num
            elif operation == "*":
                output = first_num * next_num
            elif operation == "/":
                if next_num != 0:  # Check for division by zero
                    output = first_num / next_num
                else:
                    print("Error: Division by zero is not allowed.")
                    output = None
                    continue
        else:
            print("Invalid operation. Please pick a valid operation.")
            continue
        
        print(f"{first_num} {operation} {next_num} = {output}")
        
        response = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")

        if response.lower() == "n":
            keep_calculating = False
        elif response.lower() != "y":
            print("Invalid input. Exiting.")
            keep_calculating = False

# Start the calculator
calculator()

            

    


        
    



