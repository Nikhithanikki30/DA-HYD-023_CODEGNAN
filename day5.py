'''
task : Student marks and grade analayzer (if-else)
90 - 100 --> 'A'
80 - 89 --> 'B'
70- 79 --> 'C'
60 - 69 --> 'D'
>60 --> Fail
also -ve cases should not be allowed and marks should not be greater 100
'''
#student grade analyzer--->
'''
marks=int(input('Enter the marks:'))
if marks>0 and marks<=100:
    if marks>=90 and marks<=100:
        print("Grade A")
    if marks>=80 and marks<=89:
        print("Grade B")
    if marks>=70 and marks<=79:
        print("Grade C")
    if marks>=60 and marks<=69:
        print("Grade D")
    if marks<60:
        print("Fail")
else:
    print("Enter only +ve values greater than 0 and less than 100")
'''
'''
marks = int(input("Enter student marks: "))

if marks >= 90:
    print("Grade: A")
else:
    if marks >= 80:
        print("Grade: B")
    else:
        if marks >= 70:
            print("Grade: C")
        else:
            if marks >= 60:
                print("Grade: D")
            else:
                print("Fail")                
'''
#Another way by using elif keyword--<if-else-if
#syntax
'''
if(=<condition1>:
    statment.....
elif<condition2>:
    statement.....
elif<condition3>:
    statment....
else:
    statment....
'''
#code
'''
marks=int(input('Enter the student marks:'))
if marks>=100:
    print("Enter values should be greater than 1 and less than 100")
elif marks>=90 and marks<=100:
        print("Grade A")
elif marks>=80 and marks<=89:
        print("Grade B")
elif marks>=70 and marks<=79:
        print("Grade C")
elif marks>=60 and marks<=69:
        print("Grade D")
elif marks<60 and marks>=0:
        print("Fail")
else:
    print("No negative values")
'''
#Task-->same usecase try with if-elif-else usage in another way

#voter eligiblity checkcase-->make sure to satisfy all possible conditions
'''
age=int(input('Enter your age:'))
if age>=18 and age<=100:
    print("Vote eligibility")
elif age<18 and age>0:
    print("user need to wait for more",(18-age),"year(s)")
else:
    print("Only +ve values and less than 100 acceptable")
'''

#(a)Output formatting-->old style formatting(using comma)
#% usage (%f,%d), format() usage, fstring notation
#Output-->print()-->we can pass any values also use sep and end
'''
a,b=7,9
print(a)
print(b)
print(a,b)
name="Codegnan";batch="DataAnalysis"
print(name,batch)  #by default sep is having space
print(name,batch,sep=',')
#end='\n', \t-->tab space
print(name,batch,end='\t')
print(a,b,end=' ')
print("Hyderabad")
'''
#(b)Output formatting
name="Codegnan";age=21;batch='DA-HYD-023';place='Hyderabad'
print(batch,'is in',name) #variables and msg to be sepearted by comma
print(name,'is in',place,'age is',age,'years')
#Old style formating-->%d(integer), %s(string), %f(float)
salary=25000
print("His salary is %d"%(salary))
print("His salary is %f"%(salary))
print("His salary is %.1f"%(salary)) #%.1f(rounding to 1 decimal)

#.format() usage
print("{} is in {}".format(name,place)) #order matters
#fstring usage(more recommended)
print(f'{name} is in {place}')
print(f'{"nikki"} is in {name}')



