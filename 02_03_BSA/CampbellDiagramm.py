# Import benötigter Bibliotheken
#===============================
import numpy as np
import pandas as pd

#====================================================================#
#                         CAMPBELL-DIAGRAMM                          #
#====================================================================#

# 1 - Einlesen der Messdaten
#===========================

# Beschleunigungen der Messpunkte
#--------------------------------
a0 = pd.read_excel("./02_03_BSA/a0_1r.xlsx", header = None).iloc[:, 1]
a1 = pd.read_excel("./02_03_BSA/a1_r2.xlsx", header = None).iloc[:, 1]
a2 = pd.read_excel("./02_03_BSA/a2_r4.xlsx", header = None).iloc[:, 1]
a3 = pd.read_excel("./02_03_BSA/a3_r5.xlsx", header = None).iloc[:, 1]

# Zeitvektor
#-----------
fAbtast = 1.6516129 * 10**3
dt = 1 / fAbtast
nMeas = len(a0)
tStart = 0
tEnd = nMeas * dt

time = np.arange(tStart, tEnd, dt)

# Frequenzvektor
#---------------
df = 1 / (nMeas * dt)
fStart = 0
fEnd = nMeas * df

freq = np.arange(fStart, fEnd, df)


# Drehzahl des Motors
#--------------------
def getRot(U):
    # Lineare Interpolation zw. 2 Messwerten
    n = 572.142857 * U - 93
    return n

# Definition des Spannungsvektors
Ustart = 0
Uend = 5
U = np.linspace(Ustart, Uend, nMeas)

# Bestimmen des Drehzahlvektors
n = getRot(U)
