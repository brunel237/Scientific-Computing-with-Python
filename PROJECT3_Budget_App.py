# PROJECT 3 : BUDGET APP


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        name_len = len(self.name)
        len_left = 30 - name_len
        left_pad = len_left // 2
        right_pad = 30 - (left_pad+name_len)
        first_line = f"{''.join(['*' for _ in range(left_pad)])}{self.name}{''.join(['*' for _ in range(right_pad)])}\n"
        items_string = ""
        for items in self.ledger:
            amount, description = f"{items['amount']:.2f}", items['description']
            if len(description) > 23:
                description = description[:23]
            if len(amount) > 7:
                amount = amount[:7]
            space_len = 30 - (len(description) + len(amount))
            items_string += f"{description}{''.join([' ' for _ in range(space_len)])}{amount}\n"
        last_line = f"Total: {self._get_balance()}"
        return first_line + items_string + last_line

    def _deposit(self, amount, description=""):
        self.ledger.append(
            {
                'amount': amount,
                'description': description
            }
        )

    def _withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append(
                {
                    'amount': -amount,
                    'description': description
                }
            )
            return True
        return False

    def _transfer(self, amount, category):
        if self._withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def _get_balance(self):
        return sum(map(lambda ledger: ledger['amount'], self.ledger))

    def _check_funds(self, amount):
        current_balance = self.get_balance()
        if amount > current_balance:
            return False
        return True

    def deposit(self, amount, description=""):
        self._deposit(amount, description)

    def withdraw(self, amount, description=""):
        return self._withdraw(amount, description)

    def transfer(self, amount, category):
        return self._transfer(amount, category)

    def get_balance(self):
        return self._get_balance()

    def check_funds(self, amount):
        return self._check_funds(amount)
    
    def total_spent(self):
        return sum(map(lambda ledger: abs(ledger['amount']) if ledger['amount'] < 0 else 0, self.ledger))


def create_spend_chart(categories):
    categories_names = list(map(lambda category: category.name, categories)) 
    amounts_spent = list(map(lambda category: category.total_spent(), categories))

    # dictionnary to represent our bar chart
    bar_chart = {bar: [' ' for _ in range(len(categories))] for bar in range(100, -1, -10)}

    # calculating and rounding percentage of each category
    percentage_list = [ 
        int(((val / sum(amounts_spent)) * 100)/ 10) * 10 for val in amounts_spent
    ]

    # assigning 'o' to corresponding categories percetage
    for each_amount in range(len(amounts_spent)):
        for percentage in range(percentage_list[each_amount], -1, -10):
            bar_chart[percentage][each_amount] = 'o'
    
    chart_string = "Percentage spent by category\n"

    # adding each of the bar chart with the corresponding value
    for item in range(100, -1, -10):
        chart_string += f"{''.join([' ' for _ in range(3 - len(str(item)))]) +str(item)}| {''.join([val+'  ' for val in bar_chart[item]])}\n"
    
    # adding horizontal line
    chart_string += f"    {''.join(['-' for _ in range(len(amounts_spent)*3 +1) ])}"
    
    # writing categories names vertically
    for size in range(max([len(name) for name in categories_names])):
        temp_string = ""
        for char in range(len(categories_names)):
            try:
                val = categories_names[char][size]
            except IndexError:
                val = ' '
            temp_string += f"{val}  "
        chart_string += f"\n     {temp_string}"
    return chart_string

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
market = Category("Market")
market.deposit(500, market)
market.withdraw(100, 'make up')
market.withdraw(90, 'shoes')
food.transfer(50, clothing)
clothing.withdraw(12.11, 'school dresses')
clothing.withdraw(35.11, 'school dresses')
print(create_spend_chart([food,clothing, market]))