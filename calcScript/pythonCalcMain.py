num1 = float(input("your first number : "))
num2 = float(input("your second number : "))
operator = input("operator (+, -, /, *) : ")

match operator:
    case '+':
        print(f"result : {num1 + num2}")
    case '-':
        print(f"result : {num1 - num2}")
    case '/':
        if(num2 == 0):
            print("can't divide by zero")
        else:
            print(f"result : {num1 / num2}")
    case '*':
        print(f"result : {num1 * num2}")
    case _:
        print("didn't recognize the operator")