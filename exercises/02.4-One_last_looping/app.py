names = ['Ruth'+'Pedro','Steven','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Pepe']

#Your code here:
# del names[1]
# names.insert(1, "Steven")
# del names[10]
# names.insert(10, "Pepe")
# del names[0]
# names.insert(0, "Ruth"+"Pedro")

for i in range(len(names)-1, -1, -1):
    print(names[i])
