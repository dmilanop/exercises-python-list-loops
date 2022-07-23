chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    new_list = []
    for x in range(len(list1)):
        new_list.append(list1[x])
    for x in range(len(list2)):
        new_list.append(list2[x])
    return new_list

print(merge_list(chunk_one, chunk_two))
