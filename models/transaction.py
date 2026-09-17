class Transaction:
    """Класс для представления финансовой транзакции."""

    def __init__(self, amount, category, date, type='expense'):
        self.amount = amount          # сумма
        self.category = category      # категория, например "Food"
        self.date = date              # дата
        self.type = type              # 'income' или 'expense'

    def __repr__(self):
        return f"Transaction({self.amount}, {self.category}, {self.date})"

class Transaction:
    """Класс для представления финансовой транзакции."""

    def __init__(self, amount, category, date, type='expense'):
        self.amount = amount
        self.category = category
        self.date = date
        self.type = type  # 'income' или 'expense'

    def is_expense(self):
        """Возвращает True, если это расход."""
        return self.type == 'expense'

    def get_amount_with_sign(self):
        """Сумма со знаком: расходы — минус, доходы — плюс."""
        if self.type == 'income':
            return self.amount
        else:
            return -self.amount

    def __repr__(self):
        return f"Transaction({self.amount}, {self.category}, {self.date}, {self.type})"
