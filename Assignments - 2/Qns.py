"""
    1. Write code to count down numbers from n to 1 using a while
    2. Write a program that achieves the same as Q(1) i.e. a recursive method that counts down numbers from n to 2
    3. Write a python program that uses a while loop to count down numbers within a range. The user should be asked to input the start and end
    4. Write a python program that achieves the same as Q(3) but using recursion.
    5. Write a recursive function taking 2 integers as input and returns their product using repeated addition, without using multiplication operator.
    6. Write a recursive function that takes a string as an input and returns a reversed copy of the string using only concatenation
    7. Write a recursive function that determines whether a given number n is a prime number by checking for divisibility by integers less than n

    NOTE : Uncomment out the function calls to execute each function
    NOTE : For 4,5 and 6 ensure to uncomment the input calls for full functionality.
"""

# -> 1
def countdown(start = 1) -> None:
    while start >= 1:
        print(start)
        start -= 1

# countdown(10)

# -> 2
def countdownrecursive(start = 1) -> int:
    print(start)

    if start == 1:
        return 1
    else:
        return countdownrecursive(start - 1)
    
# countdownrecursive(10)

# -> 3
def countdowninput() -> None:
    start = int(input("Enter starting number:"))
    end = int(input("Enter end number:"))

    if start == end:
        while start == end:
            end = int(input("Try entering a bigger number: "))

    while start <= end:
        print(start)
        start += 1

# countdowninput()

# -> 4
# start = int(input("Enter starting number:"))
# end = int(input("Enter end number:"))

def countdowninputrecursive(start = 1,end = 1) -> int:
    print(start)

    if start == end:
        return start
    else:
        return countdowninputrecursive(start + 1,end)

# countdowninputrecursive(start,end)

# -> 5

# start2 = int(input("Enter an multipliying number: "))
# result2 = int(input("Enter a multiplying times: "))

def additionMultiplier(multiplicand,result):
    if multiplicand == 0 or result == 0:
        return 0
    if result == 1:
        return multiplicand
    
    return multiplicand + additionMultiplier(multiplicand,result - 1)

# print("Multiplication result:",additionMultiplier(start2,result2))

# -> 6

# string = str(input("Enter a string to reverse: "))

def reversal_string_recursion(string:str,position = 0):
    if position == 0 or len(string) == 0:
        return ""
    else:
        print(string[position - 1],end="")
    return reversal_string_recursion(string,position - 1)
        
    
# print(string)
# reversal_string_recursion(string,len(string))

# -> 7

def primeChecker(number:int,checker = 2):
    if number == 1 or number == 0:
        return False
    else:
        if checker == number:
            return True
        elif number % checker == 0:
            return False
        else:
            return primeChecker(number,checker + 1)

# print(primeChecker(6))