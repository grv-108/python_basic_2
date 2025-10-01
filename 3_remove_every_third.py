# 3. Remove Every Third

# Write a Python program that removes and prints every third number from a list of numbers until the list is empty.

def remove_every_third(num_list):

    position = 2
    idx = 0
    
    len_list = len(num_list)
    
    while len_list > 0:
        idx = (position + idx) % len_list
        print(num_list.pop(idx))
        len_list -= 1
        
my_list = list(range(10,101,10))
print(my_list)

remove_every_third(my_list)


