'''
### Exercise 1.7 | Counting prices

Ask a user for a product he'd like to buy, its quantity and price. Based on that display proper information.

Example:
What would you like to buy? - tomatoes
Provide a price - 5
Provide quantity - 10

For tomatoes, you'd like to buy, you have to pay 50 PLN.
'''

item = str(input('What would you like to buy?:\n'))
price = float(input('What is the unit or per kg cost in PLN?:\n'))
quantity =float(input('How much would you like to buy?:\n'))

total_price = price * quantity

print(f'To buy {quantity} {item}, you pay {total_price} PLN')

