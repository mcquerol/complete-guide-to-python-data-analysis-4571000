# Python code below
# Use print("messages...") to debug your solution.

show_expected_result = True
show_hints = True

import itertools

def palindromes(anagrams_by_signature):
    # Your code goes here.
    palindromesList = []
    for group in anagrams_by_signature.values():
        for word1, word2 in itertools.combinations(group, 2):
            if word1 == word2[::-1] and len(word1) > 6:
                palindromesList.append({word1, word2})
    return palindromesList
