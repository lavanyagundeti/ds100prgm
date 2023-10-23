#61q


sentence = "The quick brown fox jumped over the lazy dog"


words = sentence.split()

longest_word = ""


for word in words:
    
    word = ''.join(c for c in word if c.isalpha())
    
    if len(word) > len(longest_word):
        longest_word = word

print(f"The largest word in the sentence is: {longest_word}")
