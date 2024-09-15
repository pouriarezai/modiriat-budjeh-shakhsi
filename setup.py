from setuptools import setup, find_packages

setup(
    name='PersonalBudgetManagementSystem',
    version='0.1',
    description='سیستم مدیریت بودجه شخصی برای مدیریت درآمد، هزینه‌ها و وضعیت مالی.',
    author='پوریا رضایی کماسی',
    author_email='Pouriarezaie6587@gmail.com',
    packages=find_packages(),
    install_requires=[
        'sqlite3',  # اطمینان از نصب sqlite3
    ],
    entry_points={
        'console_scripts': [
            'budget-manager = main:main_function',  # نقطه ورودی را مطابق نیاز تنظیم کنید
        ],
    },
    include_package_data=True,
)