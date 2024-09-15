# maker: pouria rezaie
# این فایل شامل کلاس‌هایی برای مدیریت بودجه، درآمدها و هزینه‌هاست

class Income:
    # کلاس برای ذخیره اطلاعات مربوط به درآمد
    def __init__(self, amount, source):
        self.amount = amount  # مبلغ درآمد
        self.source = source  # منبع درآمد، مثلاً حقوق یا پروژه

    def __str__(self):
        return f"Income: {self.source}, Amount: {self.amount}"

class Expense:
    # کلاس برای ذخیره اطلاعات مربوط به هزینه
    def __init__(self, amount, category):
        self.amount = amount  # مبلغ هزینه
        self.category = category  # دسته‌بندی هزینه، مثلاً غذا، حمل و نقل

    def __str__(self):
        return f"Expense: {self.category}, Amount: {self.amount}"

class BudgetManager:
    # این کلاس برای مدیریت کلی بودجه استفاده می‌شه
    def __init__(self):
        self.incomes = []  # لیستی برای ذخیره درآمدها
        self.expenses = []  # لیستی برای ذخیره هزینه‌ها

    # اضافه کردن درآمد به لیست
    def add_income(self, income):
        self.incomes.append(income)
        print(f"Added income: {income}")

    # اضافه کردن هزینه به لیست
    def add_expense(self, expense):
        self.expenses.append(expense)
        print(f"Added expense: {expense}")

    # محاسبه بودجه‌ی باقی‌مانده
    def calculate_balance(self):
        total_income = sum(income.amount for income in self.incomes)
        total_expense = sum(expense.amount for expense in self.expenses)
        balance = total_income - total_expense
        return balance

    # نمایش گزارش کامل درآمدها و هزینه‌ها
    def show_summary(self):
        print("---- Budget Summary ----")
        print("Incomes:")
        for income in self.incomes:
            print(income)
        print("\nExpenses:")
        for expense in self.expenses:
            print(expense)
        print(f"\nRemaining balance: {self.calculate_balance()}")