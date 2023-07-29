mystr=input("Enter a string:")
if len(mystr) % 4 == 0:
    print(''.join(reversed(mystr)))
else:
    print(mystr)