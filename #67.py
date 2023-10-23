#67


text = "This is a sample text. This text contains some sample words. Sample words are important."


words = text.split()
words = [word.strip('.,!?') for word in words]


word_freq = {}


for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1


for word, freq in word_freq.items():
    print(f"{word}: {freq}")
