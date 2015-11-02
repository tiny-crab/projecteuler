def sumOfSquares(target):
    total = 0
    for x in range(1, target+1, 1):
        total += (x**2)

    return(total)

def squareOfSums(target):
    total = 0
    for x in range(1,target+1,1):
        total += x

    return(total**2)

def differenceBetween(target):
    return(squareOfSums(target) - sumOfSquares(target))

print(differenceBetween(100))
