def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di
 
 
tups = [("Utsav",22), ("Krishnam",12), ("Bhavin", 14),
        ("manav",20), ("akhil",25)]
dictionary = {}
print(Convert(tups, dictionary))