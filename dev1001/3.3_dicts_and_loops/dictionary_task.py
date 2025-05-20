# #Create phase exercises

# #1.1

# #i, ii.
# report_card = {
#     "Bob": {"Maths": 89, "English": 70, "Geography": 82, "Science": 66}, 
#     "Kelly":{"Maths": 58, "English": 62, "Geography": 69, "Science": 46}, 
#     "James":{"Maths": 93, "English": 87, "Geography": 78, "Science": 95}, 
#     "Bree":{"Maths": 77, "English": 73, "Geography": 65, "Science": 68}
#     }

# #iii.
# for k, v in report_card.items(): 
#     print(f"The subjects and results for {k} are: \n{v}\n")

# #iv.
# print("-" * 20, "\n")
# avg = 0
# for i in report_card["Kelly"].values():
#     avg += i
# print(f"The average mark for Kelly is {avg / len(report_card["Kelly"].values())}\n")
# print("-" * 20, "\n")

# #Advanced Challenge. 
# for k, v in report_card.items():
#     min_score = min(v, key=v.get)
#     max_score = max(v, key=v.get)
#     print(f"The lowest scoring subject for {k} is {min_score} with {v[min_score]}")
#     print(f"The highest scoring subject for {k} is {max_score} with {v[max_score]}\n")
# print("-" * 20, "\n")

# # 1.2:

# #i.
# text = """
# This is a sample text. This text is for a sample programming exercise.
# The exercise is to count words in this text.
# Ignore case and punctuation for simplicity.
# """

# #ii.
# text_list = text.lower().replace(".", "").split()

# # iii. 
# text_dict = {}

# # iv.
# for i in text_list:
#     if i in text_dict:
#         text_dict[i] += 1
#     else:
#         text_dict[i] = 1

# # v.
# print(text_dict)

# # vi.
# print("\n", "-" * 20, "\n")
# for k, v in text_dict.items():
#     print(f"{k}: {v}")

# # Advanced Challenge. 
# print("\n", "-" * 20, "\n")
# sorted_dict = dict(sorted(text_dict.items()))
# freq_sorted = dict(sorted(text_dict.items(), key=lambda i: i[1], reverse=True))
# print(f"Alphabetically sorted: \n{sorted_dict}\n")
# print(f"Frequency sorted: \n{freq_sorted}")

# # 2.1

# # i.
# print("\n", "-" * 20)
# shopping_list = []

# # ii - iv.
# while True:
#     option = input("""
# 1. Add Item 
# 2. View List  
# 3. Mark Item as Purchased  
# 4. exit
# : """)
# # v.
#     match option:
#         case "1":
#             add_item = input("Enter item to add to shopping list: ").lower()
#             if add_item in shopping_list:
#                 print("item already in list")
#             else:
#                 shopping_list.append(add_item)
#             input("Hit enter to view options again")
#         case "2":
#             if len(shopping_list) == 0:
#                 print("Your shopping list is empty")
#                 input("Hit enter to view options again")
#             else:
#                 for x, i in enumerate(shopping_list):
#                     print(f"{x + 1}. {i}")
#                 input("Hit enter to view options again")
#         case "3": 
#             purchased = input("Enter shopping list item to mark as purchased: ").lower()
#             while purchased not in shopping_list:
#                 purchased = input("Please enter a valid item: ").lower()
#             shopping_list.remove(purchased)
#             input("Hit enter to view options again")
#         case "4":
#             print("Goodbye!")
#             break
#         case _:
#             print("Invalid option, please try again")
#             input("Hit enter to view options again")


# 2.2:

# i.
print("\n", "-" * 20, "\n")
users = [
    {"id": "user1", "name": "Alice", "email_verified": True, "logins_last_month": 15},
    {"id": "user2", "name": "Bob", "email_verified": False, "logins_last_month": 3},
    {"id": "user3", "name": "Charlie", "email_verified": True, "logins_last_month": 22},
    {"id": "user4", "name": "David", "email_verified": True, "logins_last_month": 8},
    {"id": "user5", "name": "Eve", "email_verified": False, "logins_last_month": 30},
]

#ii.
inactive_user_ids = []
for i in users:
    if i["logins_last_month"] < 5:
        inactive_user_ids.append(i["id"])
print(inactive_user_ids)

# iii.
print("\n", "-" * 20, "\n")
needs_verification_reminder = []
for i in users:
    if i["email_verified"] is False:
        needs_verification_reminder.append(i["name"])
for i in needs_verification_reminder:
    print(f"Reminder sent to {i} to verify email")

# iv.
print("\n", "-" * 20, "\n")
total_logins = 0
for i in users:
    total_logins += i["logins_last_month"]
print(f"Total logins = {total_logins}")

# Advanced Challenge.
print("\n", "-" * 20, "\n")
most_active = max(users, key=lambda x: x["logins_last_month"])
print(f"{most_active['name']} has the most logins with {most_active['logins_last_month']}")

