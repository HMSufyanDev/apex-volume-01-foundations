class Project:

    VALID_STATUSES = {
        "Planning",
        "In Progress",
        "Completed",
        "Cancelled"
    }

    def __init__(self, name, budget, client):
        self.name = name
        self._budget = budget
        self.client = client
        self.status = "Planning"
        self.invoices = []

    @property
    def budget(self):
        return self._budget
    @budget.setter
    def budget(self, value):
        if value < 0:
            raise ValueError("Error: Value cannot be negative")
        self._budget = value

    def update_status(self, status):
        if status not in self.VALID_STATUSES:
            raise ValueError(
                f"Invalid project status: {status}"
            )

        self.status = status

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def get_total_invoiced(self):
        return sum(
            invoice.amount
            for invoice in self.invoices
        )

    def get_paid_revenue(self):
        return sum(
            invoice.amount
            for invoice in self.invoices
            if not invoice.is_outstanding()
        )

    def get_outstanding(self):
        return sum(
            invoice.amount
            for invoice in self.invoices
            if invoice.is_outstanding()
        )

    def __str__(self):
        return f"{self.name} - ${self.budget:,.2f} - {self.status}"