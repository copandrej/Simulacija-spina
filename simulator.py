import matplotlib.pyplot as plt
import numpy as np
import random
import math
import cmath
import time
from qutip import *

# parametri
t = 0.02 # časovni interval za meritve
T = 1/4  # 4*T je trenutno en obhod
theta = math.pi
time = phi = 0  # zač. vrednosti
frekvenca = 4*math.pi  # frekvenca ni pomembna saj nimamo podane velikosti mag. polje, od katere je odvisna

# bazni vektorji
upSpin = basis(2, 0)
downSpin = basis(2, 1)

plus = (upSpin + downSpin)/math.sqrt(2)  # | + >
minus = (upSpin - downSpin)/math.sqrt(2)  # | - >


def Psi(T, base1, base2, phi, theta):
    scalar = (-1 * (1j) * (phi + frekvenca * T)) / 2
    n = cmath.cos(theta / 2) * cmath.e ** scalar
    base1 = base1 * n
    scalar = ((1j * (phi + frekvenca * T)) / 2)
    n = cmath.sin(theta / 2) * cmath.e ** scalar
    base2 = base2 * n
    vec = base2 + base1
    return vec


def zPsi(T, phi, theta):
    return Psi(T, upSpin, downSpin, phi, theta)


def xPsi(T, phi, theta):
    return Psi(T, plus, minus, phi, theta)

# simulacija v odvisnosti od parametra b
#ker je kot relativen na pozicijo baznega vektoraj morem med eno in 
#drugo simulacije popraviti oba kota 
def simulation(b):
    time = phi = 0
    theta = 1
    bl = qutip.Bloch() #za plotanje
    bl.vector_width = 1
    bl.show()
    for i in range(8):  # time rang
        vektorji = []
        while time <= T:
            phi += t*frekvenca
            time += t
            #vec = zPsi(t, phi, theta)  # tukaj plotamo
            tocka = [cmath.sin(theta)*cmath.cos(phi), 
            cmath.sin(theta)*cmath.sin(phi), cmath.cos(theta)]
            vektorji.append(tocka)
            bl.add_points(tocka)
            bl.render() 
            zero = input()

        time = 0
        tocka[1] = 0
        norm = np.dot(tocka,tocka)
        tocka /= np.dot(tocka,tocka)
        dot_product = np.dot([1,0,0],tocka)
        theta = np.arccos(dot_product)
        #print(theta)
        #theta = theta - math.pi/2
        #print(theta)
        
        #print(math.cos(phi), theta - math.pi/2)
        #print(norm)
        if(tocka[2] < 0):
            print(norm)
            phi = math.acos(norm)+math.pi
        else:
            phi = math.acos(norm)
            
        #print(phi)
        while time <= T*b:
            #za majhne b lahko aproximiramo samo premik 
            #vec = xPsi(t, phi, theta)  # tukaj plotamo izralunaj theta med x osjo (| - > in vectorejm)
            tocka = [cmath.cos(theta), cmath.sin(theta)*cmath.sin(phi),  cmath.sin(theta)*cmath.cos(phi)]
            vektorji.append(tocka)
            bl.add_points(tocka)
            bl.render() 

            #zero = input()
            phi += t*frekvenca
            time += t
        time = 0
        tocka[1] = 0
        norm = np.dot(tocka,tocka)
        tocka /= np.dot(tocka,tocka)
        dot_product = np.dot([0,0,1],tocka)
        theta = np.arccos(dot_product)
        
        print(theta)

        print(norm)
        print(tocka[0])
        print("okol")
        if(tocka[0] < 0 or tocka[1] > 0 ):
            print("debug")
            phi = math.acos(norm)+math.pi
        else:
            phi = math.acos(norm)
        #bl.add_states(vektorji)
        bl.render()
        print("okol")
        zero = input()
        



#b = qutip.Bloch()
#b.show()
simulation(0.2)
"""
phi = 0
theta = 0
b = 0.5
for i in range(4):
  #vec = zPsi(T, phi,theta)
  #phi+=T*frekvenca
  vec = xPsi(T*b, phi, theta)
  theta+=T*b*frekvenca

print(vec)
for i in range(5):
  b = random.randint(0, 100)/100
  print("pri b =", b, "je simulacije taka:")
  simulation(b)
"""
