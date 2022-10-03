'''Tuple is an ordered sequence of items same as a list.Tuples once created cannot be modified.
It is defined within parentheses ().'''
tuple = (30,'python',12,67,'hello')
print("TUPLE =",tuple)
print(type(tuple))
#prints the element present at index 2
print("Tuple[2] = ", tuple[2])
#prints the element present at 0,1,2
print("Tuple[0:3] = ", tuple[0:3])
#prints the elements starting from index 1
print("Tuple[1:] = ", tuple[1:])
#prints the element at last index
print("Tuple[-1] = ", tuple[-1])
#prints the element from starting index to 3
print("Tuple[:4] = ", tuple[:4])