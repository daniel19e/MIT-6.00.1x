s = 'azcbobobegghakl'
current=''
longest=''
for x in range(len(s)):
    if s[x-1] <= s[x]:
        current+=s[x]
    else:
        current=s[x]
    if len(current) > len(longest):
        longest=current
print("Longest substring in alphabetical order is: " + str(longest))
            
    
