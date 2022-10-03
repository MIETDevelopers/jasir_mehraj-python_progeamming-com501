#Interchange First and Last Element of a List
list = [100,80,60,40,20,0]
print("List =",list)
temp = list[0]   #by swapping method
list[0] = list[-1]
list[-1] = temp
print("Intechanged list =",list)

#second method
list[0], list[-1] = list[-1], list[0]
print("Intechanged list =",list)