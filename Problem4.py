import math

def isPalindrome(testNum):
    strTestNum = str(testNum)
    intTestNum = int(testNum)
    partLength = math.floor(len(strTestNum)/2)
    firstHalf = strTestNum[:int(partLength)]
    if(intTestNum % 2 == 0):
        lastHalf = strTestNum[int(partLength-1):]
    else:
        lastHalf = strTestNum[int(partLength):]
    #reverse string
    lastHalf = lastHalf[::-1]
    if(lastHalf == firstHalf):
        return True
    else:
        return False

def iterateThrough(firstTop, firstBot, secondTop, secondBot):
    maxPalindrome = 0
    for x in range(firstTop, firstBot, -1):
        for y in range(secondTop, secondBot, -1):
            if(isPalindrome(x*y)):
                if((x*y) > maxPalindrome):
                    maxPalindrome = x*y

    print(maxPalindrome)

iterateThrough(99,9,99,9)
iterateThrough(999,99,999,99)
