homework = int(input("Enter homework time in minutes: "))
if homework > 60:
    plan = "start homework now"
    print("That is a long homework session.")
else:
    plan = "finish homework quickly"
    print("That is a short homework session.")
time = input("Is there free time after homework? (yes/no): ")
if time == "yes":
    print("Remember to pick a hobby!")

print("=== Daily Plan ===")
print("Homework minutes:", homework)
print("Plan:", plan)
print("Free time:", time)