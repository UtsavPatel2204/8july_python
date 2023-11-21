try:
    num=int(input("Enter the number:"))

    if num%2==0:
        raise ValueError("Invalid number")
    
    print("The number is odd")

except ValueError as var:
    print(var)
