def find_anagrams(word, candidates):
    expected = []
    for candidate in candidates:
        if word.lower() == candidate.lower():
            continue

        if sorted(word.lower()) == sorted(candidate.lower()):
            expected.append(candidate)

    return expected
