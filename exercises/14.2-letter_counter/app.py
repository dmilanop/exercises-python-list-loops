par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
for letra in par.lower().replace(" ",""):
    if letra in counts:
        counts[letra] = counts[letra]+1
    else:
        counts[letra] = 1

print(counts)

