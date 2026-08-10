# Write a Python Program to Remove Punctuation From a String.

punctuations = '''!()-[]{};:'\\,<>./?@#$%^&*_~"'''

text = 'Hello!!!, he said ---and went'

clean_text = ''
for char in text:
    if char not in punctuations:
        clean_text = clean_text + char
    

print(clean_text)