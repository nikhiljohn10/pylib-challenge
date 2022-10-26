class Cart:
    items = []
    taxPercent = 18.00
    total_value = 0
    tax = 0
    cart_total = 0

    def __str__(self):
        if self.cart_total == 0:
            return "Nothing in cart"
        _cart = "\nCart:\n\n"
        for id, item in enumerate(self.items):
            _cart += f"  {id+1}. {item['name']} - Rs. {item['price']}\n"
        _cart += f"\n    Total:\t\tRs. {self.total_value}\n"
        _cart += f"    Tax ({self.taxPercent}%):\tRs. {self.tax}\n"
        _cart += "    ------------------------"
        _cart += "".join(["-" for _ in range(len(str(self.cart_total)))])
        _cart += f"\n    Grand Total:\tRs. {self.cart_total}\n"
        return _cart

    def total(self):
        if len(self.items) < 1:
            return 0
        self.total_value = sum([item["price"] for item in self.items])
        return self.total_value

    def get_tax(self):
        self.tax = round(self.total_value * self.taxPercent / 100, 2)
        return self.tax

    def calc_total(self):
        self.cart_total = self.total() + self.get_tax()

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})
        self.calc_total()

    def clear_cart(self):
        self.items = []
        self.total_value, self.tax, self.cart_total = 0, 0, 0
