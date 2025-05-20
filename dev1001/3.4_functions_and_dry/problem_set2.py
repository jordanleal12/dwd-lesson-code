"""Functions for library checkout"""

def generate_checkout_message(book_title, member_name, due_days=14):
    print(f"""
Dear {member_name}, thank you for checking out '{book_title}'.
It  is due back in {due_days} days. Happy reading!
""")

generate_checkout_message("Catcher in the Rye", "Jonathon")
