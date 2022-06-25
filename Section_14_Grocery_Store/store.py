"""
Simple Groceries App
"""

import Section_14_Grocery_Store.store_service as store_service

user_money = store_service.get_user_money()
basket_items = store_service.start_shopping()
store_service.purchase_items(user_money=user_money, items=basket_items)

