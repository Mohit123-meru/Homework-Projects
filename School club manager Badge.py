name = input ("what is your name?")
club = input ("what is your Club's name")
number = 6
points = 3.75
he_is_active = True
print ("name is a:", type(name))
print ("club is a:",type(club))
print ("numbet is an:",type(number))
print ("points is a:",type(points))
print ("he_is_active is a",type(he_is_active)) 
print ("Your club name is: ",club) 
badge_code = name[0:3:1] + club[-1]
print (badge_code, "is your Badge code")
print ("==========Club Member===========")
print ("Member:" + name)
print ("club:" + club)
print ("Code:" + badge_code)
point = str (points)
he = str (he_is_active)
print ("points:" + point + " | " + he)