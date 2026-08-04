'''
usage of else with for-->the else keyword is only be executed when the loop
is completely done without any break
'''
#1.for with else....
#--->in this case when the entire loop execution is done we get result of else block
'''
work_log=[0,1,1,1,0,1,0]
longest_streak=0 #result variable-->longest_streak,current_streak
current_streak=0
for day in work_log:
    if day==1:
        current_streak=current_streak+1
        if current_streak>longest_streak:
            longest_streak=current_streak
            print(longest_streak)
        break
    else:
        current_streak=0 #streak breaks
else:
    print(f'Longest streak is {longest_streak}')
'''
    
#-->in this case we did not used the break so it will execute entirely
'''
work_log=[0,1,1,1,0,1,0]
longest_streak=0 #result variable-->longest_streak,current_streak
current_streak=0
for day in work_log:
    if day==1:
        current_streak=current_streak+1
        if current_streak>longest_streak:
            longest_streak=current_streak
            print(f'Longest streak is {longest_streak}')
        #break
    else:
        current_streak=0 #streak breaks
else:
    print(f'Longest streak is {longest_streak}')
print('Execution done')
'''
#--->example-->for-else with notification scenario
'''
notifications=[0,0,0,0]
for notification in notifications:
    if notification==1:
        print('Unread notification')
        break
else:
    print('All Caught Up')
    
#--->giving 1 into the list
notifications=[0,0,1,0]
for notification in notifications:
    if notification==1:
        print('Unread notification')
        break
else:
    print('All Caught Up')
'''
#--->try to take notifications from user-->list of integers
'''
notifications=list(map(int,input('Enter the values --> 0 or 1:').split(',')))
print(notifications)
for notification in notifications:
    if notification==1:
        print('Unread notification')
        break
else:
    print('All Caught Up')
'''

#2.while-->it relies on condition it will be completely executed until the
#contidition is satisfied...
'''
Syntax while:
   while<condition>:
      statement(s)....
'''
#--->it runs an infinite loop
'''
while True:
    print('yes') #yes will be print infinitely, we need to press ctrl+c to interupt
'''
#--->print 1 to 10 numbers
'''
i=1 #initialised statement
while i<=10:
    print(i)
    i=i+1 #counter
'''
#--->print the counter from 10 to 1
'''
i=0 #initialised statement
while i<=10:
    print(10-i)
    i=i+1 #counter
'''
#Banking scenario-->PIN authentication if more than 3 attempts it should say account locked...
PIN='1234'
max_attempts=3
current_attempt=0
while current_attempt<max_attempts:
    entered_pin=input('Enter the ATM PIN:')
    if entered_pin==PIN:
        print('Login Successful')
        break
        #continue-->it holds for this condition and skips to the next part of the execution
    else:
        print('Entered PIN is wrong..Try again carefully')
        current_attempt+=1
else:
    print('Account locked, try after 24 hours..')








