my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

#your code go here:
new_list = []

for x in range(0, len(my_list)):
    if type(my_list[x]) == dict:
        new_list.append(my_list[x])
        print(new_list)
    elif type(my_list[x]) == list: 
        new_list.append(my_list[x])
        print(new_list)
    # print(type(new_list[x]))