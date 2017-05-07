from random import randint
import sys
a = []
tabela2 = []
for i in range(9):
    a += [[0]*9]
    tabela2 += [[0]*9]
x = 0
z = 0
y = 0
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




def zapolni():
    for i in range(9):
        for j in range(9):
            a[i][j] = 0
    
    y = 0
    while y <10:
        e = randint(1,9)
        f = randint(0,8)
        g = randint(0,8)
        if(a[f][g] == 0):
            if(je_veljavna(e,f,g) == True):
                a[f][g] = e
                y += 1
    return a

def dopolni():
   y =  0
   while y < 1:
        e = randint(1,9)
        f = randint(0,8)
        g = randint(0,8)
        if(a[f][g] == 0):
            if(je_veljavna(e,f,g) == True):
                a[f][g] = e
                y += 1
   return a
    
def resitelj1(vrstica, stolpec,y = 0):
        if((vrstica == 8) and (stolpec == 9)):
            y += 1
            print(a)
            return a
            
        elif(stolpec == 9):
            stolpec = 0
            vrstica += 1

        if(a[vrstica][stolpec] != 0):
             resitelj1(vrstica,stolpec+1,y)
        else:
            for i in range(1,10):
                if(je_veljavna(i, vrstica, stolpec) == True):
                    a[vrstica][stolpec] = i
                    resitelj1(vrstica, stolpec+1,y)


            a[vrstica][stolpec] = 0



def resitelj3(vrstica, stolpec,s = False):
        if(s == True):
            sys.exit
        if((vrstica == 8) and (stolpec == 9)):
                s = True
                sys.exit()
                return 
            
            
        elif(stolpec == 9):
            stolpec = 0
            vrstica += 1
        
        if(a[vrstica][stolpec] != 0):
             if(s == True):
                 sys.exit
             resitelj1(vrstica,stolpec+1,s)
        else:
            for i in range(1,10):
                if(je_veljavna(i, vrstica, stolpec) == True):
                    if(s == True):
                        sys.exit
                    a[vrstica][stolpec] = i
                    resitelj3(vrstica, stolpec+1,s)


            a[vrstica][stolpec] = 0

        if(s == True):
            sys.exit


            
            

def resitelj2(vrstica, stolpec):
        if((vrstica == 8) and (stolpec == 9)):
            global z
            z += 1
            print(z,0)
            return

        elif(stolpec == 9):
            stolpec = 0
            vrstica += 1

        if(a[vrstica][stolpec] != 0):
             resitelj2(vrstica,stolpec+1)
        else:
            for i in range(1,10):
                if(je_veljavna(i, vrstica, stolpec) == True):
                    a[vrstica][stolpec] = i
                    resitelj2(vrstica, stolpec+1)


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
             resitelj2(vrstica,stolpec+1)
        else:
            for i in range(1,10):
                if(je_veljavna(i, vrstica, stolpec) == True):
                    tabela2[vrstica][stolpec] = i
                    resitelj2(vrstica, stolpec+1)


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



    
    
def main():
    while True:
        global z
        z = 0
        zapolni()
        resitelj2(0,0)
        print(z)
        if(z > 1):
            dopolni()
            z = 0
            resitelj2(0,0)
            print(z)
        if(z == 1):
            return a
            print(a)
        else:
            z = 0
            

def main2():
    while True:
        global z
        napolni()
        print(tabela2)
        resitelj4(0,0)
        print(z)
        if(z == 1):
            return a
            print(tabela2)
        else:
            z = 0
        
        




