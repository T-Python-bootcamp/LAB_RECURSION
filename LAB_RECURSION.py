def Vowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']
 
def countVowels(str):
    count = 0
    for i in range(len(str)):
 
     
        if Vowel(str[i]):
            count += 1
    return count
str = 'I love javaScript'
 

print(countVowels(str))
 
