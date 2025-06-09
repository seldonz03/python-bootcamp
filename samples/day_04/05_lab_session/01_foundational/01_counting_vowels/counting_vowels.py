def count_vowels(string):
    """Return the number of vowels in the given string"""
    count=0
    vowels = "aeiou"

    for vowel in string:
        if vowel in vowels:
            count += 1
    return count

Letter=input("Enter a Word:")
letter_count=count_vowels(Letter)
print("Vowels:",count_vowels(Letter))


