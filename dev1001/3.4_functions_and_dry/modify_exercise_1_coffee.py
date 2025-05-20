# --- modify_exercise_1_coffee.py ---

# Inputs (already defined for you)
price_per_coffee = 3.50  # Price for one coffee
number_of_coffees = 8
service_fee_threshold = 5 # Orders above this many coffees incur a service fee
fixed_service_fee = 2.00

def calculate_bulk_coffee_order_total(price, coffees, service_fee, fixed_fee):
    """
    Calculates the total cost for a bulk coffee order.
    If the number of coffees is above the service_fee_threshold,
    a fixed_service_fee is added.
    This function uses the global variables defined above.
    """
    base_coffee_cost = price * coffees
    if coffees > service_fee:
        base_coffee_cost += fixed_fee
    return base_coffee_cost


# --- Main part of the script (provided) ---
order_total = calculate_bulk_coffee_order_total(price_per_coffee, number_of_coffees, service_fee_threshold, fixed_service_fee)

# Outputs (already defined for you)
print(f"Number of coffees: {number_of_coffees}")
print(f"Price per coffee: ${price_per_coffee:.2f}")
if number_of_coffees > service_fee_threshold:
    print(f"Service fee applied: ${fixed_service_fee:.2f}")
else:
    print("No service fee applied.")
print(f"Total order cost: ${order_total:.2f}")
