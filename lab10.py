def charCount(word,countVowel = 0,count = 0):
    word = word.lower()
    list1 = list(word)
    if list1[countVowel] == "a" or list1[countVowel] == "e" or list1[countVowel] == "i" or list1[countVowel] == "o" or list1[countVowel] == "u":
        count+=1
    countVowel += 1
    if countVowel < len(word):
        charCount(word,countVowel,count)
    else:
        print(f"Number of Vowels in your phrase is: {count} times.")
        return

charCount("I love python")