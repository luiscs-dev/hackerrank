#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    total_letters = len(s)
    
    changes_applied = 0
    
    for i in range(0,total_letters//2):
        difference = ord(s[total_letters - 1 - i]) - ord(s[i])
        
        if difference < 0:
            difference = ord(s[i]) - ord(s[total_letters - 1 - i]) 
        
        changes_applied += difference
        
    return changes_applied
