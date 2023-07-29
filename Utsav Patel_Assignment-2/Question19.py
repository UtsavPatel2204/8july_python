mystr=input("Enter a String:")
snot = mystr.find('not')
spoor = mystr.find('poor')
  
if spoor > snot and snot>0 and spoor>0:
    mystr = mystr.replace(mystr[snot:(spoor+4)], 'good')
    print(mystr)
else:
   print(mystr)

# Enter these value in string to check the output: Python is poor or Python is not that poor.