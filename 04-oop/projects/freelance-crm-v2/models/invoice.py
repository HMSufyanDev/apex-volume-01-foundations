class Invoice:

    def __init__(self, invoice_id, amount):
        self.invoice_id = invoice_id
        self._amount = amount
        self.status = "unpaid"

    def mark_paid(self):
        self.status = "paid"

    def mark_unpaid(self):
        self.status = "unpaid"

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Error: Value cannot be negative")
        self._amount = value

    def is_outstanding(self):
        return self.status == "unpaid"

    def __str__(self):
        return f"Invoice {self.invoice_id} - ${self.amount:,.2f} - {self.status}"