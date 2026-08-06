#Task1---->Ecommerce
'''
total=0
for i in range():
    products=input('Enter product name:')
    prices=int(input('Enter the price:'))
    total=total+prices
print('Total Bill =',total)
'''
'''
products=list(map(int,input().split(',')))
total = 0
for i in products:
    total = total+i
print(total)
'''

#Task2--->Password
'''
password=input('Enter password:')
upper=0
lower=0
digits=0
special=0
for i in password:
    if 'A'<=i<='Z':
        upper+=1
    elif 'a'<=i<='z':
        lower+=1
    elif i.isdigit():
        digits+=1
    else:
        special+=1
print('Upper:',upper)
print('Lower:',lower)
print('Digits:',digits)
print('Special character:',special)
'''

#Task3--->email
'''
email=input().split()
for mail in email:
    print(mail.split('@')[1])
'''

#Task4--->print the movie names with serial numbers
for i in range(1,6):
    movies=input('Enter movie names:')
    print(i, ".",movies)








