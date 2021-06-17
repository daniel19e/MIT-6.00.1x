bobCount=0
s = 'abob'
for x in range(len(s)):
    if s[x:x+3] == "bob":
        bobCount+=1
print('Number of times bob occurs is: ' + str(bobCount))
    
    

        