from collections import Counter


print("Project Anagram\n\n")

# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, the word "listen" is an anagram of "silent", as the same letters in the same quantity are being used in both words, but in a different order.

anagram_string = input("Enter your string: ").lower()
compare_string = input("Enter your compare string: ").lower()

if(Counter(anagram_string) == Counter(compare_string)):
    print("These strings are Anagram")
else:
    print("Not Anagrams")
