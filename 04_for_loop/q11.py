# Question: Consecutive Duplicate Remover
# Input:
# Enter a word: aaabbbccdaa

# Output:
# abcda


word = input("Enter a word: ")

result = ""
previous = ""

for ch in word:
    if ch != previous:
        result = result + ch
        previous = ch

print(result)