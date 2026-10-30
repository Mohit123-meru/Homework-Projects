t1 = 135
t2 = 110
t3 = 99
t4 = 125
t5 = 195

total = t1 + t2 + t3 + t4 + t5
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