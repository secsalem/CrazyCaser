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

for variation in combinations:
    print(variation)
