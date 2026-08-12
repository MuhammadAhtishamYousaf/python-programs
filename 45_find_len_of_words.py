# Write a Python program to find words which are greater than given length k.

words = ['apple', 'banana', 'graps', 'mango', 'dates']

def filter_words(words, k):
    # clean_words = []
    # for word in words:
    #     if len(word) > k:
    #         clean_words.append(word)
    
    clean_words = [word for word in words if len(word) > k]

    return clean_words

filtered_words = filter_words(words, 5)

print(filtered_words)