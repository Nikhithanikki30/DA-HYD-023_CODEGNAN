#Task-1--->write a python program to calculate the
#innings of a batsman and count the boundaries ,dotballs, total score using for loop
'''
list=[4,6,1,0,2,4,0,6]
total=0
boundaries=0
dotballs=0
for i in list:
    total=total+i
    if i==4 or i==6:
        boundaries=boundaries+1
    if i==0:
        dotballs=dotballs+1
print('Total score=',total)
print('Boundaries=',boundaries)
print('Dot balls=',dotballs)
'''

#Task-2--->ATM
'''
PIN=input('Enter the number:')
max_attempts=5
current_attempt=0
while current_attempt<max_attempts:
    entered_pin=input('Enter the ATM PIN:')
    if entered_pin==PIN:
        print('Login Successful')
        break
    else:
        print('Entered PIN is wrong..Try again carefully')
        current_attempt+=1
else:
    print('Account locked, try after 24 hours..')
'''

#Task-3--->Phone pattern
password = "159"
count = 0

while count < 3:
    user = input("Enter Pattern: ")

    if user == password:
        print("Unlocked")
        print("*     ")
        print("  *   ")
        print("    * ")
        break
    else:
        count += 1
        if count < 3:
            print("Wrong Pattern! Try Again.")
        else:
            print("Wrong Pattern!")
            print("Try again after 30 seconds.")








