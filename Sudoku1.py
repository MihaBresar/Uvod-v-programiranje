
from tkinter import *
from random import randint

resen_sudoku = []
sudoku1 = []
for i in range(9):
    resen_sudoku += [[0] * 9]
    sudoku1 += [[0] * 9]
x = 0
z = 0
y = 0
s = False


def je_veljavna(stevilo, vrstica, stolpec):

    for i in range(9):
        if resen_sudoku[vrstica][i] == stevilo:
            return False
        if resen_sudoku[i][stolpec] == stevilo:
            return False

    velikaVrstica = 3 * int(vrstica / 3)
    velikiStolpec = 3 * int(stolpec / 3)
    vrstica1 = (vrstica + 2) % 3
    vrstica2 = (vrstica + 4) % 3
    stolpec1 = (stolpec + 2) % 3
    stolpec2 = (stolpec + 4) % 3

    if resen_sudoku[vrstica1 + velikaVrstica][stolpec1 + velikiStolpec] == stevilo:
        return False
    if resen_sudoku[vrstica1 + velikaVrstica][stolpec2 + velikiStolpec] == stevilo:
        return False

    if resen_sudoku[vrstica2 + velikaVrstica][stolpec1 + velikiStolpec] == stevilo:
        return False

    if resen_sudoku[vrstica2 + velikaVrstica][stolpec2 + velikiStolpec] == stevilo:
        return False
    return True


def resi_sudoku(vrstica, stolpec):
    global s
    if s:
        return
    if vrstica == 8 and stolpec == 9:
        s = True
        return
    elif stolpec == 9:

        stolpec = 0
        vrstica += 1

    if resen_sudoku[vrstica][stolpec] != 0:
        resi_sudoku(vrstica, stolpec + 1)
        if s:
            return
    else:
        for i in range(1, 10):
            if je_veljavna(i, vrstica, stolpec):
                resen_sudoku[vrstica][stolpec] = i
                resi_sudoku(vrstica, stolpec + 1)
                if s:
                    return

        resen_sudoku[vrstica][stolpec] = 0


def resitelj4(vrstica, stolpec):
    if vrstica == 8 and stolpec == 9:
        global z
        z += 1
        print (z, 0)
        return
    elif stolpec == 9:

        stolpec = 0
        vrstica += 1

    if resen_sudoku[vrstica][stolpec] != 0:
        resitelj4(vrstica, stolpec + 1)
    else:
        for i in range(1, 10):
            if je_veljavna(i, vrstica, stolpec):
                sudoku1[vrstica][stolpec] = i
                resitelj4(vrstica, stolpec + 1)

        sudoku1[vrstica][stolpec] = 0


def napolni():
    # v prazno tabelo dodamo 30 števil
    for i in range(9):
        for j in range(9):
            sudoku1[i][j] = 0

    y = 0
    while y < 30:
        f = randint(0, 8)
        g = randint(0, 8)
        if sudoku1[f][g] == 0:
            sudoku1[f][g] = resen_sudoku[f][g]
            y += 1
    return sudoku1


def vrstica(resen_sudoku):
    # nakljucno zapolni prvo vrstico
    f = 0
    for i in range(9):
        for j in range(9):
            resen_sudoku[i][j] = 0
    while f < 9:
        t = randint(1, 9)
        if je_veljavna(t, 0, f):
            resen_sudoku[0][f] = t
            f += 1

    return resen_sudoku


def main1():
    # Ustvari nakljucen sudoku, tako da nakljucno permutira prvo vrstico.
    # Potem pa dano tabelo resi s pomocjo resi_sudoku
    x = 0
    z = 0
    y = 0
    s = False

    vrstica(resen_sudoku)
    resi_sudoku(0, 0)


def main2():
    # Funkcijo main1 ustvari resen 9x9 sudoku.
    # Sedaj v prazno tabelo dodamo 30 elementov, ce ima dana tabela enolicno esitev smo koncali.
    # Ce tabela nima enolicne resitve postopek ponovimo
    global s
    s = False
    main1()
    while True:
        global z
        napolni()
        resitelj4(0, 0)
        if z == 1:
            return [resen_sudoku, sudoku1]
        else:
            z = 0


m = main2()

resen_sudoku = m[0]
sudoku1 = m[1]


class Celica:

    def __init__(self, root, r, c):
        self.vrednost = StringVar()
        self.vhod = Entry(root, textvariable=self.vrednost, width=5)
        if r < 4 and (c < 3 or c > 5):
            self.vhod = Entry(root, textvariable=self.vrednost,
                              width=5, bg='orange')
        elif r > 6 and (c < 3 or c > 5):
            self.vhod = Entry(root, textvariable=self.vrednost,
                              width=5, bg='orange')
        elif r < 7 and r > 3 and c > 2 and c < 6:
            self.vhod = Entry(root, textvariable=self.vrednost,
                              width=5, bg='red')
        else:
            self.vhod = Entry(root, textvariable=self.vrednost, width=5)
        self.vhod.grid(row=r, column=c)

    def najdi_vrednost(self):
        if self.vhod.get() == '' or int(self.vhod.get()) < 1 \
            or int(self.vhod.get()) > 9:
            return 0

        return int(self.vhod.get())

    def dodaj_vrednost(self, v):
        self.vrednost.set(v)


class Application(Tk):

    def __init__(self):
        self.root = Tk()
        self.root.title('Igra Sudoku')

        self.resi = Button(self.root, text='Resi', command=self.resi_me)
        self.nova = Button(self.root, text='Nova igra', command=self.nova_igra)
        self.zacni = Button(self.root, text='Zacni', command=self.zacetek)
        self.preveri = Button(self.root, text='Preveri',
                              command=self.preveri)

        self.preveri.grid(row=10, column=7, columnspan=6)
        self.resi.grid(row=10, column=0, columnspan=3)
        self.nova.grid(row=10, column=2, columnspan=3)
        self.zacni.grid(row=10, column=4, columnspan=4)

        self.case = []
        for i in range(9):
            for j in range(9):
                self.case += [Celica(self.root, i + 1, j)]

    def nova_igra(self):
        global resen_sudoku
        global sudoku1
        m = main2()
        resen_sudoku = m[0]
        sudoku1 = m[1]
        for i in range(81):
            self.case[i].dodaj_vrednost('')

    def zacetek(self):
        for i in range(81):
            if sudoku1[int(i / 9)][i % 9] != 0:
                self.case[i].dodaj_vrednost(sudoku1[int(i / 9)][i % 9])

    def resi_me(self):
        for i in range(81):
            if resen_sudoku[int(i / 9)][i % 9] != 0:
                self.case[i].dodaj_vrednost(resen_sudoku[int(i / 9)][i % 9])
            else:
                self.case[i] = 0

    def preveri(self):
        for i in range(81):
            if self.case[i].najdi_vrednost() != resen_sudoku[int(i / 9)][i % 9]:
                top = Toplevel()
                msg = Message(top,
                              text='Sudoku ima napako'
                              )
                msg.pack()
                button = Button(top, text='Nazaj', command=top.destroy)
                button.pack()
                return

        top = Toplevel()
        sg = Message(top, text='Sudoku je pravilno rešen')
        sg.pack()

        button = Button(top, text='Nazaj', command=top.destroy)
        button.pack()


app = Application()
app.root.mainloop()
