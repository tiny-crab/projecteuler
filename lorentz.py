#Finding the lorentzian contraction of a meter stick traveling along one dimension
#speed must be a ratio of c
#l0 represents proper length (measured length in rest frame)
def lorentz(l0, speed):
    gamma = 1 / ( (1-(speed**2))**.5 )
    length = l0 / gamma
    return length

print(lorentz(1, .9))
