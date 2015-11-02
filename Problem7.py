#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10,001st prime number?

#first argument is the nth prime number (2 is first, 3 is second, etc.)
def findPrime(target):

    segment = 100
    iterationArray = []
    for x in range(0, segment, 1):
        iterationArray[x] = true

    for x in range(0, segment, 1):
        if(iterationArray[x] == false):
            continue
        if()
