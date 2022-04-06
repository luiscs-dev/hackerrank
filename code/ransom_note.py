#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#
from collections import defaultdict

def checkMagazine(magazine, note):
    # To store available words
    magazine_words = defaultdict(int)    
    
    # Update number of available words
    for word in magazine:
        magazine_words[word] += 1 

    # Check if there are enough words to use    
    for word in note:
        if magazine_words[word] == 0:
            print("No")
            return
        
        magazine_words[word] -= 1
    
    print("Yes")