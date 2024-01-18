order = ""
price = 0.0

machine = {
    'A1': 'Coca Cola',
    'A2': 'Diet Coke',
    'A3': 'Sprite',
    'A4': '7-Up',
    'A5': 'Fanta',
    'A6': 'Pepsi',
    'B1': 'Cheetos',
    'B2': 'Doritos',
    'B3': 'Pringles',
    'B4': 'Funyuns',
    'B5': "Lay's Potato",
    'B6': 'Ruffles Potato'
}

menu_prices = {
    'A1': 5.25,
    'A2': 4.75,
    'A3': 4.50,
    'A4': 6.00,
    'A5': 5.25,
    'A6': 4.70,
    'B1': 6.75,
    'B2': 4.70,
    'B3': 6.25,
    'B4': 7.75,
    'B5': 6.50,
    'B6': 6.50
}

print('Hello! Welcome to our Vending Machine!\n'
      'Select a drink or a snack of your choice!\n'
      ' =======================|============================\n'
      ' |   Softdrinks, Price  |         Chips,     Price  |\n'
      ' |======================|===========================|\n',
      f'| A1 : Coca Cola  {menu_prices["A1"]} |   B1 : Cheetos        {menu_prices["B1"]}|\n',
      f'| A2 : Diet Coke  {menu_prices["A2"]} |   B2 : Doritos        {menu_prices["B2"]} |\n',
      f'| A3 : Sprite     {menu_prices["A3"]}  |   B3 : Pringles       {menu_prices["B3"]}|\n',
      f'| A4 : 7-Up       {menu_prices["A4"]}  |   B4 : Funyuns        {menu_prices["B4"]}|\n',
      f"| A5 : Fanta      {menu_prices['A5']} |   B5 : Lay's Potato   {menu_prices['B5']} |\n",
      f'| A6 : Pepsi      {menu_prices["A6"]}  |   B6 : Ruffles Potato {menu_prices["B6"]} |\n',
      '====================================================')

while order not in machine:
    order = input('Enter the code of the item that you would like here:').upper()

price = menu_prices[order]

print(f'Please Insert {price} AED')

while True:
    payment = float(input('Insert cash here, we give back the exact amount of change:'))
    
    
    if price > payment:
        print(f'ERROR, insufficient cash. Please take your money back amounting of {payment}','\n')
    else:
        break



change = float(payment - price)

print(f'Your {machine[order]} has been dispensed, please get it at the bottom of the machine.','\n')
if change > 0:
    print(f'Please take your change amounting to: {change} AED. If the change given is short, contact our customer support #123 893 4567','\n')
else:
    print('Thank you and have a nice day!')