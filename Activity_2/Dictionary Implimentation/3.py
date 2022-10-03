dict = {'pen':20,'copy':100,'pencil':10}  #creation of dictionary
print("Dictionary =",dict)  #printing dictionary
#acessing the values
print("Rate of pen =",dict['pen'])
print("Rate of pencil =",dict['pencil'])
print("Rate of copy =",dict['copy'])
#deleting elements of dictionary
del dict["copy"]
print("Updated Dictionary =",dict)
#delecting the dictionary itself
del dict
print(dict)