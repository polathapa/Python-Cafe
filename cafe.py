
menu = ['Baked aubergine 🍆', 'Steamed rice 🍚', 'Chickpea soup 🍲', 'Fried tofu 🍢']
stock = {'Baked aubergine 🍆': 20, 'Steamed rice 🍚': 40, 'Chickpea soup 🍲': 32, 'Fried tofu 🍢': 25} # Dictionary with corresponding key : value
price = {'Baked aubergine 🍆': 7, 'Steamed rice 🍚': 4, 'Chickpea soup 🍲': 6, 'Fried tofu 🍢': 7} # Dictionary with corresponding key : value

# Giving an initial value of 0 to total stock worth
total_stock_worth = 0

for item in menu: # Iterating through every item on the menu
    item_value = stock[item] * price[item] 
    print(f"{item}:\n Stock - {stock[item]},\n Price - £{price[item]},\n Total Value - £{item_value}\n") # Every item name, stock, price and value is printed as it iterates
    total_stock_worth = total_stock_worth + item_value # Every item value is added to the total stock worth

print(f"\nTotal Stock Worth in the Cafe: £{total_stock_worth}")
