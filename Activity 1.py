def calculate_change(paid, price):
    change = paid - price
    return change

snack_price = 25
print("===== SNACK VENDING MACHINE =====")
print(f" This Snack Costs {snack_price} units!")
print("Accepted coins are 1, 5, 10, 25!\n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert a coin (1, 5, 10, 25): "))

    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin Try again!\n")
        continue

    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted}\n")

    if total_inserted >= snack_price:
        print("Enough money inserted!\n")
        break

change_due = calculate_change(total_inserted, snack_price)

print("Dispensing your snack...")

if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units")

print("\n===== PURCHASE SUMMARY =====")
print("Snack price:", snack_price)
print("Coins inserted:", coins_inserted)
print("Total paid:", total_inserted)
print("Change Given:", change_due)
print("==============================")
print("Thank you for your purchase!")