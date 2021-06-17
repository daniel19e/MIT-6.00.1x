def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    if aStr== '':
        return False
    if len(aStr) == 1:
        return aStr == char
    midIndex=len(aStr)//2
    midChar=aStr[len(aStr)//2]    
    if midChar == char:
        return True
    elif midChar>char:
        return isIn(char, aStr[:midIndex])
    else:
        return isIn(char, aStr[midIndex+1:])