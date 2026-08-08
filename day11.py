#Task1--->
'''
correct_code="1345"
while True:
    code=input("Enter the code: ")
    if code==correct_code:
        print("Correct")
        break
    else:
        print("Wrong")
'''
#Task2--->OTP verification
'''
otp="1345"
attempt=0
while attempt<7:
    code=input("Enter OTP: ")
    if code==otp:
        print("Correct OTP")
        break
    else:
        print("Wrong OTP")
    attempt=attempt+1
if attempt==5:
    print("OTP Expired")
'''

#Task3--->Food order
'''
orders=[]
count=0
while True:
    food=input("Enter food: ")
    if food=="exit":
        print("Thank you for ordering")
        print("Your orders:",orders)
        print("Total orders:",count)
        break
    print(food, "added to order")
    orders.append(food)
    count=count+1
'''
#Task4--->
secret='python'
count=3
attempt=0
while attempt<3:
    game=input('Enter the game name:')
    if game==secret:
        print("You win the game")
        break
    else:
        print("Try again..")
        print('Number of attempts',count)
        count=count-1
    attempt=attempt+1
else:
    print('You lost the game')









