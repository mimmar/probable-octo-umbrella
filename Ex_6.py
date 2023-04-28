'''
### Exercise 1.6 | Tickets

Assumptions:
	- 0-6   - kindergarten - ticket price: 0
	- 7-17  - school       - ticket price: 2.28
	- 18-64 - adult        - ticket price: 3.80
	- +65   - pensioner    - ticket price: 1.90

Write a program that will ask a user for his age and a number of tickets he'd like to buy.

Based on the assumptions above calculate the price he should pay for the tickets.
'''
# Input
age = int(input('Please enter your age:\n'))
no_of_tickets = int(input('Please enter the number of tickets:\n'))
category = ['kindergarten', 'school', 'adult', 'pensioner']

# Check if integers provides are valid.
if age < 0:
    print("Age cannot be negative")
    exit()

if no_of_tickets < 0:
    print("Number of tickets cannot be negative")
    exit()

# calculate the price and determine the category
if age in range(0, 7):
    ticket_price = 0
    category = category[0]
elif age in range(7, 17):
    ticket_price = 2.28
    category = category[1]
elif age in range(18, 64):
    ticket_price = 3.80
    category = category[2]
else:
    ticket_price = 1.90
    category = category[3]

total = age * ticket_price

# output

print(f'You have chosen {no_of_tickets} tickets for the category {category}, Your total is: {total}')

