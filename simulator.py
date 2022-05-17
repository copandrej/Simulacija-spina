import matplotlib.pyplot as plt
import numpy as np
import random
import math
import cmath
from qutip import *

# parametri
t = 0.05  #časovni interval za meritve
T = math.pi  # 4*T je trenutno en obhod
time = theta = phi = 0 #zač. vrednosti
frekvenca = 1 #frekvenca ni pomembna saj nimamo podane velikosti mag. polje, od katere je odvisna

#bazni vektorji
upSpin = basis(2, 0) 
downSpin = basis(2, 1)

plus = (upSpin + downSpin)/math.sqrt(2) # | + >
minus = (upSpin - downSpin)/math.sqrt(2)# | - >


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

#simulacija v odvisnosti od parametra b
def simulation(b):
    time = phi = theta = 0
    for i in range(10): #time range 
      while time <= T:
        vec = zPsi(t, phi, theta) #tukaj plotamo
        phi += t*frekvenca
        time += t
      time = 0
      while time <= T:
        vec = xPsi(t, phi, theta) #tukaj plotamo
        theta += t*frekvenca
        time += t
      print("sim")

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
