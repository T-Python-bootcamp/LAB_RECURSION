count=0
v=["a","e","i","o","u"]
def vowels(word):
    lowerchar=word[0].lower()
    if  lowerchar in v:
        print(lowerchar)
        global count
        count+=1
    if len(word)>1:
        newWord=word[1 : : ]
        vowels(newWord)
vowels("I love python")
print(count)
        
           
    

