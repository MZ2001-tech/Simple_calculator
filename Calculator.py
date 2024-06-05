
def main():




    num1 =int(input("enter your first number: ").capitalize())
    num2 = int(input("enter your second number: ").capitalize())



    calculate = calculatator(num1,num2)

    print(calculate)


def calculatator(num1,num2):

    operation = input("Please choose the following operation: +, -, *, / : ")

    if operation == "+":
       NUM = num1 + num2
       result = (f"the total sum of the numbers are: {NUM}").capitalize()
    elif operation == "-":
        NUM = num1 - num2
        result= (f"The subtraction of the numbers are{NUM}").capitalize()
    elif operation == "*":
        NUM = num1 * num2
        result = (f"The multiplication of the numbers are{NUM}").capitalize()
    elif operation == "/":
        if num2 != 0:
         NUM = num1 / num2
         result = f"The devision of the numbers are{NUM}".capitalize()
        else:
         result =f"Division by 0 is not operational".capitalize()
    else:
       result = f"please enter a vaild operation".capitalize()
    
    return result


if __name__ == '__main__':
 main()



