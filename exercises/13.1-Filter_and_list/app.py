
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def filter_name(names):
    return names[0].lower() in "r"

resulting_names = list(filter(filter_name, all_names))

print(resulting_names)




