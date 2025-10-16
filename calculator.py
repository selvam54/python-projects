def calculatorplay():
    # Loop
    while True:

        # Quit section (currently commented)
        # if num1 == "quit":
        #     break 

        # Calculator function
        def calculator(num1, num2):
            if user == "+":
                return num1 + num2
            elif user == "-":
                return num1 - num2
            elif user == "*":
                return num1 * num2
            elif user == "%":
                return num1 % num2

        # User input
        num1 = int(input("Enter the number: "))
        user = input("Addition + \nSubtraction - \nMultiplication * \nDivide % \nWhat do you choose: ")
        num2 = int(input("Enter the number: "))

        # Print result
        print(f"{num1} {user} {num2} answer is: {calculator(num1, num2)}")

