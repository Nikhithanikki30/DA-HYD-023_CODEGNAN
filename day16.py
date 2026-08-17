'''
Mapping-->Dictionary-->collection of key-value pairs used to store related data
-->JSON,APIs,database records
dict() function-->data={}-->data={key:value}
dictionary is mutable,ordered,indexed through keys,heterogeneous,
keys must be unique (int,float,strings...)
'''
#1.dictionary
details={}
print(type(details))
details={'id':'CGH3882',
         'Name':'Nikhitha',
         'Gender':'Female',
         'Age':21,
         'Batch':'DA23',
         'Place':'Hyd'}
print(details)
print(len(details))


#2.access data from dictionary
#-->details[0]-->KeyError
'''
print(details.keys()) #it returns keys from the dictionary
print(details['id'],details['Name'])
#if key name is not matching/invalid-->then it raises an keyError
#--->print(details['Marks'])-->keyError as marks is not present

print('====================================')

details['Marks']=[]
print(details)

details['Marks'].append(20)
print(details)

details['Marks'].extend([24,28,30,35,40])
print(details)
'''

#-->create a key-value pair for practice session
'''
details['Practice-Session']=[]
print(details)

details['Practice-Session']=('Tuesday','Thursday','Saturday')
print(details)
'''

#-->accessing 3rd day marks of student
'''
print(details['Marks'][2])

print('====================================')
'''

#-->accessing second day of practice session
'''
print(details['Practice-Session'][1])
'''

#-->create a key-value pair for mock interview
'''
details['MI']=('Monday','Wednesday','Friday')
print(details)

print('====================================')
'''

#operations-->mutable,indexing through keys,membership
'''
print('Wednesday' in details) #returns false as we doesnt have wednesday as key
print('MI' in details) #returns True as we have MI as key

print('====================================')

for i in details:
    print(i) #it returns keys one by one

print('====================================')

for i in details.keys():
    print(f'Key:', i)
    print(f'Value is:',details[i])

print('====================================')

for i in details.values(): #returns value from dictionary
    print(i)

print('====================================')

for i in details.items():
    print(i)

print('====================================')

for key,value in details.items():
    print(f'key is {key}')
    print(f'Value is {value}')
'''

#we can update values by above way or below way
#to update group of values we use update
#--->Update()-->updating the dictionary with key-value pairs
'''

details.update({'Marks':[20,24,28,30,35,40],
                'Practice-Session':['Tuesday','Thursday','Saturday']})
print(details)

print('====================================')

#taking input from the user and extended to the original marks
marks=list(map(int,input('Enter the marks:').split(',')))
print(marks)
details['Marks'].extend(marks)
print(details)
'''

'''
print('====================================')

print(details.keys())
print(details.get('Name'))
print(details.get('Branch')) #it returns None as we dont have branch as key
'''

#--->setdefault()
'''
details.setdefault('Branch') #if key is not present it inserts the data into dict
print(details)

details['Branch']='CSE'
print(details)
'''

#example--->print(details.setdefault('Name','Nikki'))
#in setdefault it will be create when key is not present
#in setdefault if key is present it cannot do anything


#--->pop()
'''
print(details.pop('Branch')) #we need to mention key
print(details.keys())
'''

#--->popitem()-->removes and returns a key value pair as a 2-tuple
'''
print(details.popitem())
print(details.popitem())
'''

#--->del()
'''
del details['id']
print(details.keys())
'''

#--->clear()
'''
details.clear()
print(details)
'''

#--->fromkeys()-->creates a dictionary from iterable(lists,tuples,sets,strings)
'''
data=['nikki','rishi','data']
a=dict.fromkeys(data) #creates a dictionary but values set to None
print(a)
a['nikki']=21
print(a)
c=dict.fromkeys(['CGH3882','CGH1234'],['Code','gnan'])
print(c)
'''

#Task: create a dictionary with your personal details, similar to your codegnan profile


