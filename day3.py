#Numeric datatype-->int,float,complex along with boolean

#input formatting-->Accepting input from the user-->input()

#1.Accepting integer input from user
'''
age=int(input('Enter the age:')) #by default input() accepts any input-->str
#int(input())-->will accept only integers
print(age)
print(type(age))
'''
#--->replace int with float
#by default input() accepts any input-->str
#float(input())-->will accept only float
'''
age=float(input('Enter the age:')) 
print(age)
print(type(age))
'''

#2.Accepting string input from user
'''
name=input('Enter the name:')
print(name)
print(type(name))
'''

#3.Accept group of values(more than one)
'''
a=input().split()
print(a)
#--->comma seperated values
a=input('Enter the values:').split(',') #inside split we can give any characters
print(a)
'''

#4.Accepting list of integers
'''
marks=list(map(int,input('Enter the values:').split(',')))  #map-->will transform every input to integer type
print(marks)
'''

#5.Now we want to accept 2 values from user
'''
age,salary=map(int,input('Enter the values:').split(','))
print(age)
print(salary)
'''

#Single input-->int(input())
#two inputs-->a,b=map(int,input().split(','))
#any number result as list-->a=list(map(int,input().split(',')))

#6.Accepting integer input from user
'''
marks=list(map(float,input('Enter the values:').split(',')))
print(marks)
'''

#Accepting input from user-->int,float-->input formatting

#Operators--> Operators perform operations between values(operands)
#7 types-->Arithematic,Assaignment,Comparison(relationship)
#Membership,Identity,Logical,Bitwise

#1.Arithematic---> (+,-,*,/)
'''
print(5+3)
print(5-3)
print(5*3)
print(5/3)  #Float value(result)
#Floor division or integer division-->returns quotient
print(5//3) #result will give in integer format(quotient)
print(5%3)  #result will give in integer format(remainder)
print(5**3) #exponential
'''

#Task-->Accept integer input as length,breadth-->find the area of rectangle-->l*b
'''
length=int(input('Enter the value:'))
breadth=int(input('Enter the value:'))
Area=length*breadth
print(Area)
#OR---------------->
length,breadth=map(int,input('Enter the values:').split(','))
area=length*breadth
print(area)
'''

#2.Assaignment--->assaign the values (=,+=,-=)
'''
a=45
print(a)
#update the value of 'a'
a+=5 #or a=a+5
print(a)
b=35
b+=a #or b=b+a
print(b)
b-=5 #or b=b-5
print(b)
'''

#Task---> *=,/=,//=,%=,**=
'''
a=35
print(a)
a*=5
print(a)
a/=5
print(a)
a//=5
print(a)
a%=5
print(a)
a**=5
print(a)
'''

#3.Compariosn--> we can compare the values-->boolean
#(== ,equal to), (!=, not equal to), (<, less than), (>, greater than)
#(<=, less than equal to), (>=, greater than equal to)
'''
age=25
print(age==25) #returns boolean output
print(age!=35)
print(age<35)
print(age>35)
print(age<=35)
print(age>=35)
'''

#4.Membership operator--> in,not in-->boolean output
#it checks for the existance of an object in a collection
'''
marks=[56,75,45,85]
print(35 in marks)
#print(35 in 355)-->TypeError
print(25 not in marks)
'''

#5.Logical operatos--> logical decison making--> and,or,not
#and-->all conditions to be satisfied
#or-->any one condition to be satisfied
#not-->opposite
'''
a=(25 in [25,45,65]) and 45<56
print(a)
b=(25 in [25,45,65]) or 45<56
print(b)
c=not True
print(c)
'''

#Identity operators-->check for identity of an object by using 'id()' function
#is, is not
'''
a=35
b=35
print(id(a))
print(id(b))
print(a is b) #returns boolean output
c=a
print(id(c))
print(c is a)
a=[1,3,4,5]
print(id(a))
c=a
print(id(c))
print(c is a)
'''
