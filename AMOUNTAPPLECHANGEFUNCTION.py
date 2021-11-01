def get_amount_money():
    amount_money_function = int(input('Enter the amount of money you have: '))
    return amount_money_function

def get_price_apple():
    price_apple_function = int(input('What is the price of the apple you wish to purchase?: '))
    return price_apple_function

def maximum_apple():
    maximum_apple_function = int(amount_money/price_apple)
    return maximum_apple_function

def amount_change():
    amount_change_function = int((amount_money)-(price_apple*apple))
    return amount_change_function

def display_output(maximum_apple_function, amount_change_function):
    output_function = print(f"You can buy {apple} apples and your change is {change} pesos.")

amount_money = get_amount_money() #this ask the user the amount of money he has
price_apple = get_price_apple() #this ask the user what price of the apple he wanna buy
apple = maximum_apple() #this is the calculation of the maximum apple he can buy with the amount of money he has
change = amount_change() #this is the calculation of how much money the user's going to have after buying apples
display_output(apple, change) #this let the user know how many apple the user's can buy and how much money is left after buying