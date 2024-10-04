from speak import Speak

def calculate(num1,num2,operator):
    print(num1)
    print(num2)
    a=int(num1)
    b=int(num2)

    while True:
        if "add" in operator or "addition" in operator or "plus" in operator:

            sum=a+b
            break

        elif "minus" in operator or "subtract" in operator:

            sum=a-b
            break

        elif "multiplication" in operator or "multiply" in operator:

            sum=a*b
            break

        elif "division" in operator or "divide" in operator:

            sum=a/b
            break

        else:

            Speak("Please choose from the list mention")

    return sum

    