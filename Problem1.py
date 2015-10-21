def multiples(max):
    sum = 0
    for x in range(0, max, 1):
        if(x % 3 == 0 or x % 5 == 0):
            sum += x
    return sum

print(multiples(10))
print(multiples(100))
print(multiples(1000))

#Any syntax used in this was new for me :)
#I really like Python's style when writing for loops, really easy!
