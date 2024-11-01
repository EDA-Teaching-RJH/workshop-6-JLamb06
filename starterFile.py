#Your code goes here. 
import math
def main():
    a = float(input("Enter a number: "))
    b = float(input("Enter a second number: "))
    safe_divide(a,b)
    input_list = []
    process_list(input_list)

def safe_divide(a, b):
    try:
        solution = a/b
        print(solution)
    except ZeroDivisionError:
        print("Cannot Divide by zero")




def process_list(input_list):
    total = 0
    x = 0
    for x  in range(5): 
        number = float(input("Enter a number: "))
        input_list.append(number)
        print(input_list)
        try:
            answer = int(input_list[x])**2
            total += answer
        except TypeError or ValueError:
            print("That is not a valid number")
    print(total)
    

def nested_operations(a, b):
    print("")

def process_input():
    print("")


main()
