# Python program to calculate length of a String without using len() function

# when string is declared before 
string = "Welcome To The World Of PYTHON"
count = 0   #initialzing count to 0
for i in string:
    count = count + 1 #increment count by 1
print("The Length of given string is",count)


# when user inputs the string of his/her own choice
print("Enter the String : ")
string = input() #using input function to take user's string
count = 0   #initialzing count to 0
for i in string:
    count = count + 1 #increment count by 1
print("The Length of given string is",count)