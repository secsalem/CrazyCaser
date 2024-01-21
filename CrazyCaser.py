#!/usr/bin/env python3

from itertools import product

def change_case_combinations(word):
    # Generate all possible combinations of uppercase and lowercase letters
    variations = product(*zip(word.lower(), word.upper()))

    # Join the combinations into strings
    result = [''.join(variation) for variation in variations]

    return result

# Accept the word from the user
word = input("Enter a word: ")

combinations = change_case_combinations(word)

# Write combinations to a text file with a name based on the entered word
output_file = f"{word}_case_variations.txt"
with open(output_file, "w") as file:
    for variation in combinations:
        file.write(variation + "\n")

print(f"Case variations written to {output_file}")
