def convertTuple(tup):
        
    str = ''
    for item in tup:
        str = str + item
    return str
 
tuple = ('U','t','s','a','v')
str = convertTuple(tuple)
print(str)