def vowelsCounter(word:str)->int:
    vowels = ["a","e","i","o","u"]
    counter = [x for x in word.lower() if x in vowels]
    return len(counter)

print(vowelsCounter("I love python"))