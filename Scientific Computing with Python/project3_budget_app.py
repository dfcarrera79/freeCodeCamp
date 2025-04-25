## Build a Budget App Project
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate the percentage spent for each category
    withdrawals = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        withdrawals.append(spent)
    
    total_spent = sum(withdrawals)
    percentages = [int((spent / total_spent) * 100) if total_spent != 0 else 0 for spent in withdrawals]
    
    # Build the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    
    # Add the horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # Get the longest category name
    max_length = max(len(category.name) for category in categories)
    
    # Add the category names vertically
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n"
    
    return chart