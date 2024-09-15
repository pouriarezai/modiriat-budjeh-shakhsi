# maker: pouria rezaie
# این فایل مسئول مدیریت دیتابیس برای ذخیره اطلاعات درآمدها و هزینه‌هاست.
import sqlite3

class Database:
    def __init__(self, db_name="budget.db"):
        self.conn = sqlite3.connect(db_name)  # اتصال به دیتابیس یا ساختنش اگه نباشه
        self.cursor = self.conn.cursor()
        self.create_tables()  # ساخت جدول‌های لازم

    # این تابع جدول‌ها رو می‌سازه
    def create_tables(self):
        # جدول درآمدها
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS incomes (
                               id INTEGER PRIMARY KEY,
                               amount REAL NOT NULL,
                               source TEXT NOT NULL)''')

        # جدول هزینه‌ها
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                               id INTEGER PRIMARY KEY,
                               amount REAL NOT NULL,
                               category TEXT NOT NULL)''')
        self.conn.commit()  # ذخیره تغییرات

    # اضافه کردن درآمد به دیتابیس
    def add_income(self, amount, source):
        self.cursor.execute("INSERT INTO incomes (amount, source) VALUES (?, ?)", (amount, source))
        self.conn.commit()
        print(f"Income of {amount} from {source} added to the database.")

    # اضافه کردن هزینه به دیتابیس
    def add_expense(self, amount, category):
        self.cursor.execute("INSERT INTO expenses (amount, category) VALUES (?, ?)", (amount, category))
        self.conn.commit()
        print(f"Expense of {amount} for {category} added to the database.")

    # گرفتن کل درآمدها
    def get_incomes(self):
        self.cursor.execute("SELECT * FROM incomes")
        return self.cursor.fetchall()

    # گرفتن کل هزینه‌ها
    def get_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        return self.cursor.fetchall()

    # بستن اتصال به دیتابیس
    def close(self):
        self.conn.close()