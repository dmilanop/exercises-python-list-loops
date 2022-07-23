arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sumOdds(odd_numbers):
    aux = 0

    for x in range(len(arr)):
        if arr[x] % 2 != 0:
            aux += arr[x]
    return aux 

print(sumOdds(arr))

