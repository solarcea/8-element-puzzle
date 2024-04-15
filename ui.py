import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("530x500")
win.title("Пазл IQ (Дамба)")
win.minsize(530, 500)

l1 = ["Круг", "Ромб", "Квадрат", "Рыба"]
l2 = ["Py", "En"]

line1 = []
line2 = []
el11 = None
el12 = None
el13 = None
el14 = None
el21 = None
el21 = None
el23 = None
el24 = None

def remember():
    print(combo1.get(), combo2.get(), combo3.get(), combo4.get())
    print(combo5.get(), combo6.get(), combo7.get(), combo8.get())
    global el11
    global el12
    global el13
    global el14
    global el21
    global el22
    global el23
    global el24
    if combo1.get() == "Круг":
        el11 = 1;
    if combo1.get() == "Ромб":
        el11 = 2;
    if combo1.get() == "Квадрат":
        el11 = 3;
    if combo1.get() == "Рыба":
        el11 = 4;
    if combo2.get() == "Круг":
        el12 = 1;
    if combo2.get() == "Ромб":
        el12 = 2;
    if combo2.get() == "Квадрат":
        el12 = 3;
    if combo2.get() == "Рыба":
        el12 = 4;
    if combo3.get() == "Круг":
        el13 = 1;
    if combo3.get() == "Ромб":
        el13 = 2;
    if combo3.get() == "Квадрат":
        el13 = 3;
    if combo3.get() == "Рыба":
        el13 = 4;
    if combo4.get() == "Круг":
        el14 = 1;
    if combo4.get() == "Ромб":
        el14 = 2;
    if combo4.get() == "Квадрат":
        el14 = 3;
    if combo4.get() == "Рыба":
        el14 = 4;
    if combo5.get() == "Круг":
        el21 = 1;
    if combo5.get() == "Ромб":
        el21 = 2;
    if combo5.get() == "Квадрат":
        el21 = 3;
    if combo5.get() == "Рыба":
        el21 = 4;
    if combo6.get() == "Круг":
        el22 = 1;
    if combo6.get() == "Ромб":
        el22 = 2;
    if combo6.get() == "Квадрат":
        el22 = 3;
    if combo6.get() == "Рыба":
        el22 = 4;
    if combo7.get() == "Круг":
        el23 = 1;
    if combo7.get() == "Ромб":
        el23 = 2;
    if combo7.get() == "Квадрат":
        el23 = 3;
    if combo7.get() == "Рыба":
        el23 = 4;
    if combo8.get() == "Круг":
        el24 = 1;
    if combo8.get() == "Ромб":
        el24 = 2;
    if combo8.get() == "Квадрат":
        el24 = 3;
    if combo8.get() == "Рыба":
        el24 = 4;
    global line1
    global line2
    line1 = [el11, el12, el13, el14]
    line2 = [el21, el22, el23, el24]
    print(line1)
    print(line2)


count = 0
setline1 = set(line1)
setline2 = set(line2)

stepcount = 0
sequence = ""
solution = ""
a = [1, 2, 3, 4]
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

def solve():
    variable = 0
    linesolution = []

    timestart = perf_counter()

    while variable <= 999:
        global line1
        global line2
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
        global sequence
        if len(sequence) <= 35:
            linesolution.append(sequence)
        sequence = ""
        line1 = [el11, el12, el13, el14]
        line2 = [el21, el22, el23, el24]
    global solution
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
        textbox.insert(tk.INSERT,"Решение правильное" + '\n')

def copypaste():
    global solution
    # print(str(combolang))
    if combolang.get() == "Py":
        for aa in solution:
            if aa == "x":
                # print("Поверните левый вентиль один раз")
                textbox.insert(tk.INSERT,"Поверните левый вентиль один раз" + '\n')
            if aa == "y":
                # print("Поверните вентиль посередине один раз")
                textbox.insert(tk.INSERT, "Поверните вентиль посередине один раз" + '\n')
            if aa == "z":
                # print("Поверните правый вентиль один раз")
                textbox.insert(tk.INSERT, "Поверните правый вентиль один раз" + '\n')
            if aa == " ":
                continue
    else:
        for aa in solution:
            if aa == "x":
                # print("Turn the left valve once")
                textbox.insert(tk.INSERT, "Turn the left valve once" + '\n')
            if aa == "y":
                # print("Turn the middle valve once")
                textbox.insert(tk.INSERT, "Turn the middle valve once" + '\n')
            if aa == "z":
                # print("Turn the right valve once")
                textbox.insert(tk.INSERT, "Turn the right valve once" + '\n')
            if aa == " ":
                continue

combo1 = ttk.Combobox(win, values=l1, width=10)
combo2 = ttk.Combobox(win, values=l1, width=10)
combo3 = ttk.Combobox(win, values=l1, width=10)
combo4 = ttk.Combobox(win, values=l1, width=10)
combo5 = ttk.Combobox(win, values=l1, width=10)
combo6 = ttk.Combobox(win, values=l1, width=10)
combo7 = ttk.Combobox(win, values=l1, width=10)
combo8 = ttk.Combobox(win, values=l1, width=10)

combolang = ttk.Combobox(win, values=l2, width=6)

label_1 = tk.Label(win, text="Выбери элементы", pady=10)
label_1.grid(row=0, column=0, columnspan=4, stick="we")

combo1.grid(row=1, column=0)
combo2.grid(row=1, column=1)
combo3.grid(row=1, column=2)
combo4.grid(row=1, column=3)
combo5.grid(row=2, column=0)
combo6.grid(row=2, column=1)
combo7.grid(row=2, column=2)
combo8.grid(row=2, column=3)

ttk.Button(win,text="Записать", command=remember).grid(row=3, column=1, columnspan=2, pady=10, stick="we")
ttk.Button(win,text="Решить", command=solve).grid(row=4, column=1, columnspan=2, pady=5, stick="we")

label_lang = tk.Label(win, text="Выбери язык пасты")
label_lang.grid(row=5, column=0, stick="w", padx=10, columnspan=2)
combolang.grid(row=5, column=1, pady=10)
ttk.Button(win,text="Паста", command=copypaste).grid(row=6, column=1, columnspan=2, stick="we")

from tkinter import Text
textbox = Text(win, width= 40, height= 10, font=("Helvetica", 16))
textbox.grid(row = 7, column = 0, columnspan = 4, padx=20)

win.mainloop()
