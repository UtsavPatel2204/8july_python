def split(list_a, size):

  for i in range(0, len(list_a), size):
    yield list_a[i:i + size]

size = 3
my_list = [1,2,3,4,5,6,7,8,9]
print(list(split(my_list,size)))