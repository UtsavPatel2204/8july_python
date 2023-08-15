l = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
print (d)