#X = 10
#X -= 3
#print(X)

#X = 10 + 3 * 2
#print(X)

#X = 2.9
#print(abs(-X))

# import math
# print(math.floor(2.9))


import math


weight = float(input("weight:"))
convert= input("(L)bs or (K)g:")
pound = 2.20462
kilogram = float(weight * pound)
lbs = float(weight / pound)

if convert.lower() == "k":
  print(f"you are {kilogram} pounds")

elif convert.lower()== "l":
      print(f"you are {lbs} pounds")

else:
    print("invalid choice")