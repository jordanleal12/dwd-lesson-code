# Lists Exercise

# Shopping Cart
cart = ["apples", "bananas", "bread"]

# 1. Add milk to the end of the cart.
# 2. Bananas are out of stock. Remove them.
# 3. You remembered you need eggs and they're a higher priority
#       than everything other than apples.
#       Insert eggs right after apples.
# 4. You decide to get 2 more apples, so add them.
# 5. Print out how many apples are in the cart.
# 6. Sort the cart alphabetically.
# 7. Get and print a new list with only the first 2 items.
# 8. Get and print a new list with all items EXCEPT the first one.
# 9. Print the final cart and how many items are in it.
#1
cart.append("milk")
#2
cart.pop(1)
#3
cart.insert(1, "eggs")
#4
extra_apples = ["apples", "apples"]
cart.extend(extra_apples)
#5
print(cart.count("apples"))
#6
cart.sort()
#7
cart_first2 = cart[:2]
print(cart_first2)
#8
cart_except_first = cart[1:]
print(cart_except_first)
#9
print(cart, len(cart))