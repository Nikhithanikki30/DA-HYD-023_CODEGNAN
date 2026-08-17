#1.Student Marks Manager
'''
marks=[]
for i in range(3):
    mark=int(input('Enter the mark:'))
    marks.append(mark)
print('Original marks:',marks)
marks.insert(0,90)
print(marks)
marks.extend([75,85])
print(marks)
if 75 in marks:
    marks.remove(75)
remove=marks.pop()
print("Removed value:", remove)
print("Final list:", marks)
print("Length:", len(marks))

Output:
Enter the mark:56
Enter the mark:78
Enter the mark:47
Original marks: [56, 78, 47]
[90, 56, 78, 47]
[90, 56, 78, 47, 75, 85]
Removed value: 85
Final list: [90, 56, 78, 47]
Length: 4
'''

#2.Number list analyser
'''
numbers=[20,10,30,20,40,20]
numbers.sort()
print("Sorted list:", numbers)
print("Ascending values:")
for i in numbers:
    print(i)
numbers.reverse()
print("Reversed list:", numbers)
print("Descending values:")
for i in numbers:
    print(i)
num=int(input("Enter the number to search: "))
if num in numbers:
    print("Count:", numbers.count(num))
    print("First Index:", numbers.index(num))
else:
    print("Number not found")
print("Smallest number:", min(numbers))
print("Largest number:", max(numbers))
print("Sum:", sum(numbers))

Output:
Sorted list: [10, 20, 20, 20, 30, 40]
Ascending values:
10
20
20
20
30
40
Reversed list: [40, 30, 20, 20, 20, 10]
Descending values:
40
30
20
20
20
10
Enter the number to search: 20
Count: 3
First Index: 2
Smallest number: 10
Largest number: 40
Sum: 140
'''

#3.Even and odd number seperator
'''
numbers=[10,15,20,25,30,35]
even=[]
odd=[]
for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('Even:',even)
print('Odd:',odd)
print('First three numbers:',numbers[:3])
print('Last three numbers:',numbers[3:])
backup=numbers.copy()
numbers.clear()
print('Original list:',numbers)
print('Backup:',backup)

Output:
Even: [10, 20, 30]
Odd: [15, 25, 35]
First three numbers: [10, 15, 20]
Last three numbers: [25, 30, 35]
Original list: []
Backup: [10, 15, 20, 25, 30, 35]
'''

#4.Unique name manager
'''
names=['Asha','Rahul','Asha','John','Rahul']
a=set(names)
print(a)
a.add('Meera')
print('Added:',a)
a.update(['Arun','priya'])
print('Updated:',a)
if 'John' in names:
    a.remove('John')
    print('Removed:',a)
a.discard('David')
print('Discarded:',a)
for i in names:
    print(i)

Output:
{'Rahul', 'John', 'Asha'}
Added: {'Meera', 'Rahul', 'John', 'Asha'}
Updated: {'priya', 'Meera', 'Arun', 'Asha', 'Rahul', 'John'}
Removed: {'priya', 'Meera', 'Arun', 'Asha', 'Rahul'}
Discarded: {'priya', 'Meera', 'Arun', 'Asha', 'Rahul'}

Asha
Rahul
Asha
John
Rahul
'''

#5.Course student comparision
'''
python_students={'Asha','Rahul','John','Meera'}
da_students={'Rahul','Meera','Arun'}
a=python_students.union(da_students)
b=python_students.intersection(da_students)
c=python_students.difference(da_students)
d=python_students.symmetric_difference(da_students)
print('All Students:')
for i in a:
    print(i)
print('Students have both courses:')
for j in b:
    print(j)
print('Only Python:') 
for k in c:
    print(k)
print('Only one course:')
for m in d:
    print(m)
    
print("\nDA is subset of Python:", da_students.issubset(python_students))
if da_students.issubset(python_students):
    print("All DA students are also Python students")
else:
    print("All DA students are not Python students")

print("Python is superset of DA:", python_students.issuperset(da_students))
if python_students.issuperset(da_students):
    print("Python contains all DA students")
else:
    print("Python does not contain all DA students")

print("Both sets are disjoint:", python_students.isdisjoint(da_students))
if python_students.isdisjoint(da_students):
    print("There are no common students")
else:
    print("There are common students in both courses")

Output:
All Students:
John
Arun
Rahul
Meera
Asha
Students have both courses:
Rahul
Meera
Only Python:
John
Asha
Only one course:
John
Arun
Asha

DA is subset of Python: False
All DA students are not Python students
Python is superset of DA: False
Python does not contain all DA students
Both sets are disjoint: False
There are common students in both courses
'''
                 




















