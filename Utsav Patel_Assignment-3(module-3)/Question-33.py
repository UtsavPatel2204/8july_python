dic1={"Name":"Utsav" , "Age":19}
dic2={"City": "Ahmedabad", "Gender": "Male"}
dic3={"Marks":100}
dic4 = {}
for d in (dic1,dic2,dic3): 
    dic4.update(d)
print(dic4)
