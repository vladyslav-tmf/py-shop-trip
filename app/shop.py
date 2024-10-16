import datetime


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_product_cost(self, product_cart: dict) -> float:
        total_cost = 0
        for product, amount in product_cart.items():
            if product in self.products:
                total_cost += self.products[product] * amount
        return total_cost

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        print(
            f'\nDate: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
        )
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, amount in product_cart.items():
            cost = self.products[product] * amount
            formatted_cost = f"{cost:.1f}" if cost % 1 != 0 else f"{int(cost)}"  # noqa: E231, E501
            print(f"{amount} {product}s for {formatted_cost} dollars")
            total_cost += cost
        print(f"Total cost is {total_cost:.1f} dollars")  # noqa: E231
        print("See you again!\n")
