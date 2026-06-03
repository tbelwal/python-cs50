def main():
    fruit_name = input("Item: ").title()
    calories = get_cals(fruit_name)
    if calories is not None:
        print("Calories:", calories)


def get_cals(f):
    fruit_calories = {
        "Apple": 130,
        "Avocado": 50,
        "Sweet Cherries": 100,
        "Kiwifruit": 90,
    }
    if f in fruit_calories:
        return fruit_calories[f]


main()
