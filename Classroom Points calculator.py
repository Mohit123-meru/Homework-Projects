team1 = 120
team2 = 95
team3 = 140
team4 = 110
team5 = 85
total = team1 + team2 + team3 + team4 + team5
avg = total / 5

print("Total points :", total)
print("Average per team :", avg)
stars = 2
reward = total * stars

print("Total reward stars :", reward)
boxes = reward // 25
leftover = reward % 25

print("Full boxes packed :", boxes)
print("Leftover stars :", leftover)
week = 500
print("Better than last week? :", total > week)
print("Same as last week? :", total == week)
print("At least as good? :", total >= week)
total += 30
print("After bonus points :", total)
total -= 15
print("After missed tasks :", total)
rewards = total * stars
boxes = rewards // 25
print("Final boxes packed :", boxes)