import re

text = "This is a sample    string with   spaces."

text_without_whitespace = text.replace(" ", "")

text_without_whitespace_regex = re.sub(r"\s", "", text)

print("Text without whitespace (using replace):", text_without_whitespace)
print("Text without whitespace (using regex):", text_without_whitespace_regex)
