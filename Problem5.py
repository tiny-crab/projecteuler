#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def isDivisibleBy(target):
    minCheck = 0
    if (target % 2 == 0):
        minCheck = (target/2)
    elif(target % 1 == 0):
        mincheck = (target/2 + 1)
    else:
        return ("not an int")

    start = minCheck * target

    for x in range(start, 1000000000, minCheck):
        for y in range(target, minCheck, -1):
            if (x % y != 0):
                break
            if( (y == minCheck + 1) and (x % y == 0)):
                return(x)
                break


print(isDivisibleBy(10))
print(isDivisibleBy(20))
