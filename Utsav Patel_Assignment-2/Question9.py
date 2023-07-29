A=int(input("Enter the value of A:"))
B=int(input("Enter the value of B:"))
C=int(input("Enter the value of C:"))

if A==B or B==C or A==C:
    sum=0
else:
    sum=A+B+C

print("The sum of A,B and C is:",sum)