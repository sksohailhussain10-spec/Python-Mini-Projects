print("____CALCULATOR____")


n1: int = int(input("Enter First  Number: "))
n2: int = int(input("Enter Second Number: "))
operator = input('''enter operator: +,-,/,%,* : ''')


if operator == "+": #addition
    result = n1 + n2

    print(f"Result : {n1} + {n2} = {round(result, 3)}")
elif operator == "-": #subtraction
    result = n1 - n2
    print(f"Result : {n1} - {n2} = {round(result, 3)}")

elif operator == '*': #multiplication
    result = n1 * n2
    print(f"Result : {n1} * {n2} = {round(result, 3)}")

elif operator == '/': #Divition
    result = n1 / n2
    print(f"Result : {n1} / {n2} = {round(result, 3)}")

else:
    print("invalid input")

