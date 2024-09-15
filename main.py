# maker: pouria rezaie
# این فایل برای اجرای اصلی برنامه است.
from budget import BudgetManager, Income, Expense
from database import Database

def main():
    db = Database()  # ایجاد اتصال به دیتابیس
    manager = BudgetManager()  # ایجاد مدیر بودجه

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            # گرفتن ورودی برای درآمد
            amount = float(input("Enter income amount: "))
            source = input("Enter income source: ")
            income = Income(amount, source)  # ایجاد شیء درآمد
            manager.add_income(income)  # اضافه کردن به مدیریت بودجه
            db.add_income(amount, source)  # ذخیره در دیتابیس

        elif choice == '2':
            # گرفتن ورودی برای هزینه
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            expense = Expense(amount, category)  # ایجاد شیء هزینه
            manager.add_expense(expense)  # اضافه کردن به مدیریت بودجه
            db.add_expense(amount, category)  # ذخیره در دیتابیس

        elif choice == '3':
            # نمایش خلاصه بودجه
            manager.show_summary()

        elif choice == '4':
            # خروج از برنامه
            db.close()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if name == "__main__":
    main()