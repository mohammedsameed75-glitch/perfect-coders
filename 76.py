def count_vowels(s):
    if s == "":
        return 0

    if s[0] in "aeiouAEIOU":
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])


text = input("Enter a string: ")

print("Number of vowels =", count_vowels(text))
