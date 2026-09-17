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