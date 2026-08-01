# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

with open ("ducat.txt" , "w") as file:
    file.write("vaibhav")
    
file = open("ducat.txt", "r")
print(file.read())
file.close()

file = open("ducat.txt", "w")
file.write("Python Programming")
file.close()

file = open("ducat.txt", "r")
print(file.read())
file.close()


# create mode(x)
# ---create a new file
file = open("newfile.txt","x")
file.close()

with open("newfile.txt","x") as file:
    file.write("hello world")
    

#readlines()
#read all lines and returns a list
with open("newfile.txt", "r") as file:
    lines = file.readlines()
    print(lines)


#close
# file.close()
file = open("newfile.txt", "r")
print(file.read())
file.close()