marks = [95, 85, 75, 55, 35]
# print(marks[-4])
# print(marks[0:2])

marks.append(100)
marks.insert(0, 99)

# for score in marks:
#     print(score)

# print(99 in marks)

# print(len(marks))
i = 0
while i < len(marks):
    print(marks[i])
    i += 1

    marks.clear()
    print(marks)