def emptylist(list1):
    if len(list1) == 0:
        return 0
    else:
        return 1
 
list1 = []
if emptylist(list1):
    print("The list is not empty")
else:
    print("Empty List")