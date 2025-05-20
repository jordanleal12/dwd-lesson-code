# map() Exercises
#
# Exercise 1
# ----------
# You have a list of product prices.
# Use `map` and a lambda to create a new list where each price
# has a 20% tax added to it (price * 1.20).
# Remember to format the output nicely if you can
# (e.g., to two decimal places, but the core is the map).

prices = [10.99, 5.49, 20.00]
new_list = list(map(lambda x: f"${x * 1.2:.2f}", prices))
print(new_list)


# Exercise 2
# ----------
# Given a list of scores, use map() to get a list of the grade level for each score.
#
# HD if >=90
# D if >=80
# C if >=70
# P if >=50
# F if <50

scores = [85, 92, 78, 60, 42, 95, 70, 53]
def score_fn(score):
    if score >= 90:
        return f"HD: {score}"
    elif score >= 80:
        return f"D: {score}"
    elif score >= 70:
        return f"C: {score}"
    elif score >= 50:
        return f"P: {score}"
    else:
        return f"HD: {score}"
grade_level = list(map(score_fn, scores))
print(grade_level)
