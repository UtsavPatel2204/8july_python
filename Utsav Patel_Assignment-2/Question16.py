mystr="Hello! my name is Utsav and I am an IT engineer and I am currently learning python programming."
word=input(("Enter a word:"))
a=[]
count=0
a=mystr.split(" ")
for i in range(1,len(a)):
    if word==a[i]:
        count+=1
    
print("Count of the word is:",count)
