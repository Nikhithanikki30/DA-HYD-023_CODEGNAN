'''
Tokens-->keywords,identifiers,literals,operators,punctuators,variable
operators-->Numberic data(int,float,complex,boolean)
control flow statements-->if,elif,else,for,while
sequences-->strings,list,sets,tuples.mapping(dict)
'''
#1.Strings-->group of characters, where we use single or double or triple quotes for representation of strings...
#strings are immutable,ordered,indexed collection
'''
name='Codegnan'
print(name)
print(type(name))
print(len(name)) #len returns the number of items in container, and space also will be counts
#--->index()-->fetch the object(position) starts at 0 and it ends at len(obj)-1
#we use []-square brackets for representation
print(name[0])
print(name[5])
#print(name[25])-->IndexError as it is out of range
#--->Negative Indexing-->-1 to len(obj)
print(name[-1]) #it returns last character
print(name[-5])
'''

#2.Slicing-->we can access group of objects
#we use [start:end]-->start default-->0, start is included, end is excluded
#slicing is applicable from lower index to higher index
#In slicing does'nt get any error
'''
name='Codegnan'
print(name[:]) #returns entire string
print(name[0:]) #returns entire string
print(name[:4]) #returns at 0th index before 4th index
print(name[1:5])
print(name[3:8])
print(name[7:3]) #returns empty as strings are immutable
print(name[:45]) #returns till end of the string
'''
#--->Negative indexing
'''
name='Python'
#print(name[-1:-5])-->returns empty
print(name[-5:-1]) #starts at -5th and ends at -2
print(name[-2:])
'''
#--->combining positive and negative
'''
name='Python'
print(name[1:-2])
#print(name[2:-6])-->returns empty string
'''
#Task-->observe +ve +ve,-ve -ve, +ve -ve,-ve +ve all possibilities

#3.Striding-->[start:end:step]
'''
course='DataAnalysis'
print(len(course))
print(course[:4])
print(course[4:])
print(course[-3:])
print(course[::1]) #returns all characters
print(course[::2]) #skipping of character (in this example it will skip 1 character)
print(course[1:6:3]) #[1:6]-->ataAn,-->[1:6:3]-->aA
print(course[2::3])
print(course[::-1]) #it returns the reverse of the string
print(course[::-2]) #it skips the character
'''

#4.Operations on strings-->Indexing,concatenation,repetition
'''
name='Codegnan'
print(name*3)
print('*'*25) #repetition
#--->Concatenation-->combining strings
data='nikki'+' '+'python'+' '+'database'
print(data)
print('123'*4) #Numeric String
print('Code' in 'Codegnan')
#in the below case we get every character line by line
for i in 'Codegnan':
    print(i,':')
#in the below case we get every character in side by side with space
for i in 'Codegnan':
    print(i,end=' ')
'''

#5.Built-in functions-->length,min,max,sorted
'''
name='dataCodegnan'
print(len(name))
print(min(name)) #it goes with alphabetical order, ASCII order
print(ord('A')) #to know the ASCII value should use 'ord'
print(ord('a'))
print(max(name))
print(chr(97))
print(sorted(name)) #it returns a list by sorting all elements
'''

#6.Methods on strings-->case-conversions,finding/searching...
'''
name='Codegnan data'
#in case-conversions-->upper(),lower(),title(),capitialize()
#--->upper
a=name.upper()
print(a)
#--->lower()
b=name.lower()
print(b)
#--->title()
c=name.title() #converts every word first letter to uppercase
print(c)
#--->capitalize()-->converts first letter to uppercase
name='codEgnan data'
a=name.capitalize()
print(a)
'''

#Task: A B C D E F G H I J K L M O P Q R S T U V W X Y Z
#use loops and strings to return A to Z
