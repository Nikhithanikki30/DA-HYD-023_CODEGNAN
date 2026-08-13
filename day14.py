'''
Lists,tuples...
'''
#1.List-->mutable,ordered,heterogenous
#index(),count(),copy(),sort(),reverse()

#---->index()
'''
details=['Codegnan',7,2018,'Hyderabad']
print(len(details))
print(details.index(7))
print(details.index('Codegnan'))
details.extend([7,21,45,21])
print(details)
print(details.index(21)) #it returns first occurance
print(details.index(21,6))
#print(details.index('Python'))-->it raises valueError
'''
#--->count()
'''
print(details.count(21))
print(details.count('python'))
'''

#-------------> yestarday's task code
'''
data=['codegnan','saketh','python','java']
for i in data:
    print(data.index(i),':',i)

#another way-->
for obj in range(len(data)):
    print(obj,':',data[obj])
'''

#--->copy()-->it creates shallow copy of given collection
'''
data=['codegnan','saketh','python','java']
new=data.copy()
print(new)
print(type(new))
print(len(data))

new[2]='Agentic AI'
print(new)
print(data)

data.append('nikki')
print(data)
print(new)

data.extend(['rishi'])
print(data)
print(new)

data.pop()
print(data)
print(new)

data.remove('nikki')
print(data)
print(new)
'''

#whenever we make changes in nested list original will also be effected
'''
data=[1,4,5,[21,34,45],23]
print(data)
new=data.copy()
print(new)

new[3][2]='Agents'
print(new)
print(data)

new[1]='Python'
print(new)
print(data)
'''

#--->sort()
'''
marks=[14,24,-45,27,35]
print(marks)
marks.sort() #returns in ascending order...(big to small)
#print(marks.sort()) returns None
print(marks)
marks.sort(reverse=True) #it returns in descending order...(small to big)
print(marks)
marks.insert(2,'code')
print(marks)

#we cannot compare string and integer-->sort is not possible
marks=['codegnan','nikki','python','java',21]
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
'''

#--->reverse()-->returns in reverse order
'''
marks.reverse()
print(marks)
print(marks[::-1])
'''

#type(),len(),max(),min(),print()

#--->sorted()-->returns in ascending order and gives in the list
'''
print(sorted('codegnan')) #returns list
print(sorted('nikki'))
print(sorted('python'))
print(sorted('java'))
#print(sorted(['code',23,45,'56'])-->raises error
'''


#2.Tuples-->tuples are also indexed,ordered,heterogenous,immutable collection
#dimensions,co-ordinates,database records
#we prefer '()' notation for tuple
#we cannot change bcoz tuples are immutable
#we cannot combine tuple and list it raises an error
'''
a=()
print(type(a))
print(len(a))

dimensions=1.5,2.5
print(dimensions)
print(type(dimensions))
print(len(dimensions))
'''

#--->operations-->indexing,slicing,striding,membership,ordered,merging,repetion
'''
courses=('PFS','JFS',('DA','DS'),'agentic ai',[100,6,6])
print(courses)
print(len(courses))

print(courses[3][:-2])
print(courses[3][-2:])

courses[-1].append('codegnan') #we can make any modifications inside the list
print(courses)

print('PFS' in courses) #membership
d=courses*2 #repeat
print(d)
e=courses+(2,3,4,5) #merging
print(e)
'''

#--->tuples immutable-->count(),index()
'''
courses=('PFS','JFS',('DA','DS'),'agentic ai',[100,6,6])
print(courses.index('agentic ai'))
print(courses.count('Agents'))

#print(courses.sort())-->attributeError
#sort is in list not in tuple

print(sorted(courses[-1]))

#print(sorted(courses))-->it raises an error, as we have an mixed type

d=tuple(sorted((23,67,47))) #TypeCasting
print(d)
'''

#--->accept group of integers space seperated
'''
a,b=map(int,input('enter the values:').split(','))
print(a,b)

a=tuple(map(int,input('Enter the values:').split(',')))
print(a)
'''

#--->eval()
'''
print('9+4') #it returns 9+4 bcoz it is in the string format
print(eval('9+4')) #by using eval in this, it add 9+4 and gives 13 as output

a=eval(input('Enter a list:')) #we can also give int,str,float 
print(a)
print(type(a))
#by default it returns tuple as type, if we give list it returns list
'''


#Task 1-->create a nested tuple as above and work on slicing,striding,and list functions


#Task 2--> take a user input as string, do this is two ways:
'''
1) give the count of each of each repeating character
test case 1: programming
r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2) r is repeating 2 times
index=[1,4]
g is repeating 2 times
index=[3,10]
m is repeating 2 times
index=[6,7]
'''








