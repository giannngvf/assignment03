def display_price_apple():
    print("The price of the apple is 20 pesos.")

def price_of_apple():
    price_a = 20
    return price_a

def get_pieces_apple():
    pieces_apple_function = int(input('How many apples do you want to buy?: '))
    return pieces_apple_function

def display_price_orange():
    print("The price of the orange is 25 pesos.")

def price_of_orange():
    price_o = 25
    return price_o

def get_pieces_orange():
    pieces_orange_function = int(input('How many oranges do you want to buy?: '))
    return pieces_orange_function

def total_amount():
    total_amount_function = int((price_a*pieces_apple) + (price_o*pieces_orange))
    return total_amount_function

def display_amount():
    amount_function = print(f"The total amount is {amount}.")


price_a = price_of_apple() #this is the price of the apple
display_price_apple() #this let the user know the price of the apple
pieces_apple = get_pieces_apple() #after the user knows the price of the apple, the program will ask how many apple the user's going to buy
price_o = price_of_orange() #this is the price of the orange
display_price_orange() #this let the user know the price of the orange
pieces_orange = get_pieces_orange() #after the user knows the price of the orange, the program will ask how many orange the user's going to buy
amount = total_amount() #this is the calculation of the user's total amount of buying apples and oranges
display_amount() #this let the user know the total amount the user's need to pay