"""
Store service
"""
items_to_purchase = {
    'candy': 7,
    'notebook': 15,
    'paper': 8,
    'coffee': 3,
    'socks': 7
}

items_price_added_to_cart = []


def get_user_money():
    user_money_is_string = True
    user_money = ''
    while user_money_is_string:
        s_user_money = input('How much money do you have: ')
        if s_user_money.isdigit():
            user_money = int(s_user_money)
            user_money_is_string = False
        else:
            print('Please enter a valid amount')

    return user_money


def start_shopping():
    user_shopping = True
    while user_shopping:
        add_item_to_cart = input('What item would you like to add to your cart? ')
        if add_item_to_cart.lower().strip() in items_to_purchase:
            items_price_added_to_cart.append(items_to_purchase.get(add_item_to_cart))
            print(f'You currently have {len(items_price_added_to_cart)} items in your cart')
        else:
            print('Item is not at this store')

        keep_shopping = input('Do you wish to continue shopping? '
                              '(y = yes, n = no) ')
        if keep_shopping.lower().strip() == 'n':
            user_shopping = False

    return items_price_added_to_cart


def purchase_items(user_money, items):
    items_total_cost = 0
    for item in items:
        items_total_cost += item
    if items_total_cost <= user_money:
        amount_left = user_money - items_total_cost
        print(f'Purchase Complete: R{amount_left} left')
    else:
        print('You cannot afford all of these items')
