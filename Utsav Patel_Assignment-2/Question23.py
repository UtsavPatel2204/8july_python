main_str = input("Enter main string: ")  
mid_str = input("Enter the string to be inserted: ")
position = int(input("Enter the position in which string should be inserted: ")) 
main_str = main_str[:position]+mid_str+main_str[position:] 

print(main_str) 