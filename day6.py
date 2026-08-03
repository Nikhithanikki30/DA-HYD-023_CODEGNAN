'''
control statements--> contrl the flow of execution of the program
conditional statements-->if,elif,else..., it tells when to execute
repetition statements(loops)-->for ,while (for withb else), (while with else)
jumping statements-->break,continue,pass
'''

#1.Loops-->loops are helpful for repetition(automative tasks)
#for keyword will be helpful to iterate over a sequence/range
#syntax for (for keyword):
'''
for <temp_var> in sequence/range:
   statement(s).....
'''
#range(stop)-->default 0 ends at stop -1
#range(start,stop,step)---->
#by default  range picks 0 as start value
'''
for i in range(10):
    print(i)
'''
#--->in above case we got 10 iterations
'''
for i in range(1,10):
    print(f'value of i is -->{i}')
'''
#--->numbers which are greater then 5 and print only even number
'''
for i in range(1,10):
    if i>5 and i%2==0:
        print(f'value of i is -->{i}')
'''
#--->ranhe(start,stop,step)-->here step-->interval...
'''
for i in range(10,0,-1):  #it returns counter in reverse order
    print(i)
'''
#print(-10 to -1)
'''
for i in range(-10,0,1):
    print(i)
'''
#2.[]-->we generally use as lists
'''
names=['nikki','sadaf','nithya']
print(len(names))  #len(obj)-->returns the number of items in a container
for i in names:
    print(i)
    print(f'student Name is {i}')
'''
#--->calling single person in the lists
'''
names=['nikki','sadaf','nithya']
print(len(names))
for i in names:
    if i=="nikki":
        print(f'Student name is {i}')
'''
#--->calculate the sum of first 10 numbers
#first understand your input-->range(11)-->10 numbers
#understand your output-->sum(number)
#map the logic
'''
result=0 #target variable
for i in range(11):
    result=result+i #result+=i
    print(f'Result is : {result}')
print(f'Sum of 10 numbers is {result}')
'''
#--->calculate the sum of first 10 even numbers
'''
result=0 #target variable
for i in range(21):
    if i%2==0:
        print(i)
        result=result+i #result+=i
        print(f'Result is : {result}')
print(f'Sum of 10 even numbers is {result}')
'''
#--->Understand the usage with fitness streak example
#workout-->1, workout miss-->0
'''
work_log=[0,1,1,1,0,1,0]
longest_streak=0 #result variable-->longest_streak,current_streak
current_streak=0
for day in work_log:
    if day==1:
        current_streak=current_streak+1
        if current_streak>longest_streak:
            longest_streak=current_streak
    else:
        current_streak=0 #streak breaks
print(longest_streak)
'''
