'''
Tokens-->variables, punctuators
varibales-->Named memory location where we store the data (placeholder)
#Rules are to be followed
'''
#1.MultiAssaignment if variables
name,age,place='Codegnan',21,'hyderbad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='-->')

#Error-->valueError as too many values to unpack (a,b=2,3)

#2.Reassaigning variables
name="Codegnan"
a,b=45,1.5
print(a,b)
a,b=b,a  #swapping
print(a,b,sep=',')

#Error-->NameError (a,b=b,c, print(a,b)) "c" is not defined

#3.Deleting the variables-->del (is used to delete the variables)
#del a,b
#print(a,b)

'''
4.punctuators-->([](Lists),()(tuples),{}(Dict,sets))
example-->
name="Codegnan",age=7  #should not write like this(comma)
print(name,age)
#we should keep semicolon in middle so that the computer can undeerstand what to print below is the correct example and this is how we can seperate
name="Codegnan";age=7;course="Data_Analysis"
print(name,age,course)
'''


#4.DataTypes-->Numeric(int,float,complex), boolean, None
#-->int datatype-->quantity,age..
age=7
print(age)
print(type(age)) #type--> returns the datatype of object
#direct calling the value--> print(type(234))-->literal
quantity=3 #should not start with "0" example-->03,04,05
print(quantity)

#-->float datatype-->temp,salary,price
price=750.24;discount=2.5
print(price,discount,sep=',')
print(type(price))

#-->complex-->combination of real and imaginary
i2=4  #should not write 2i (storing the data)
data=5+i2
print(data)

data=5+2j  #should not write j2 bcoz (j is an imaginary representation)
print(data)
print(type(data))

#-->boolean-->True/False
valid=True   #1
print(type(valid))

error=False  #0
print(type(error))

#5.TypeCasting-->converting one type to another type
#python by default follows implicit type (were we not mention the datatype)
#in that case we will go to explicit conversion
#Rule-->every built-in datatype is a built-in function
#TypeCasting--> int->float->complex->bool

#-->int TypeCasting
age=35
print(type(age))
b=float(age)
print(b)
c=complex(age)
print(c)
d=bool(age)  #returns True for existing data
print(d)
e=bool(0)  #returns False
print(e)

#-->Float-->TypeCasting
quantity=35.5
print(type(quantity))
b=int(quantity)
print(b)
c=complex(quantity)
print(c)
d=bool(quantity)  #returns True for existing data
print(d)
e=bool(0)  #returns False
print(e)

#-->complex-->TypeCasting
#in complex we cannot change into int,float
data=35+2j
print(type(data))
'''
b=int(data)
print(b)
c=float(data)
print(c)
'''
d=bool(data)  
print(d)
e=bool(0)  
print(e)

#example-->combining
e=int(float(bool(45)))
print(e)

f=45+2.5+2+3j+False
print(f)


#6.Sequences-->Lists,tuples,sets,strings,frozensets,mappings(dict)


 
