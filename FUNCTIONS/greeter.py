def greet_user(user_age,user_name):
    """Display."""
    print(f"Hello, {user_name.title()}!. Age: {user_age}")


name = input("Name: ")
age = input("Age: ")
greet_user(user_name=name,user_age=age)

