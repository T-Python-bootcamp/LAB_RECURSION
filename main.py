vowels = ['a','e','i','o','u']

def vowels_count (word:str="")->int:

    if not len(word):
        return 0
    
    temp = list(word)

    if temp.pop().lower() in vowels:
        temp = "".join(temp)
        return vowels_count(temp)+1
    else:
        temp = "".join(temp)
        return vowels_count(temp)

print(vowels_count('I love python'))