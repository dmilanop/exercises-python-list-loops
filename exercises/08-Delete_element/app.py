people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    new_list_people = []
    for x in range(len(people)):
        if people[x] != person_name:
            new_list_people.append(people[x])
            
    return new_list_people
    #     if x == person_name:
    #         x.pop()
    # return x
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))