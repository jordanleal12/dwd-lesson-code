# Callbacks Exercise
#
# 1. Write a function: perform_operation(a, b, math_callback).
# 2. This function should take two numbers and a callback.
# 3. The callback function itself should accept two numbers and return their result
#       (e.g., sum, product).
# 4. perform_operation() should then print this result.
# 5. Create two simple callbacks (e.g., add_them, multiply_them) and
#       test perform_operation with both.

def sum_fn(a, b):
    """Returns sum of numbers"""
    return a + b

def multiply_fn(a, b):
    "Returns multiplication of numbers"""
    return a * b

def perform_operation(a, b, math_cb):
    """Takes two variables and runs them through a maths function"""
    print(f"Result is: {math_cb(a, b)}")

perform_operation(5, 6, multiply_fn)
