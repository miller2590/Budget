from user import User

name = input("Enter name: ").capitalize()
user = User(name)

user_options = input("Enter 'a', to add a category.\n"
                     "Enter 'u', to update an expense in an existing category.\n"
                     "Enter 'd' to delete an expense\n"
                     "Enter 'l' to list expenses or,\n"
                     "'q' to quit.\n"
                     "Enter here: ").lower()

while user_options != 'q':
    if user_options == 'a':
        category_name = input("Enter expense category: ").capitalize()
        expense_amount = input("Enter expense: ")
        user.add_category(category_name)
        user.update_expense(category_name, expense_amount)
    elif user_options == 'u':
        category_name = input("Enter category of expense you wish to update: ").capitalize()
        expense_amount = input("Enter expense: ")
        user.update_expense(category_name, expense_amount)
    elif user_options == 'd':
        expense_category = input("Enter category of expense you wish to delete: ").capitalize()
        user.delete_expense(expense_category)
    elif user_options == 'l':
        print(user, user.list_expenses())

    user_options = input("Enter 'a', to add a category.\n"
                         "Enter 'u', to update an expense in an existing category.\n"
                         "Enter 'd' to delete an expense\n"
                         "Enter 'l' to list expenses or,\n"
                         "'q' to quit.\n"
                         "Enter here: ").lower()
