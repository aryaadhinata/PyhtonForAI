num1 = int(input("your first number : "))
num2 = int(input("your second number : "))
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
        print("did'nt recognize the operator")