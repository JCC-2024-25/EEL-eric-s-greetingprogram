while True:
    number1 = float(input("Enter the first number: "))
    equation = input("Enter the equation (+,/,-,*):")
    number2 = float(input("Enter the second number: "))
    ready = input("Press enter to get the answer: ")
    ready = "="
    if equation == "+" and ready == "=":
       print(f"The answer is {number1 + number2}")
    if equation == "-" and ready == "=":
       print(f"The answer is {number1 - number2}")
    if equation == "/" and ready == "=":
       print(f"The answer is {number1 / number2}")
    if equation == "*" and ready == "=":
       print(f"The answer is {number1 * number2}")
    repeat = input("Do you want to do another calculation? (y/n):")
    if repeat.lower() == "n":
        print("Goodbye!")
        break