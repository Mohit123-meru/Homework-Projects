homework = int(input("Enter homework time in minutes: "))
if homework > 60:
    plan = "start your homework"
    print("That is a long time for homework.")
else:
    plan = "Complete your homework quickly"
    print("That is a short time for homework.")
time = input("Do you have free time after finishing your homework? (yes/no): ")
if time == "yes":
    print("Remember to play outside with your friends! They must be waiting.")

print("=== Daily Plan ===")
print("Homework minutes:", homework)
print("Plan:", plan)
print("Free time:", time)