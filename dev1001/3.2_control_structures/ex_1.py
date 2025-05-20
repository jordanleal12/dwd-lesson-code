item_price = int(input("What's the item price?: "))
customer_has_coupon = input("do you have a coupon? (Y/N): ")

if item_price <= 0:
    print("Did you enter item price correctly?")

if customer_has_coupon.lower() == "y":
    customer_has_coupon = True
elif customer_has_coupon.lower() == "n": 
    customer_has_coupon = False
else: 
    customer_has_coupon = False
    print("Coupon input not recognized. Did you enter 'Y' for yes or 'N' for no?")


if customer_has_coupon == True:
    item_price *= 0.9

print(f"Final price: {item_price}")
 