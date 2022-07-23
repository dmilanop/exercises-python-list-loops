my_list = [ 1, 0, 0, 0, 1, 0, 0, 0, 1, 1 ]

def my_function(numbers):
    new_list = []
    for index, numb in enumerate(numbers):
        if numb == 1: 
            new_list.append(numb)
            print(new_list)
        elif numb == 0:
            new_list.append(numb)
            new_list[index] = 'Yahoo'
            print(new_list)
        
    return new_list
print(my_function(my_list))


