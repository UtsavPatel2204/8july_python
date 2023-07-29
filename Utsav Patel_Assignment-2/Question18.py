mystr=input("Enter a string:")

if len(mystr)>2:
    if mystr[-3:]=="ing":
      mystr+="ly"
    else:
      mystr+="ing"

print(mystr)