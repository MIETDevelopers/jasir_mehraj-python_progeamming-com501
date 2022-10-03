list = [10,30,50,70,90]     # creation of list
print("List =",list)     #printing a list
list[0] = 20   #updating list[0] from 10 to 20
print("List =",list)
list.append(100)   #adds 100 to the last of list
print("List =",list) 
list.insert(3,40)   #adds 40 to the 3rd index of list
print("List =",list)
list.reverse()   #prints the reversed list
print("List =",list)
list.sort()   #prints the list in sorted order
print("List =",list)
list.count(40)   #counts how many 40 are present in list
print(list.count(40))
list.index(90)   #prints the index of 90
print(list.index(90))
list.pop(4)   #pop out the elemnet at 4th index
print(list.pop(4))
print("List =",list)
list.remove(50)   #removes the 50 from the list
print("List =",list)
print("Length of list =",len(list)) #prints the length of list
print(30 in list)   #prints true if 30 is present in list