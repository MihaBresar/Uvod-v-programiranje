
from tkinter import *
from random import randint

#***************************************************************************************
#Funkcija ki ustvari sudoku in vrne dve tabeli. Prva je naključno generiran sudoku. Druga pa njegova rešena verzija.
#**********************************************************************************************

a = []
tabela2 = []
for i in range(9):
    a += [[0]*9]
    tabela2 += [[0]*9]
x = 0
z = 0
y = 0
s = False
def je_veljavna(stevilo , vrstica, stolpec):
    
        for i in range(9):
            if(a[vrstica][i] == stevilo):
                return False
            if(a[i][stolpec] == stevilo):
                return False

        velikaVrstica = 3 * int(vrstica/3)
        velikiStolpec = 3 * int(stolpec/3)
        vrstica1 = (vrstica + 2) % 3
        vrstica2 = (vrstica + 4) % 3
        stolpec1 = (stolpec + 2) % 3
        stolpec2 = (stolpec + 4) % 3
    

        if(a[vrstica1 + velikaVrstica][stolpec1 +velikiStolpec] == stevilo):
            return False
        if(a[vrstica1 + velikaVrstica][stolpec2 +velikiStolpec] == stevilo):
            return False
        
        if(a[vrstica2 + velikaVrstica][stolpec1 +velikiStolpec] == stevilo):
            return False

        if(a[vrstica2 + velikaVrstica][stolpec2 +velikiStolpec] == stevilo):
            return False
        return True






def resitelj3(vrstica, stolpec):
        global s
        if(s == True):
            return
        if((vrstica == 8) and (stolpec == 9)):
            s = True
            return
                
                 
            
            
        elif(stolpec == 9):
            stolpec = 0
            vrstica += 1
        
        if(a[vrstica][stolpec] != 0):
             resitelj3(vrstica,stolpec+1)
             if(s == True):
                 return
        else:
            for i in range(1,10):
                if(je_veljavna(i, vrstica, stolpec) == True):
                    a[vrstica][stolpec] = i
                    resitelj3(vrstica, stolpec+1)
                    if(s == True):
                        return


            a[vrstica][stolpec] = 0



            
            


def resitelj4(vrstica, stolpec):
        if((vrstica == 8) and (stolpec == 9)):
            global z
            z += 1
            print(z,0)
            return

        elif(stolpec == 9):
            stolpec = 0
            vrstica += 1

        if(a[vrstica][stolpec] != 0):
             resitelj4(vrstica,stolpec+1)
        else:
            for i in range(1,10):
                if(je_veljavna(i, vrstica, stolpec) == True):
                    tabela2[vrstica][stolpec] = i
                    resitelj4(vrstica, stolpec+1)


            tabela2[vrstica][stolpec] = 0


def napolni():
    
    for i in range(9):
        for j in range(9):
            tabela2[i][j] = 0
    
    y = 0
    while y <30:
        f = randint(0,8)
        g = randint(0,8)
        if(tabela2[f][g] == 0):
                tabela2[f][g] = a[f][g]
                y += 1
    return tabela2



def vrstica(a):
    f = 0
    for i in range(9):
        for j in range(9):
            a[i][j]  = 0
    while f < 9:
        t = randint(1,9)
        if(je_veljavna(t,0,f) == True):
            a[0][f] = t
            f += 1

    return a


def main1():

    x = 0
    z = 0
    y = 0
    s = False
    print(x)
    
    vrstica(a)
    print(a)
    resitelj3(0,0)
    print(a)
           

def main2():
    global s
    s = False
    main1()
    while True:
        global z
        napolni()
        print(tabela2)
        resitelj4(0,0)
        print(z)
        if(z == 1):
            return [a,tabela2]
            print(tabela2)
        else:
            z = 0
m = main2()

    
a = m[0]
b = m[1]



#***************************************************************************************************************************
#Grafični vmesik
#**************************************************************************************************************************
class Celica:
        def __init__(self, root, r, c):
            self.vrednost = StringVar()
            self.vhod = Entry(root, textvariable=self.vrednost, width=5)
            if(r<4) and (c<3 or c>5):
                self.vhod = Entry(root, textvariable=self.vrednost, width=5,bg='orange')
            elif((r>6) and (c<3 or c>5)):
                self.vhod = Entry(root, textvariable=self.vrednost, width=5,bg='orange')
            elif(r<7 and r>3) and (c>2 and c<6):
                self.vhod = Entry(root, textvariable=self.vrednost, width=5,bg='orange')
            else:
                self.vhod = Entry(root, textvariable=self.vrednost, width=5)
            self.vhod.grid(row=r, column=c)
            
                
            

        def getValue(self):
            if self.vhod.get()=='' or int(self.vhod.get())<1 or int(self.vhod.get())>9:
                return 0

            return int(self.vhod.get())

        def putValue(self, v):
            self.vrednost.set(v)

class Application(Tk):
        def __init__(self):
            self.root = Tk()
            self.root.title('Igra Sudoku')

            self.solve = Button(self.root, text="Resi", command=self.SolveMe)
            self.quitt = Button(self.root, text="Koncaj", command=self.OutMe)
            self.newpl = Button(self.root, text='Zacni', command=self.newp)
            self.preveri = Button(self.root, text='Preveri',command=self.preveri)
            
            self.preveri.grid(row=10,column=7,columnspan=6)
            self.solve.grid(row=10, column=0,columnspan=3)
            self.quitt.grid(row=10, column=2,columnspan=3)
            self.newpl.grid(row=10, column=4,columnspan=4)
            
            
            self.case = []
            for i in range(9):
                for j in range(9):
                    self.case += [Celica(self.root, i+1, j)]

        def OutMe(self):
            global a
            global b
            m = main2()
            a = m[0]
            b = m[1]
            for i in range(81):
                self.case[i].putValue('')
        
        def newp(self):
            for i in range(81):
                    if(b[int(i/9)][i%9] != 0):
                        self.case[i].putValue(b[int(i/9)][i%9])
                
        def SolveMe(self):
            for i in range(81):
                if(a[int(i/9)][i%9] != 0):
                    self.case[i].putValue(a[int(i/9)][i%9])
                else:
                    self.case[i]=0
        
        def preveri(self):
            for i in range(81):
                if self.case[i].getValue() != a[int(i/9)][i%9]:
                        top = Toplevel()
                        msg = Message(top, text='Vaša rešitev ima napako')
                        msg.pack()
                        button = Button(top, text="Nazaj", command=top.destroy)
                        button.pack()
                        return
                          
            top = Toplevel()
            sg = Message(top, text='Vaša rešitev je pravilna')
            sg.pack()

            button = Button(top, text="Nazaj", command=top.destroy)
            button.pack()
                

            




app = Application()
app.root.mainloop()





