#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

import math

#function to actually return the largest prime factor
def findFactors(targetNum):
    #don't need to iterate higher than this
    foundMaxFactor = False
    maxDivisor = int(targetNum**.5)+1
    maxFactor = 0
    #iterating through all numbers between 0 and target/2
    for x in range(2, maxDivisor, 1):
        #if the iterator is now on a prime number,
        if(isPrime(x)):
            #and if the target is divisible by that prime number,
            #it's a prime factor!
            if(targetNum % x == 0):
                #print("A prime factor is: " + str(x))
                #print("The target was: " + str(targetNum))
                #print("The new target is: " + str(targetNum/x))
                #if the target div by factor is a prime, that means it's the largest prime factor
                if(isPrime(targetNum/x)):
                    print("The highest prime factor is: " + str(targetNum/x))
                    foundMaxFactor = True
                    break
                else:
                    findFactors(targetNum/x)
                return foundMaxFactor



#checking if a number is prime
def isPrime(checkNum):
    #if the number is two,
    if (checkNum == 2):
        #it's prime!
        return True

    else:
        #getting square root of num
        sqrRoot = int(checkNum**.5)+1
        #finding out if the number is prime only takes
        for x in range (2, sqrRoot, 1):
            if(checkNum % x == 0):
                return False
        return True

findFactors(13195)
findFactors(600851475143)
