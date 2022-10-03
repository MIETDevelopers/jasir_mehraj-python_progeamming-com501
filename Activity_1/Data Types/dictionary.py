'''Dictionary is an unordered collection of key-value pairs.dictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type.'''

d = {} # empty dictionary
print("DICTIONARY =",d)
print(type)
# int key, string value
numNames={1:"One", 2: "Two", 3:"Three"} 
print("DICTIONARY =",numNames)
print(type(numNames))

# float key, string value
decNames={1.5:"One and Half", 2.5: "Two and Half", 3.5:"Three and Half"}
print("DICTIONARY =",decNames)
# tuple key, string value
items={("Parker","Reynolds","Camlin"):"pen", ("LG","Whirlpool","Samsung"): "Refrigerator"} 
print("DICTIONARY =",items)
romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5} # string key, int value
print("DICTIONARY =",romanNums)