"""Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them
alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world"""

# Accept input from the user
input_sequence = input("Enter a whitespace separated sequence of words: ")

# words = input_sequence.split()

# deduplicate_words = set(words)

# sorted_words = sorted(deduplicate_words)

# output_sequence = " ".join(sorted_words)



# improved version

output_sequence = " ".join(sorted(set(input_sequence.split())))
print(output_sequence)
