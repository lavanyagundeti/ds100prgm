#78

from collections import defaultdict
import string


sentences = [
    "This is the first sentence.",
    "The second sentence is here.",
    "And this is the third sentence."
]


word_counts = defaultdict(int)


for sentence in sentences:
    words = sentence.split()
    # Remove punctuation and convert words to lowercase
    words = [word.strip(string.punctuation).lower() for word in words]
    for word in words:
        word_counts[word] += 1


for word, count in word_counts.items():
    print(f"'{word}': {count}")
