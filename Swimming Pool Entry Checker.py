
age = int(input("How old are you? "))
swim = input("Can you swim? (yes / no): ").strip().lower()
adult = input("Is an adult with you? (yes / no): ").strip().lower()

print()
print("--- Pool Safety Decision ---")
print("Age:", age)

if age <= 4:
    group = "Toddler"
elif age <= 12:
    group = "Child"
elif age <= 18:
    group = "Teen"
else:
    group = "Adult"

print("Age group:", group)

if swim == "yes" and adult == "yes":
    print("Deep pool -> you can swim and an adult is with you.")
if age >= 12 or swim == "no":
    print("Shallow pool -> Stay in the shallow end.")
if age < 12 and swim == "no":
    print("Shallow pool -> Stay in the shallow end.")
if not adult == "yes":
    print("No adult with you -> call the lifeguard.")
if swim != "yes" and swim != "no":
    print("Input error. Please answer the swimming question with yes or no.")