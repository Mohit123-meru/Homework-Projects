print("--- Grocery cost comparision tool ---")

rice = 16
milk = 5
fruit = 10
baskets = 15
family = 29

cost = ((rice + milk + fruit) * baskets) / family
print("Basket cost per person:", cost)

total = int(input("Enter total items: "))
people = int(input("Enter number of people: "))

if people == 0:
    print("You cannot share between 0 people.")
else:
    remainder = total % people

    if remainder == 0:
        print("Items divide equally.")
        print("Each person gets:", total // people)
    else:
        print("Items do not divide equally.")
        print("Remainder:", remainder)

r_average = 65
total_weeks = 4
wrong_week_cost = 50
correct_week_cost = 80

total_cost = r_average * total_weeks
c_total = total_cost - wrong_week_cost + correct_week_cost
c_average = c_total / total_weeks

print("Recorded average:", r_average)
print("Corrected average:", c_average)
print("Corrected total:", c_total)

store_a_average = 70
store_b_average = 75
store_c_average = 80

v = c_average < store_a_average and c_average < store_b_average and c_average < store_c_average

print("Basket cost per person:", cost)
print("Corrected average:", c_average)
print("Verdict:", v)