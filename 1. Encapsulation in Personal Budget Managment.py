# Task 1
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

# Task 2
    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, category_name):
        self.__category_name = category_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
            self.__remaining_budget = allocated_budget  
        else:
            print("Sorry an error has occured. Your balance must be positive.")

# Task 3
    def get_remaining_budget(self):
        return self.__remaining_budget

    def add_expense(self, expense_amount):
        if expense_amount > 0:
            if expense_amount <= self.__remaining_budget:
                self.__remaining_budget -= expense_amount
                print(f"Expense of {expense_amount} added to {self.__category_name}.")
            else:
                print("Sorry your expense exceeds the remaining budget.")
        else:
            print("Sorry an expense amount must be a positive number.")

# Task 4
    def display_budget_details(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: {self.__allocated_budget}")
        print(f"Remaining Budget: {self.__remaining_budget}")


if __name__ == "__main__":
    food_budget = BudgetCategory("Food", 500)

    food_budget.display_budget_details()

    food_budget.add_expense(50)

    food_budget.display_budget_details()

    food_budget.set_allocated_budget(-100)  # Should display an error

    food_budget.add_expense(-20)  # Should display an error
