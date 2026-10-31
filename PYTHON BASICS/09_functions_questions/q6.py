# Write a function count_vowels(text) that returns the number of vowels (a, e, i, o, u) in a string.?


def count_vowels(text):
    count=0
    for i in text:
        if i in "a,e,i,o,u":
            count+=1
            return count
        
print(count_vowels("hello"))        

    