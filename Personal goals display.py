import keyword
name = input("Enter your name: ")
goal = input("Enter one skill you want to get better at: ")
target = input("Enter the month you want to reach it by: ")
daily_minutes = 30

print("\nMY PERSONAL GOAL PLAN\n")
print("Name:", name)
print("Goal:", goal)
print("Target month:", target)
print("Daily practice:", daily_minutes, "minutes")
print("Status: ", end="")
print("Not started")
print("Reminder: - ", end="")
print("Practise every day!")
print("In one sentence:")
print(name, "will practise", goal, "for", daily_minutes, "minutes every day until", target + ".")
print(keyword.kwlist)

