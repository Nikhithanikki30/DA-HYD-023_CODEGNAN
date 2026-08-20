'''
functions-->arguments usage(variable length arguments)
        -->keyword variable length arguments(**kwargs)
'''
#1.Exception handling/scope of variables/built-in functions
#it is a mechanism that helps to respond or make the flow of execution in normal way
#without this error will occur and disrup the flow of program
#common expection-->valueError,TypeError,IndexError,AtrributeError,ZeroDivisionError
'''
Syntax:
try:
    #code that will cause the exception
except Exception as e;
    #code will catch the exception
finally:
    #runs irrespective of both try and except...
    ...
'''

#--->basic exception handling
'''
try:
    #a=10
    a=int(input('Enter the value:'))
    result=20/a
    print(result)
except Exception as e:
    print(e)
'''

'''
--->when i gave value 0 then exception block will be run and print the message instead of throwing error
Enter the value:0
division by zero

--->when i gave value float value then exception block will be run and print the message instead of throwing error
Enter the value:2.5
invalid literal for int() with base 10: '2.5'
'''
#--->basic example with ValueError,ZeroDivisionError,NameError
'''
try:
    #a=10
    a=int(input('Enter the value:'))
    result=20/a
    print(result)
except ValueError:
    print(f'Invalid enter, enter only integer values')
#output: Enter the value:22.45
         #Invalid enter, enter only integer values
    
except ZeroDivisionError:
    print(f'Division by zero is not possible')
#output:Enter the value:0
        #Division by zero is not possible

except NameError:
    print(f'Check the name of varibale properly')
#Output: Enter the value:45
         #Check the name of varibale properly
'''

#--->basic example with IndexError,AtrributeError
'''
try:
    a=[10,20,30]
    a.apped(24)
    print(a[5])
#in this i had given 3 numbers in the list and given index is out of range then this message will be printed
except IndexError:
    print(f'Check the length  of list properly and access elements')

#i had given append spelling wrong so that this exception message will be printed
except AttributeError:
    print(f'Dont rush write the name properly')
'''

#--->both exceptions in single case
'''
try:
    a=[10,20,30]
    a.apped(24) #'list' object has no attribute 'apped'
    print(a[5])  #list index out of range
except (IndexError,AttributeError) as e:
    print(e)
    #a=list(map(int,input('Enter:').split(',')))
    #print(a) -->we can take input in exception
'''

#--->BMI calculator-->bmi=(weight)/((height**2))
#--->Use exception handling along with jumping statement in functions BMI task
#feet-->12 inches-->1 inch-->2.3
'''
while True:
    try:
        weight=int(input('Enter the weight in kgs:'))
        height=float(input('Enter the height in meters:'))
        #write my logical condition
        if weight>0 and height>0:
            break
        else:
            print('Make sure to enter only correct values')
    except ValueError:
        print(f'Make sure to enter weight as integer only, height also as number')
bmi=((weight)/(height)**2)
print(bmi)
'''

#2.Scope of Varibales-->scope is basically the region/area where it is accessible
#Local Scope, Global Scope
#Usage of Global keyword along with enclosing scope(nonlocal keyword)

#--->local scope-->variables define inside the function accessible only inside
'''
def display():
    """Usage of local scope"""
    name='Codegnan' #local variable
    print(name)
display()
#print(name)-->it raises NameError
'''

#--->global scope-->variables define outside the function accessible anywhere in the script
'''
place='hyd' #gloal variable
def display():
    """Usage of local and global scope"""
    name='Codegnan' #local variable
    print(name)
    print(f'{name} is in {place}')
display()
print(place)
'''

#--->UnboundLocalError
'''
count=20
def data():
    """usage of global keyword"""
    count=count+5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')
'''

#--->modifying global variable inside the function and accessible outside the function
'''
count=20
def data():
    """usage of global keyword"""
    global count
    count=count+5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')
'''

#--->priority of local vs global
#local has higher priority than global variable
'''
count=20
def data():
    """Priority of local vs global"""
    count=5  #local variable
    count=count+5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')
'''

#--->enclosing scope(nonlocal keyword)
'''
def outer():
    """Outer function with a local variable"""
    count=5
    def inner():
        """Nested function"""
        nonlocal count
        count=count+10
        print(f'Value inside is {count}')
    inner()
    print(f'Value outside is {count}')
outer()
'''

#--->Built-in functions-->avriables builtinscope
len=56
print(len+4)

print(len('Codegnan'))




