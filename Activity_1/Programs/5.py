#Python program to print the even numbers from a given list
list = [1,2,3,4,5,6]
print("LIST =",list)
for num in list:
    if num % 2 == 0: # checks if any number present in liat divisible by 2 or not
        print(num)