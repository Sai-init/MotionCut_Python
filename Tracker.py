import datetime

expenses = {}
categories = set()

def add_expenses(amount, description, category):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount should be positive.")
    except ValueError:
        print("Invalid amount entered. Enter valid amount.")
        return
    if not description:
        print("Description should not be empty.")
        return
    if category.strip() == "":
        category = "Uncategorized"
    if category not in expenses:
        expenses[category] = []
    expenses[category].append({"amount": amount, "description": description, "date": datetime.datetime.now().strftime("%Y-%m-%d")})

def monthly_expense_details(month, year):
    try:
        month = int(month)
        year = int(year)
    except ValueError:
        print("Invalid month or year.")
        return

    if month < 1 or month > 12:
        print("Invalid month. Month must be between 1 and 12.")
        return

    total_expense = 0
    monthly_expenses = {}
    for i, j in expenses.items():
        monthly_expenses[i] = 0
        for k in j:
            expense_date = datetime.datetime.strptime(k["date"], "%Y-%m-%d")
            if expense_date.month == month and expense_date.year == year:
                monthly_expenses[i] += k["amount"]
                total_expense += k["amount"]
    return total_expense, monthly_expenses

def category_details(category):
    category_expenses = []
    if category in expenses:
        for i in expenses[category]:
            category_expenses.append({"date": i["date"], "amount": i["amount"]})
        return category_expenses
    else:
        print("No expenses found for category:", category)
        return []

def user_details():
    amount = input("Enter amount spent: ")
    description = input("Describe the expense: ")
    category = input("Enter expense category: ").strip()
    add_expenses(amount, description, category)

while True:
    user_details()
    next_expenses = input("Are you ready to add another expense? (yes/no): ").lower()
    if next_expenses != "yes":
        break

month = input("Enter month(1-12): ")
year = input("Enter year: ")

# Validate month and year
if not month.isdigit() or not year.isdigit():
    print("Month and year must be numbers.")
else:
    total_expense, monthly_expenses = monthly_expense_details(month, year)
    if total_expense:
        print("Total expense for", month, "/", year, ":", total_expense)
        print("Monthly expenses:", monthly_expenses)

    category = input("Enter category to get details: ")
    category_expenses = category_details(category)
    if category_expenses:
        for i in category_expenses:
            print("Date:", i["date"], "Amount:", i["amount"])
    else:
        print("No expenses found for category:", category)

