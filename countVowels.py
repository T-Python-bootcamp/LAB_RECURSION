def countVowels(word,countVowel = 0,count = 0):
    word = word.lower()
    li = list(word)
    if li[countVowel] == "a" or li[countVowel] == "e" or li[countVowel] == "i" or li[countVowel] == "o" or li[countVowel] == "u":
        count+=1
    countVowel += 1
    if countVowel < len(word):
        countVowels(word,countVowel,count)
    else:
        print(f"Number of Vowels is: {count}")
        

countVowels("I love python")