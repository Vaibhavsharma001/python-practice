                                              # PRACTICE SET


# 1.Write a python program to display a user entered name followed by Good Afternoon using input () function.

# 2. Write a program to fill in a letter template given below with name and date.

# letter

# Dear <Name>,

# You are selected!

# <|Date|>

# 3. Write a program to detect double space in a string.

# 4. Replace the double space from problem 3 with single spaces.

# 5. Write a program to format the following letter using escape sequence characters.

# Letter = "Dear Harry, this python course is nice. Thanks!"


                                              # 1
name = input("enter your name:-")
print("Good Afternoon",name)

# or

name =input("enter your name:-")
print(f"Good Afternoon {name}")


                                               # 2
letter='''

Dear <Name>,
     You are selected!
     <|Date|>'''

print(letter.replace("<Name>","Vaibhav").replace("<|Date|>","13Jun26"))



                                               # 3

name = "vaibhav is a good boy"
print(name.find(" "))      #7

                                               # 4

name = "vaibhav is  a good boy"
print(name.replace("  ","   "))


                                                #5

letter = "Dear Vaibhav,\n\tthis python course is nice.\nThanks!"       
print(letter)

