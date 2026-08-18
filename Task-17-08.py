#student profile using Dictionary
student={'name':'Nikhitha',
         'id':'CGH3882',
         'gender':'female',
         'batch':'DA-HYD-023',
         'email':'nikhithakoduri694@gmail.com',
         'phno':9182687358,
         'qualification':'B.Tech',
         'department':'computer science',
         'pass-out-year':2026,
         'percentage':87.5,
         '10th_percentage':99.33,
         'inter_percentage':80,
         'skills':['python','SQL','excel','powerBi']
}
#all students details will be printed
print('Student Details:',student)

print('====================================')

#it prints the length of the students
print(len(student))

print('====================================')

#all keys will be return
print(student.keys())

print('====================================')

#only student-id and student-name will be printed
print(student['id'],student['name'])

print('====================================')

#in this we just created a name called city with an empty list
student['city']=[]
print(student)

print('====================================')

#we added a value to the city
student['city'].append('Ongole')
print(student)

print('====================================')

print('city' in student) #it returns true

print('====================================')

#in this we again created a name called practice-session with values
student['practice-session']=('tuesday','thursday','saturday')
print(student)
#accessing second day of practice session
print(student['practice-session'][1]) #it prints thursday

print('====================================')

#mock-interview is created in the dictionary
student['MI']=('monday','wednesday','friday')
print(student)

print('====================================')

#upto now the length of the students are 16
print(len(student))

print('====================================')

#all the keys will be return one-by-one
for i in student:
    print(i)

print('====================================')

#all the values will be return one-by-one
for i in student.values():
    print(i)

print('====================================')

#key : value will be printed
for i,j in student.items():
    print(f'Key is : {i}')
    print(f'Value is : {j}')

print('====================================')

#we can use 'get' to print that particular value
print(student.get('name'))
print(student.get('practice-session'))

print('====================================')

#it prints None bcoz we did not passed any value
student.setdefault('date-of-birth')
print(student)

print('====================================')

#after adding DOB
print('After adding DOB:')
student['date-of-birth']='30-03-2005'
print(student)

print('====================================')

#we didnt say what to pop, we kept it as empty
#then it will removes the last element
print(student.popitem()) #DOB is removed
print(student.popitem()) #now MI is removed

print('====================================')

#now id is removed and also printed all the dict_keys(updated)
del student['id']
print(student.keys())

print('====================================')

#now the length becomes 14 
print(len(student))

print('====================================')

for key,value in student.items():
    print(f'-->key is = {key}')
    print(f'Value is = {value}')
    
print('====================================')

#output:
'''
-->key is = name
Value is = Nikhitha
-->key is = gender
Value is = female
-->key is = batch
Value is = DA-HYD-023
-->key is = email
Value is = nikhithakoduri694@gmail.com
-->key is = phno
Value is = 9182687358
-->key is = qualification
Value is = B.Tech
-->key is = department
Value is = computer science
-->key is = pass-out-year
Value is = 2026
-->key is = percentage
Value is = 87.5
-->key is = 10th_percentage
Value is = 99.33
-->key is = inter_percentage
Value is = 80
-->key is = skills
Value is = python,SQL,excel,powerBi
-->key is = city
Value is = ['Ongole']
-->key is = practice-session
Value is = ('tuesday', 'thursday', 'saturday')
'''

#now i wanted to add all the deleted one's
print('After adding....')
student['id']='CGH3882'
student['date-of-birth']='30-03-2005'
student['MI']=('monday','wednesday','friday')
print(student)

print('====================================')

for key,value in student.items():
    print(f'-->key is : {key}')
    print(f'Value is : {value}')

#final output:
#id,DOB,MI is added last 
'''
-->key is : name
Value is : Nikhitha
-->key is : gender
Value is : female
-->key is : batch
Value is : DA-HYD-023
-->key is : email
Value is : nikhithakoduri694@gmail.com
-->key is : phno
Value is : 9182687358
-->key is : qualification
Value is : B.Tech
-->key is : department
Value is : computer science
-->key is : pass-out-year
Value is : 2026
-->key is : percentage
Value is : 87.5
-->key is : 10th_percentage
Value is : 99.33
-->key is : inter_percentage
Value is : 80
-->key is : skills
Value is : python,SQL,excel,powerBi
-->key is : city
Value is : ['Ongole']
-->key is : practice-session
Value is : ('tuesday', 'thursday', 'saturday')
-->key is : id
Value is : CGH3882
-->key is : date-of-birth
Value is : 30-03-2005
-->key is : MI
Value is : ('monday', 'wednesday', 'friday')
'''












