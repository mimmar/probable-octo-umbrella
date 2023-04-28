
'''
duration = int(input('Please enter the number of nights: '))
age = int(input('Please enter your age:'))

minor = age < 18
adult = age > 18 or age < 65

price = [100, 200, 180, 150]

if minor is True:
    price = price[0]
elif adult is True and duration >= 2 or duration <= 5:
    price = price[1]
elif adult is True and duration > 5:
    price = price[2]

else:
    price = price[3]

total = price * duration

if age > 65:
    price = total * 0.10

print(f'Your total cost will be: {total}')
'''

'''
- minor (below 18 years old) will pay 100 PLN per night
- adults (of age 18 but less than 65) will pay:
    - 200 PLN if they are staying for one night
    - 180 PLN if they are staying for at least 2 nights but less than 5
    - 150 PLN if they are staying for 5 and more nights
- pensioners (65 and older) will pay the same rate as adults but with a 10% discount
'''

duration = int(input('Please enter the number of nights: '))
age = int(input('Please enter your age: '))

price_per_night = None

if age < 18:
    price_per_night = 100
elif age >= 65:
    price_per_night = 150
else:
    if duration == 1:
        price_per_night = 200
    elif 2 <= duration < 5:
        price_per_night = 180
    else:
        price_per_night = 150

total_cost = price_per_night * duration

if age >= 65:
    total_cost *= 0.9

print(f'Your total cost will be: {total_cost}')
