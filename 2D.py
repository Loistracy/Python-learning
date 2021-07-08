# # matrix = [
# #  [1, 2, 3],
# #  [4, 5, 6],
# #  [7, 8, 9]
# # ]
# # # print(matrix[0][1])

# # for row in matrix:
# #     for item in row:
# #         print(item)

# numbers = [5, 2, 1, 7, 4]
# # numbers.append(20)
# print(50 in numbers)
# print(numbers.count())
# print(numbers.sort())
# # print(numbers)

numbers = [5, 6, 7, 8, 9, 5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)