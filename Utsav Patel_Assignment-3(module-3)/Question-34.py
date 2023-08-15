d = {'id':101,"name":"Utsav","Address":"Ahmedabad","Subject":"python"}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary.')
  else:
      print('Key is not present in the dictionary.')
is_key_present("id")
is_key_present("pincode")
is_key_present("Subject")