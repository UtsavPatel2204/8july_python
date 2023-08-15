from collections import Counter
 
my_dict = {'A': 98, 'B': 101, 'C': 120,
           'D': 190, 'E': 105, 'F': 93}
 
k = Counter(my_dict)
 
high = k.most_common(3)
 
print("Initial Dictionary:")
print(my_dict, "\n")
 
print("Dictionary with 3 highest values:")
print("Keys: Values")
 
for i in high:
    print(i[0]," :",i[1]," ")