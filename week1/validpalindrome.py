s =  "A man, a plan, a canal: Panama"

def palindrome(s):
        word1 = ""
        word2 = ""
        s = s.lower()

        abc = "qwertyuiopasdfghjklzxcvbnm" # this is valid
        for letter in s:
            if letter in abc:
                word1 += letter
        for letter in reversed(s):
            if letter in abc:
                word2 += letter
        return word1 == word2

palindrome(s)