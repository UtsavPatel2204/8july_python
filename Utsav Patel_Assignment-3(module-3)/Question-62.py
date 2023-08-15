pi=22/7
height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))
volume = pi * radian * radian * height  
sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)
print("Volume of cylinder is: ", volume)
print("Surface Area of cylinder is: ", sur_area)