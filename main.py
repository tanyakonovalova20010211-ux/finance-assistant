from models.transaction import Transaction

# Пример использования
if __name__ == "__main__":
    t1 = Transaction(100, "Food", "2023-10-25")
    print(t1)

from models.transaction import Transaction
from models.category import Category

if __name__ == "__main__":
    food_cat = Category("Food", "Расходы на еду")
    t1 = Transaction(100, food_cat, "2023-10-25")
    print(t1)

from models.transaction import Transaction

if __name__ == "__main__":
    t1 = Transaction(100, "Food", "2023-10-25", "expense")
    t2 = Transaction(500, "Salary", "2023-10-26", "income")

    print(t1)
    print("Это расход?", t1.is_expense())
    print("Сумма со знаком:", t1.get_amount_with_sign())

    print(t2)
    print("Это расход?", t2.is_expense())
    print("Сумма со знаком:", t2.get_amount_with_sign())