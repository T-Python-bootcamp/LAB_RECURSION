def vowels(word,index=0, count=0):
    v = ["a", "e", "i", "o", "u"]
    word = word.lower()
    if index < len(word) :
        if word[index] in v:
            vowels(word,index+1, count+1)
        else:
            vowels(word,index+1, count)
    else:
        print(f"vowels = {count}")
