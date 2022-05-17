import matplotlib.pyplot as plt
import numpy as np
import time
import random
import math
import cmath
from qutip import *


"""
IDEJA:
  a) Simuliram spin v odvisnosti od časa po polju v smeri X xsim()
  b) Simuliram spin v odvisnosti od časa po polju v smeri Z zsim()

  pseudo
  sim1(b):
    Vzamem nek T in b
    T časa laufam simulacijo a) xsim()
    bT časa laufam simulacijo b) xsim()

  sim2:
    generiram različne b in simulriam sim1(b)
  
  main:
    glavni program laufa sim2, plota, oz če to ne bo delal izpiše pogruntane rezultate

  xsim(T):
    za nek majhen deltaT se kliče hermitska funkcija na nekem začetnem vekrju v odvisnosti od časa izpeljana v učbeniku in rezultate shrani kot vektor
    to se kliče T časa. oz. sej ne rabim to večkrat klicat right? samo časovno razliko od prejšnje simulacije uzamem? al? t+=T ?
   zsim(b*T)
    na isto sceno samo b*T časa


"""
#par
t = 0.05 #short interval
T = 5 #ms ?
time = 0
theta = 0
phi = 0+0j
frekvenca = 1+0j

upSpin = basis(2, 0)
downSpin = basis(2, 1)


def xPsi(T):
  upSpin = basis(2, 0)
  downSpin = basis(2, 1)
  debug = ((-1*(1j)*(phi+frekvenca*T))/2)
  n = cmath.cos(theta/2)*cmath.e**debug
  upSpin = upSpin * n
  debug = ((1j*(phi+frekvenca*T))/2)
  n = cmath.sin(theta/2)*cmath.e**debug
  downSpin =  downSpin*n
  vec = downSpin+upSpin
  return vec

def zSim(T):
  print("zSim")

def simulation(b):
  time = 0
  while time < T:
    xSim(time)
    zSim(b*time)
    time += t
    print("sim")

#up.dag() creates bra
"""ket = (basis(2, 0) + basis(2, 1)).unit()
sigmap() * spin
print(sigmap() * spin)
print(sigmax()*spin)"""

#xPsi(2)
print(xPsi(2))

"""
for i in range(5):
  b = random.randint(0, 100)/100
  print("pri b =", b, "je simulacije taka:")
  simulation(b)
"""