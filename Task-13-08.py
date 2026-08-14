#Task 1
'''
t = ((10, 20, 30, 40),(50, 60, 70, 80),(90, 100, 110, 120))

# Slicing
print(t[0:2])
print(t[1:3])

# Striding
print(t[::2])
print(t[0][::2])
print(t[0][::-1])

# Tuple to list
my_list = list(t[0])
print(my_list)

# List functions
my_list.append(50)
print(my_list)

my_list.insert(1, 15)
print(my_list)

my_list.remove(30)
print(my_list)

my_list.pop()
print(my_list)

my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)
'''

#Task 2-method 1
'''
s=input("Enter a string: ")
seen=[]
for ch in s:
    if ch not in seen:
        if s.count(ch)>1:
            print(ch, "is repeating", s.count(ch), "times")
        seen.append(ch)
        
#---->output
Enter a string: programming
r is repeating 2 times
g is repeating 2 times
m is repeating 2 times
'''

#Task 2-method 2
'''
s=input("Enter a string: ")
seen = []
for ch in s:
    if ch not in seen:
        if s.count(ch)>1:
            indexes=[]
            for i in range(len(s)):
                if s[i]==ch:
                    indexes.append(i)
            print(ch, "is repeating", len(indexes), "times")
            print("index =", indexes)
        seen.append(ch)
        
#--->output
Enter a string: programming
r is repeating 2 times
index = [1, 4]
g is repeating 2 times
index = [3, 10]
m is repeating 2 times
index = [6, 7]
'''
















