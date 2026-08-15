#1.Text Case Converter
'''
text=input("Enter a sentence: ")
methods=["Upper", "Lower", "Title", "Capitalized", "Swap case"]
for method in methods:
    if method=="Upper":
        print("Upper :", text.upper())
    elif method=="Lower":
        print("Lower :", text.lower())
    elif method=="Title":
        print("Title :", text.title())
    elif method=="Capitalized":
        print("Capitalized :", text.capitalize())
    elif method=="Swap case":
        print("Swap case :", text.swapcase())
if text.isupper():
    print("Original text is uppercase")
else:
    print("Original text is not uppercase")
if text.islower():
    print("Original text is lowercase")
else:
    print("Original text is not lowercase")

if text.istitle():
    print("Original text is title case")
else:
    print("Original text is not title case")

OUTPUT--->
Enter a sentence: WELCOME TO PYTHON
Upper: WELCOME TO PYTHON
Lower: welcome to python
Title: Welcome To Python
Capitalized: Welcome to python
Swap case: welcome to python

Enter a sentence: PYTHON IS FUN and Learning python
Upper: PYTHON IS FUN AND LEARNING PYTHON
Lower: python is fun and learning python
Title: Python Is Fun And Learning Python
Capitalized: Python is fun and learning python
Swap case: python is fun AND lEARNING PYTHON
'''

#2.Username Validator
'''
while True:
    username=input("Enter username: ")
    if username == "quit":
        break
    if username.isalnum():
        print("Contains only letters and numbers")
    else:
        print("Contains other characters")
    if username[0].isalpha():
        print("Starts with a letter")
    else:
        print("Does not start with a letter")
    if username.isidentifier():
        print("Valid Python identifier")
    else:
        print("Invalid Python identifier")
    if username.isascii():
        print("Contains ASCII characters")
    else:
        print("Contains non-ASCII characters")
        
OUTPUT--->
Enter username: student_10
Contains other characters
Starts with a letter
Valid Python identifier
Contains ASCII characters

Enter username: student10
Contains only letters and numbers
Starts with a letter
Valid Python identifier
Contains ASCII characters

Enter username: 10student
Contains only letters and numbers
Does not start with a letter
Invalid Python identifier
Contains ASCII characters

Enter username: student_name
Contains other characters
Starts with a letter
Valid Python identifier
Contains ASCII characters
Enter username: quit
'''

#3.Student Report
'''
print("=" * 30)
print("STUDENT REPORT".center(30))
print("=" * 30)
for i in range(3):
    name=input("Enter student name: ")
    marks=int(input("Enter marks: "))
    if marks<0 or marks>100:
        print("Invalid marks")
        continue
    if marks>=80:
        grade="A"
    elif marks>=60:
        grade="B"
    elif marks>=40:
        grade="C"
    else:
        grade="Fail"
    print(f"{name.ljust(10)} {str(marks).rjust(5)} {grade.rjust(5)}")
 
OUTPUT--->
==============================
        STUDENT REPORT        
==============================
Enter student name: Asha
Enter marks: 85
Asha          85     A
Enter student name: Rahul
Enter marks: 63
Rahul         63     B
Enter student name: John
Enter marks: 35
John          35  Fail
'''

#4.Character and Text Analyzer
'''
text = input("Enter text: ")
letters=0
digits=0
spaces=0
printable=0
for ch in text:
    if ch.isalpha():
        letters=letters + 1
    if ch.isdigit():
        digits=digits + 1
    if ch.isspace():
        spaces=spaces + 1
    if ch.isprintable():
        printable=printable + 1
print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)
print("Printable:", printable)
print("Lowercase:", text.islower())
print("Uppercase:", text.isupper())
print("Title case:", text.istitle())

OUTPUT--->
Enter text: Python Class 101
Letters: 11
Digits: 3
Spaces: 2
Printable: 16
Lowercase: False
Uppercase: False
Title case: True

Enter text: Python\tClass
Letters: 12
Digits: 0
Spaces: 0
Printable: 13
Lowercase: False
Uppercase: False
Title case: False
'''







        
