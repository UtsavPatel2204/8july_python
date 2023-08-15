def unique_list(l):
  num = []
  for a in l:
    if a not in num:
      num.append(a)
  return num

print('unique elements are')
print(unique_list([1,2,3,4,5,3,5,6,7,9,17,10,12,7]))