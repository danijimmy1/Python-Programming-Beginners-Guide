"""
Two types of files:
1. Text Files
    -> Plain Text
    -> XML
    -> JSON
    -> Source Code

2. binary Files
    -> Compiled Code
    -> App data
    -> Media files
        ~ images
        ~ audio
        ~ video
"""
# open() can be used for opening the function
# creating a text file
f = open("28_guido_bio.txt")
text = f.read()
f.close()
print(text)

# Another method
# This method automatically closes the file
with open("28_guido_bio.txt") as fobj:
    bio = fobj.read()

print(bio)

print("@"*80)
# Trying to open a file which is not available
try:
    with open("future_lottery_numbers.txt") as f:
        text2 = f.read()
except FileNotFoundError:
    text2 = None

print(text2)

print("^"*80)
# Writing in a file
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]
with open("28_oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")

# Writing in a file
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]
with open("28_oceans_2.txt", "w") as f:
    for ocean in oceans:
        print(ocean, file = f)

# To avoid overriding the file open file in append mode
with open("28_oceans_2.txt", "a") as ff:
    print("="*23, file = ff)
    print("These are 5 Oceans.", file = ff)