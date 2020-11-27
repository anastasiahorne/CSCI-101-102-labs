#Anastasia Horne
#​CSCI 101 – Section A
#Python Lab 2B
#References: no one
#Time:35 minutes


convert_rate= 0.0
item_cost= 0.0
currency= str('EUR')
print('What is the original currency of your item?') 
currency= str(input('CURRENCY>'))
print(f'What is today\'s convert rate for {currency}?')
convert_rate= float(input('RATE>'))
print('What is the cost of the item?')
item_cost= int(input('COST>'))
US_dollars= convert_rate * item_cost
print(f' The item that costs {item_cost:.1f} in {currency} currency costs ${US_dollars:.2f} in US dollars')
print(f' OUTPUT ${US_dollars:.2f}')


