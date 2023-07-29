mystr=input("Enter a String:")
if len(mystr) > 2:
    mystr=mystr[0:2] + mystr[-2:]
    print("The first and last two characters of given string is:",mystr)
else:
    print(mystr)


