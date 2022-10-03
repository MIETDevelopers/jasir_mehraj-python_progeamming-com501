#Program to calculate factorial of a number using function

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact

num = int(input("Enter a Number: "))
x = factorial(num)
print(f"Factorial of {num} is {x}")