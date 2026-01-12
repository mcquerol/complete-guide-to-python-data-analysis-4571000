# Python code below
# Use print("messages...") to debug your solution.

show_expected_result = True
show_hints = True

def palindromes(anagrams_by_signature):
    # Your code goes here.
    palindromesList = []
    for group in anagrams_by_signature.values():
        for word in group:
            if len(word) < 7:
                continue
            else:
                rev = word[::-1]
                if rev in group and rev != word:
                    palindromesList.append({word, rev})
    return palindromesList
