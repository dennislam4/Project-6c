# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-26-2022
# Description: Recursice function that takes two string parameters and returns True if the first string is subsequent of
# the second string, otherwise returns False.

def is_subsequence(word_a, word_b):
    """Returns True if word_a is subsequent of word_b. Returns false if otherwise."""
    if word_a == word_b:
        return True
    elif not word_a:
        return True
    elif not word_b:
        return False
    elif word_a[0] == word_b[0]:
        return is_subsequence(word_a[1:], word_b[1:])
    else:
        return is_subsequence(word_a, word_b[1:])
    
