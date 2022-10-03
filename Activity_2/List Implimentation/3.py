#Program to Merge Two Lists
listA = [1,3,5,7,9]
listB = [2,4,6,8,10]
print("List A =",listA)
print("List B =",listB)
listC = listA + listB  #using + operator
print("LIST C =",listC)

#using extend method
listA.extend(listB)
print("List =",listA)