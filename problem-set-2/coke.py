def main():
    coke_price = 50
    amount_due = coke_price
    paid = 0
    change_due = 0

    while amount_due > 0:
        print("Amount Due:", amount_due)
        payment = int(input("Insert Coin:"))

        if payment == 5 or payment == 10 or payment == 25:
            paid = paid + payment
        else:
            continue

        amount_due = amount_due - payment
        change_due = paid - coke_price

    if change_due >= 0:
        print("Change Owed:", change_due)


main()
