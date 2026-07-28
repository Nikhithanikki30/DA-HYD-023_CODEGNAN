#IDLE is color coding environment
#hastag is used as Single line comment...
#we use triple quotes(single/double) ''',""" as multiple comments
print("Hello Codegnan")
'''
--->Tokens--> A smallest unit in a program, there are 5 types of tokens...
1.keywords
2.identifiers
3.literals
4.operators
5.punctuators
'''

'''
--->keywords--> these are reserved words in python, we have 35 keywords...
Here is a list of the Python keywords.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
'''

'''
--->identifiers-->These are the names being alloted to variables, functions, classes...
1.we cannot start with a number
2.we can start with Uppercase/lowercase (A-Z,a-z) but not special characters (@,#,$...)
3.no space between letters, where as we can also use underscore as identifier (_)
4.python is a case-sensitive language
'''
name='My name is Nikhitha' #name is an identifer
print(name)
email_id='My email is nikhithakoduri694@gmail.com' #snake-case convention
print(email_id) #as python is case-sensitive-->NameError
#True=45 #No keywords
batch='My batch is DA-23'
print(batch)

'''
--->Literals-->these are constants (value(s))-->number, character
--->Operatos-->Operators perform specific operation--> 7 types
'''
#example-->
length=5
breadth=3
area=length*breadth
print(area)

#--->Multiassaignment of variables
name,location,age='Codegnan','Hyd',7
print(name)
print(location)
print(age)
