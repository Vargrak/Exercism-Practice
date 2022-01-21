def find_anagrams(word, candidates):
    results = []
    for candidate in candidates:
        if sorted(word.lower()) == sorted(candidate.lower()) and word.lower() != candidate.lower():
            results.append(candidate)
    return results