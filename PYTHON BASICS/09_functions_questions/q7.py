# Write a function reverse_string(text) that returns the reversed string.


def reverse_string(text):
     return text[::-1]

print(reverse_string("hello"))



def reverse_string(text):
     rev=""

     for i in text:
          rev= i + rev
     return rev

print(reverse_string("python"))