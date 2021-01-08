class User:
    def __init__(self, name):
        self.name = name
        self.expenses = {}

    def __repr__(self):
        return f'User: {self.name}'

    def add_category(self, category,):
        if category not in self.expenses:
            self.expenses[category] = 0

    def update_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] = amount

    def delete_expense(self, category):
        if category in self.expenses:
            self.expenses.pop(category, None)

    def list_expenses(self):
        return self.expenses
