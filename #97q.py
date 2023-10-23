import string
import re

text = "Hello, World! This is an example text: with some punctuation."

translator = str.maketrans('', '', string.punctuation)
text_no_punctuation = text.translate(translator)

text_no_punctuation_regex = re.sub(r'[^\w\s]', '', text)

print("Text without punctuation (using string.translate()):", text_no_punctuation)
print("Text without punctuation (using regex):", text_no_punctuation_regex)
