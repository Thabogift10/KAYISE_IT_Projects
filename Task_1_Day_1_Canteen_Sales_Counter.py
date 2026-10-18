# TASK 1: Canteen Sales Counter
# Topics: while, for/range, break/stop condition, continue, counters, totals

print("=== Canteen Sales Counter ===")

item_count = 0
total_sales = 0.0

while True:
    price_text = input("Enter item price (enter 0 to finish): ")

    price = int(price_text)

    if price == 0:
        break
    elif price < 0:
        print("Price cannot be negative")
        continue
    else:
        item_count += 1
        total_sales += price
        print(f'Items:{item_count} : Total sales:{total_sales}')
for i in range(3):
    print("Thanks for using the cantee counter") 
    # TODO 1: Convert price_text to a number and store it in price

    # TODO 2: If price is 0, stop the loop

    # TODO 3: If price is negative, display a message and use continue

    # TODO 4: Increase item_count by 1 for a valid price

    # TODO 5: Add price to total_sales

# TODO 6: Display item_count and total_sales

# TODO 7: Use for and range() to print "Thank you for using the canteen counter"
#          three times
