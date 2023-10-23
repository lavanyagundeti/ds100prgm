#62


sentence = "The quick brown fox jumped over the lazy dog"


words = sentence.split()


longest_word = ""


for word in words:
    
    cleaned_word = ''.join(e for e in word
