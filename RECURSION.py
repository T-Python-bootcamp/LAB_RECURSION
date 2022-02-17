# def myFunc(num:int =20):
#     print(num)
#     if num == 1:
#         return
#     myFunc(num-1)

# myFunc(num=50)

###


def vowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']
    
def countVovels(str, n):
    if (n == 1):
        return vowel(str[n - 1])
 
    return (countVovels(str, n - 1) + vowel(str[n - 1]))
 
print(countVovels("I love python",len("I love python")))
