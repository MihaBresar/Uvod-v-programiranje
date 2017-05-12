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
            sys.exit
            return
        if((vrstica == 8) and (stolpec == 9)):
                s = True
                sys.exit()
                
                 
            
            
        elif(stolpec == 9):
            stolpec = 0
            vrstica += 1
        
        if(a[vrstica][stolpec] != 0):
             if(s == True):
                 sys.exit
                 return
             resitelj3(vrstica,stolpec+1)
        else:
            for i in range(1,10):
                if(je_veljavna(i, vrstica, stolpec) == True):
                    if(s == True):
                        sys.exit
                        return
                    a[vrstica][stolpec] = i
                    resitelj3(vrstica, stolpec+1)


            a[vrstica][stolpec] = 0

        if(s == True):
            sys.exit
            return


            
            


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
    while f < 9:
        t = randint(1,9)
        if(je_veljavna(t,0,f) == True):
            a[0][f] =t
            f += 1

    return a


def prva():

    x = 0
    z = 0
    y = 0
    s = False
    print(x)
    
    vrstica(a)
    print(x)
    resitelj3(0,0)
    print(a)



    

            

def main2():
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
        

def pisatelj(c):
    with open('text.txt','w') as f:
        for i in c:
            h = str(i).strip(',')
            h = h.replace(',','')
            h = h.replace(' ','')
            print(h[1:len(h)-2],file=f)
        




prva()

m = main2()
pisatelj(m[1])

        
        




