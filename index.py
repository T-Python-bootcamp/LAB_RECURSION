count=0
def vowels(word):
    lowerchar=word[0].lower()
    if  lowerchar=="a" or lowerchar=="e" or lowerchar=="i" or lowerchar=="o" or lowerchar=="u":
        global count
        count+=1
    if len(word)>1:
        newWord=word.replace(word[0], '')
        vowels(newWord)
vowels("I love python")
print(count)
        
           
    

