from collections import Counter


def anagram(firstname: str, secondname: str) -> bool:
    print(Counter(firstname))
    print(Counter(secondname))

    return Counter(first)==Counter(secondname)




    """Returns True if the first and second word are anagrams.

    Note: Listen and Silent are anagrams
    """

first=input("Please Enter First Word:")
second=input("Please Enter Second Word:")


anagram(first,second)







print("Anagrams:",anagram(first,second))

