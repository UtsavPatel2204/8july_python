NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input(f"Please enter the Value of Element {i}:"))
    NumList.append(value)

print("The Smallest Element in this List is:", min(NumList))
print("The Largest Element in this List is:", max(NumList))
total=0
for i in range(0, len(NumList)):
    total = total + NumList[i]
 
print("Sum of all elements in given list: ", sum(NumList))