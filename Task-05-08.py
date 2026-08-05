#Task 1-->observe +ve +ve,-ve -ve, +ve -ve,-ve +ve all possibilities
'''
name='badminton'
#1.(+ve +ve) indexing--->
print(len(name))
print(name[0:4]) #output:badm
print(name[1:5]) #output:admi
print(name[2:7]) #output:dmint
print(name[3:8]) #output:minto
print(name[0:9]) #output:badminton

#2.(-ve -ve) indexing--->
print(name[-5:-1]) #output:into
print(name[-8:-3]) #output:admin
print(name[-7:-2]) #output:dmint
print(name[-6:-1]) #output:minto
print(name[-9:-4]) #output:badmi

#3.(+ve -ve) indexing--->
print(name[0:-1]) #output:badminto
print(name[1:-2]) #output:admint
print(name[2:-3]) #output:dmin
print(name[3:-1]) #output:minto
print(name[0:-4]) #output:badmi

#(-ve +ve) indexing--->
print(name[-5:8]) #output:inton
print(name[-7:7]) #output:dmito
print(name[-9:5]) #output:badmin
print(name[-6:6]) #output:mint
print(name[-4:8]) #output:nton
'''

#Task: A B C D E F G H I J K L M O P Q R S T U V W X Y Z
#use loops and strings to return A to Z
'''
for i in range(65,91): #65 is starting number, 91 is ending number
    print(chr(i),end=' ')
'''



