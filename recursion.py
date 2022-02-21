def vowels (word:str)->int:
    vowels = ["a","e","i","o","u"]
    coun = [x for x in word.lower() if x in vowels]
    return len(coun)

print(vowels ("I love python"))