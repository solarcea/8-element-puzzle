# В игре Island Hoppers есть головоломка, в которой две трубы стоят рядом
# У каждой трубы по 4 элемента - всего 8
# Рядом с трубами есть 3 вентиля, которые крутят 4 элемента по квадратам
# 1 вентиль - элементы 1,2 обеих труб
# 2 вентиль - элементы 2,3 обеих труб
# 3 вентиль - элементы 3,4 обеих труб
# Программа позволяет ввести текущую позицию труб и методом случайного перебора найти решение

el11 = int(input("Линия 1, элемент 1: "))
el12 = int(input("Линия 1, элемент 2: "))
el13 = int(input("Линия 1, элемент 3: "))
el14 = int(input("Линия 1, элемент 4: "))
el21 = int(input("Линия 2, элемент 1: "))
el22 = int(input("Линия 2, элемент 2: "))
el23 = int(input("Линия 2, элемент 3: "))
el24 = int(input("Линия 2, элемент 4: "))
line1 = [el11, el12, el13, el14]
line2 = [el21, el22, el23, el24]
print(line1)
print(line2)

count = 0
setline1 = set(line1)
setline2 = set(line2)

stepcount = 0
sequence = ""
a = [1, 2, 3, 4]
b: list[int] = [6, 8, 10, 12, 14]
x = "0"
y = "0"
z = "0"


def rotate_x():
    global x
    x += "x"  # крутим первый квадрат
    # print("Крутим Х")
    global stepcount
    stepcount += 1
    global sequence
    sequence += "x "
    line1.insert(0, line2[0])
    line1.insert(1, line1[1])
    line2.insert(0, line2[1])
    line2.insert(1, line1[3])
    line1.pop(2)
    line1.pop(2)
    line2.pop(2)
    line2.pop(2)

def rotate_y():
    global y
    y += "y"  # крутим второй квадрат
    # print("Крутим Y")
    global stepcount
    stepcount += 1
    global sequence
    sequence += "y "
    line1.insert(1, line2[1])
    line1.insert(2, line1[2])
    line2.insert(1, line2[2])
    line2.insert(2, line1[4])
    line1.pop(3)
    line1.pop(3)
    line2.pop(3)
    line2.pop(3)

def rotate_z():
    global z
    z += "z"  # крутим третий квадрат
    # print("Крутим Z")
    global stepcount
    stepcount += 1
    global sequence
    sequence += "z "
    line1.insert(2, line2[2])
    line1.insert(3, line1[3])
    line2.insert(2, line2[3])
    line2.insert(3, line1[5])
    line1.pop(4)
    line1.pop(4)
    line2.pop(4)
    line2.pop(4)

import random
from time import perf_counter


variable = 0
linesolution = []

timestart = perf_counter()

while variable <= 999:
    while line1 != a or line2 != a:
        randomlist = [1, 2, 3]
        rnd = random.choice(randomlist)
        if rnd == 1:
            rotate_x()
        elif rnd == 2:
            rotate_y()
        elif rnd == 3:
            rotate_z()
    variable += 1
    if len(sequence) <= 35:
        linesolution.append(sequence)
    sequence = ""
    line1 = [el11, el12, el13, el14]
    line2 = [el21, el22, el23, el24]

solution = min(linesolution)
print(solution)
timestop = perf_counter()
print(timestop - timestart)
print("Готово")

print("Проверка")
print(line1)
print(line2)
line1 = [el11, el12, el13, el14]
line2 = [el21, el22, el23, el24]
for i in solution:
    if i == "x":
        rotate_x()
    if i == "y":
        rotate_y()
    if i == "z":
        rotate_z()
    if i == " ":
        continue
if line1 == a and line2 == a:
    print(line1)
    print(line2)
    print("Решение правильное")

lang = str(input("Выбери язык для пасты (ru / en): "))
while lang != "ru" and "en":
    lang = str(input("Выбери язык для пасты (ru / en): "))

for i in solution:
    # print(i)
    if i == "x":
        if lang == "en":
            print("Turn the left valve once")
        else:
            print("Поверните левый вентиль один раз")
    if i == "y":
        if lang == "en":
            print("Turn the middle valve once")
        else:
            print("Поверните вентиль посередине один раз")
    if i == "z":
        if lang == "en":
            print("Turn the right valve once")
        else:
            print("Поверните правый вентиль один раз")
    if i == " ":
        continue
