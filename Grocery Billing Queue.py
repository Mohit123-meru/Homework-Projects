print("=== Grocery Billing Queue ===\n")
low = 0
medium = 0
high = 0
customers = 0
sales = 0
billing = True

while billing:
    name = input("Enter customer name: ")
    count = int(input("Enter number of items: "))

    if count <= 0:
        print("Invalid number")
        continue

    total = 0
    number = 1

    while number <= count:
        name = input("Enter item name: ")
        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        if price <= 0 or quantity <= 0:
            print("Invalid input")
            continue

        item = price * quantity
        print(name, ":", quantity, "x", price, "=", item)
        total = total + item

        if price < 50:
            low = low + quantity
        elif price <= 100:
            medium = medium + quantity
        else:
            high = high + quantity

        item = item + 1

    customers = customers + 1
    sales = sales + total
    print("Customer total:", total)

    next = input("Next customer? (yes/no): ")
    if next != "yes":
        billing = False

print("Daily report")
for name, count in [("Low", low), ("Medium", medium), ("High", high)]:
    print(name, ":", end=" ")
    for i in range(count):
        print("*", end="")
    print()

print("Customers served:", customers)
print("Total sales:", sales)