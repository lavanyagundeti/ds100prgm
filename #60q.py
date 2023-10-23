#60q

def is_palindrome(s):
    
    s = ''.join(c for c in s if c.isalpha()).lower()
    
    
    return s == s[::-1]


text = "A man, a plan, a canal, Panama"


if is_palindrome(text):
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
