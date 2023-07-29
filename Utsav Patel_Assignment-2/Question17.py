mystr1=input("Enter the value of first string:")
mystr2=input("Enter the value of second string:")

x=mystr1[0:2]

mystr1=mystr1.replace(mystr1[0:2],mystr2[0:2])

mystr2=mystr2.replace(mystr2[0:2],x)

print("First string after swapping is:",mystr1)
print("Second string after swapping is:",mystr2)

print("Both combined strings after swapping is:",mystr1,"",mystr2)



