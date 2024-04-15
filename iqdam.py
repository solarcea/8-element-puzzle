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

stepcount = 0
sequence = ""
a = [1, 2, 3, 4]
x = "0"
y = "0"
z = "0"

if line1 != a or line2 != a:
    print("Непорядок")
    inp = input('Выбери рычаг для прокрутки (x, y, z): ')
    while inp == "x" or "y" or "z": #без этого программа ловит инпут и идет дальше
             if inp == "x":
                        x += "x" #крутим первый квадрат
                        print("Крутим Х")
                        stepcount += 1
                        sequence += "x "
                        line1.insert(0, line2[0])
                        line1.insert(1, line1[1])
                        line2.insert(0, line2[1])
                        line2.insert(1, line1[3])
                        line1.pop(2)
                        line1.pop(2)
                        line2.pop(2)
                        line2.pop(2)
                        print(line1)
                        print(line2)
                        if line1 == a and line2 == a:
                            print("Ходов для решения", stepcount)
                            print("Порядок: ", sequence)
                            break
                        inp = input("Какой дальше? ")
                        if inp == "exit":
                            break
             elif inp == "y":
                        y += "y" #крутим второй квадрат
                        print("Крутим Y")
                        stepcount += 1
                        sequence += "y "
                        line1.insert(1, line2[1])
                        line1.insert(2, line1[2])
                        line2.insert(1, line2[2])
                        line2.insert(2, line1[4])
                        line1.pop(3)
                        line1.pop(3)
                        line2.pop(3)
                        line2.pop(3)
                        print(line1)
                        print(line2)
                        if line1 == a and line2 == a:
                            print("Ходов для решения", stepcount)
                            print("Порядок: ", sequence)
                            break
                        inp = input("Какой дальше? ")
                        if inp == "exit":
                            break
             elif inp == "z":
                        z += "z" #крутим третий квадрат
                        print("Крутим Z")
                        stepcount += 1
                        sequence += "z "
                        line1.insert(2, line2[2])
                        line1.insert(3, line1[3])
                        line2.insert(2, line2[3])
                        line2.insert(3, line1[5])
                        line1.pop(4)
                        line1.pop(4)
                        line2.pop(4)
                        line2.pop(4)
                        print(line1)
                        print(line2)
                        if line1 == a and line2 == a:
                            print("Ходов для решения", stepcount)
                            print("Порядок: ", sequence)
                            break
                        inp = input("Какой дальше? ")
                        if inp == "exit":
                            break
             elif inp != "x" or "y" or "z":
                 print("Нет рычага")
                 inp = input("Давай еще раз (x, y, z)։")
                 if inp == "exit":
                     break
else:
    print("Уже сделано")