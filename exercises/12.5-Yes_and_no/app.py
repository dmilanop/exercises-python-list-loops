theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def map_theBools(numb):
    if numb == 1:
        numb = 'wiki'
    elif numb == 0:
        numb = 'woko'
    return numb
    
new_list = list(map(map_theBools, theBools))

print(new_list)