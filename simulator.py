import matplotlib.pyplot as plt
import numpy as np
import random
import math
import cmath
import time
from qutip import *

# parametri
t = 0.005 # časovni interval za meritve
T = 1/20  # 4*T je trenutno en obhod
theta = math.pi
time = phi = 0  # zač. vrednosti
frekvenca = 4*math.pi  # frekvenca ni pomembna saj nimamo podane velikosti mag. polje, od katere je odvisna

# bazni vektorji
upSpin = basis(2, 0)
downSpin = basis(2, 1)

plus = (upSpin + downSpin)/math.sqrt(2)  # | + >
minus = (upSpin - downSpin)/math.sqrt(2)  # | - >

#te metode sedaj  ne igrajo nbene vloge, pustim zavoljo mojega truda :(
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
    theta = math.pi/2
    bl = qutip.Bloch() #za plotanje
    bl.vector_width = 2
    bl.add_states([upSpin, minus])
    bl.point_color = 'b'
    bl.point_marker = 'o'
    bl.point_size = [20]
    bl.show()
    
    for i in range(8):  # time range
        while time <= T:
            tocka = [cmath.sin(theta)*cmath.cos(phi), 
            cmath.sin(theta)*cmath.sin(phi), cmath.cos(theta)]
            bl.add_points(tocka)
            phi += t*frekvenca
            time += t

        time = 0
        phiOld = phi
        thetaNew = cmath.acos(cmath.sin(theta)*cmath.cos(phi))
        phi = cmath.acos(cmath.cos(theta)/cmath.sin(thetaNew))
        theta = thetaNew

        #popravek, v dolocenih primerih
        if(phiOld.real > math.pi+0.2):
            phi =2*math.pi-phi

        while time <= T*b:
            tocka = [cmath.cos(theta), cmath.sin(theta)*cmath.sin(phi),  cmath.sin(theta)*cmath.cos(phi)]
            bl.add_points(tocka)
            phi += (t*frekvenca)
            time += t

        time = 0
        phiOld = phi
        thetaNew = cmath.acos(cmath.sin(theta)*cmath.cos(phi))
        phi = cmath.acos(cmath.cos(theta)/cmath.sin(thetaNew))
        theta = thetaNew
        if(phiOld.real > math.pi+0.2):
            phi =2*math.pi-phi

    bl.render()
        
#generiranje b-jev
for i in range(5):
    b = random.randint(1, 1000)/1000
    print("Pri parametru b =", b, ",je simulacije taka: ")
    simulation(b)
zero = input() #da se program ustavi, da lahko pogledam rezultate
