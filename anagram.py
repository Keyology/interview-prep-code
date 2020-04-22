# Given a word and a list of possible anagrams, select the correct sublist.

# Given "listen" and a list of candidates like "enlists" "google" "inlets" "banana" the program should return a list containing "inlets".


'''
------------------
Test Input 

@input: "enlists", "google", "inlets", "banana"]
 '''


def find_anagrams(word, candidates):
    return [
        candidate for candidate in candidates if is_anagram(
            word, candidate)]

# Anagram comparison is case insensitive


def is_anagram(word, candidate):
    word_lowercase = word.lower()
    candidate_lowercase = candidate.lower()
    return (is_not_identical(word_lowercase, candidate_lowercase) and
            is_identical_when_sorted(word_lowercase, candidate_lowercase))


def is_not_identical(word, candidate):
    return word != candidate


def is_identical_when_sorted(word, candidate):
    return sorted(word) == sorted(candidate)