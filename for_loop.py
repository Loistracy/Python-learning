# for item in ["mash","john","sera"]:
#  print(item)

# for item in range(5,10,2):
#    print(item)

# for x in range(4):
#     for y in range(3):
#        print(f"({x}, {y})")


numbers = [5, 2 , 5 ,2 ,2]
for item in numbers:
    output = ""
    for count in range(item):
            output += "X"
    print(output)