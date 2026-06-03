# 1. Get item
# 2. Check price -> iggnore if not available -> prompt again
# 3. Add to total if proce exists
# 4. Exit on ctrl+d


def main():
    get_order()


def get_order():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    total = 0
    while True:
        try:
            item = input("Item: ").title()
        except EOFError:
            break
        else:
            price = menu.get(item)
            if price is not None:
                total += price
                print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
