class Transaction:
    """Класс для представления финансовой транзакции."""

    def __init__(self, amount, category, date, type='expense'):
        self.amount = amount          # сумма
        self.category = category      # категория, например "Food"
        self.date = date              # дата
        self.type = type              # 'income' или 'expense'

    def __repr__(self):
        return f"Transaction({self.amount}, {self.category}, {self.date})"