def is_palindrome(s):
    t=s[::-1]
    if s==t:
        return "Palindrome"
    else :
        return "Not palindrome"
print(is_palindrome("AbbA"))    
