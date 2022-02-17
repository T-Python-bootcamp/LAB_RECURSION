# Solution without recursion
# word = "I love python"
# vowels = ["a", "e", "i", "o", "u"]
# def recursion_func(word):
#     arr = []
#     for char in word:
#         for ch in vowels:
#             if char.lower() == ch:
#                 arr.append(char)
#     print(len(arr))
# recursion_func(word)


# Solution with recursion
def recursion_func(word, count=0):
    if word:
        if word[0].lower() in ("a", "e", "i", "o", "u"):
            count += 1
        return recursion_func(word=word[1:], count=count)
    else:
        return count


print(recursion_func("I love python"))
