

def letters ( word:str ) -> int :
    letters = [ "a" , "e" , "i" , "o" , "u" ]

    counter = [any for any in word.lower() if any in letters]
    return len(counter) 

print (letters (" I love python "))  