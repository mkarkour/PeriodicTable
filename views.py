import sqlite3
from string import ascii_lowercase
import pandas as pd
import math

###############################
###---------Constante-------###     
###############################
CNTP={"Pression":101325,"Temperature":273.15,"V_molaire":22.4}
CSTP={"Pression":1.01325*math.pow(10,5),"Temperature":298.15,"V_molaire":24.5}
n_avogadro = 6.022*math.pow(10,23)
air = {"O":0.21,"N":0.78,"Autre":0.01}

#################################
### Read Data in the database ###
#################################
def read_data_pandas(table):
    dbase = sqlite3.connect('mendeleev.db', isolation_level=None)
    dbase.execute("PRAGMA foreign_keys = 1")
    query = ('''SELECT * FROM "{}"'''.format(table))
    results=pd.read_sql_query(query,dbase)
    dbase.close()
    return print(results)
#read_data_pandas("Element")


def separateur(eq):
    d = dict()
    compose,valence=[],[]
    for e in eq:
        if e.isalpha():
            compose.append(e)
        else:
            valence.append(e)

    mini=False
    for a in ascii_lowercase:                              #ascii_lowercase = "abcdefghijklmnopqrstuvwxyz" en minuscule 
        if a in compose:
            mini = True
            break
    if mini == True:
        compose_clear=[]
        for c in range(len(compose)):
            if compose[c].islower():                       #regarde si un nombre est en minuscule
                new = str(compose[c-1]+ compose[c])
                compose_clear.append(new)
                compose_clear.remove(compose[c-1])
            else:
                compose_clear.append(compose[c])
        
    else:
        compose_clear=compose
    
    a=len(eq)
    for position in range(a):
        if eq[position].isnumeric():                     #regarde si un caractère est un nbre numérique
            if eq[position-1].islower():
                last = eq[position-2]+eq[position-1]
                d[last]=eq[position]
            else:
                last=eq[position-1]
                d[last]=eq[position]
        else:
            continue
    if len(valence)!= len(compose_clear):
        for l in compose_clear:
            if l in d:
                continue
            else:
                d[l]=1

    #print(compose_clear, valence)
    #print(d)
    return d

def masse_molaire(eq):
    repartition = separateur(eq)
    dbase = sqlite3.connect("mendeleev.db",isolation_level=None)
    masse_mol = 0
    for r in repartition:
        masse_atomique = dbase.execute('''SELECT Masse_atomique FROM Element WHERE Symbole = "{}"'''.format(r)).fetchall()[0][0]
        masse_mol += float(masse_atomique*float(repartition[r]))
    print("La masse molaire est de {a} g/mol pour le {b}".format(a=masse_mol,b=eq))
    return masse_mol
        
def mole(eq,masse):
    g_mol = masse_molaire(eq)
    g = float(masse)
    mol = g/g_mol
    print("le nombre de mole est de {a} pour {b}".format(a=mol,b=eq))
    return mol

def masse():

    return True

def number_atome(eq,masse):
    n = mole(eq,masse)
    number = n*n_avogadro
    print("le nombre d'atomes du {a} est de {b}".format(a=eq,b=number))
    return number

def concentration_molaire(eq,v,m):
    n = mole(eq,m)
    c_M=n/v
    print("La concentration molaire est de {a} mol/l pour {b}".format(a=c_M,b=eq))
    return c_M

def concentration_massique(eq,v,m):
    M = masse_molaire(eq)
    c_m=m/v
    c_M=c_m/M
    print("La concentration massique est de {a} g/l pour {b}".format(a=c_m, b=eq))
    return c_m

def repartisseur(eq,masse,mol,vol):
    g_mol=masse_molaire(eq)
    # if masse == "":
    #     if mol != "":

    return True

def separateur_coef(eq):
    liste =[]
    for e in eq:
        liste.append(e)
    eq_clear=""
    for l in liste:
        if l.isnumeric():
            liste.remove(l)
            coef=l
            break
    for l in liste:
        eq_clear+=str(l)
    return (coef,eq_clear)

def stoechiometrie(r1,r2,p1):
    compose = [r1,r2,p1]
    compose_coef=[]
    for c in compose:
        react1=separateur(separateur_coef(c)[1])
        for r in react1:
            a = int(react1[r])*int(separateur_coef(c)[0])
            react1[r]=a
        compose_coef.append(react1)

    reactif = [compose_coef[0],compose_coef[1]]
    produit = [compose_coef[2]]
    print(reactif,produit)
    reactif_commun=dict()
    for element, nombre in compose_coef[0].items():
        if element in compose_coef[1]:
            reactif_commun[element]=nombre+compose_coef[1][element]
        else:
            reactif_commun[element]=nombre
    for element2,nombre2 in compose_coef[1].items():
        if element2 in reactif_commun:
            continue
        else:
            reactif_commun[element2]=nombre2
    
    produit_commun = compose_coef[2]
    print(reactif_commun, produit_commun)

    for i in zip(reactif_commun,produit_commun):
        if reactif_commun[i[0]]!=produit_commun[i[0]]:
            diff = reactif_commun[i[0]]-produit_commun[i[0]]
            print(diff,i[0])
            if diff <0:
                diff=-diff
            
            print(reactif_commun,produit_commun)
  

    return True
#stoechiometrie("3H2O","2CO2","2H2CO3")





