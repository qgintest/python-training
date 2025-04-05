menu = ["pasta", "pizza", "salad"]

user_choice = input("Enter the index of the item: ")
user_choice_index = int(user_choice)

user_choice = menu[user_choice_index]
# user_choice = menu[user_choice_index]

# message = f"You chose {menu[user_choice]}."
print(f"You chose {user_choice}: {user_choice_index}.")


# Print out the item with that index
