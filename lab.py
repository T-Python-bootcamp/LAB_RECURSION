def vowelsCounter(word:str, index =0, counter=0)->int:
    vowels = ["a","e","i","o","u"]
    word = word.lower()
    if index < len(word):
        for c in word:
            if c in vowels:
                counter+=1
                index+=1
                vowelsCounter(word, index, counter)
            else:
                index+=1
                vowelsCounter(word, index, counter)
        return counter
    else:
        return
print(vowelsCounter("I love python"))