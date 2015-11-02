#Finding the lorentzian contraction of a meter stick traveling along one dimension
#speed must be a ratio of c
def lorentz(length, speed):
    gamma = 1 / ( (1-(speed**2))**.5 )
    l0 = length / gamma
    return l0

print(lorentz(1, .8))
