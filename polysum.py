import math
def polysum(n,s): 
    # this function takes the number and length of the sides
    # it returns the sum of the area and square of the perimeter    
    sum = (0.25*n*s**2)/math.tan(math.pi/n)+(n*s)**2
    return round(sum,4) # the sum is rounded to 4 decimal places
