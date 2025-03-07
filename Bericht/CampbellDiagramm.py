# Import benötigter Bibliotheken
#===============================
import numpy as np
import pandas as pd
from scipy.interpolate import (griddata, Rbf)
from scipy.signal import stft
import matplotlib.pyplot as plt

#====================================================================#
#                         CAMPBELL-DIAGRAMM                          #
#====================================================================#

# 1 - Einlesen der Messdaten
#===========================

# Fkt. zum Einlesen der Beschleunigungen
#---------------------------------------
def readMeas(name):
    a = pd.read_excel(name, header = None).iloc[1:, 1]  # Excel einlesen
    a = np.array(a)                        # In numpy-Array umwandeln
    a = a.astype(float)                    # Einträge alle zu float machen

    return a

# Beschleunigungen der Messpunkte
#--------------------------------
a0 = readMeas("./02_03_BSA/a0_1r.xlsx")
a1 = readMeas("./02_03_BSA/a1_r2.xlsx")
a2 = readMeas("./02_03_BSA/a2_r4.xlsx")
a3 = readMeas("./02_03_BSA/a3_r5.xlsx")

# Liste mit Beschleunigungen
a = [a0, a1, a2, a3]
#============================================================================

# 2 - Transformation in den Freq.-Bereich
#========================================

# Fkt. zur Bestimmung der Drehzahl des Motors
#--------------------------------------------
def getRot(U):
    # Lineare Interpolation zw. 2 Messwerten
    n = 572.142857 * U - 93
    return n

# Festlegen der Abtastfrequenz
#-----------------------------
fAbtast = 1.6516129 * 10**3

# Definieren der Spannungsgrenzen
#--------------------------------
Ustart = 0
Uend = 5

# Definieren einer Laufvariable
i = 0

for acc in a:
    # Shortterm-FFT
    #--------------
    f, t_stft, A = stft(acc, fAbtast, nperseg=500, window="hamming")

    # Bestimmen des Spannungsvektors
    #-------------------------------
    U = np.linspace(Ustart, Uend, len(t_stft))

    # Bestimmen des Drehzahlvektors
    #------------------------------
    n = getRot(U)

    # Mitzählen der Messpunkte
    i = i + 1

    # STFT plotten -> Campbell-Diagramm
    #----------------------------------
    fig = plt.figure(figsize=(12,8))
    
    plt.pcolormesh(n, f, np.abs(A), cmap="jet")
    plt.ylabel('Frequenz [Hz]')
    plt.xlabel('Drehzahl [U/min]')
    plt.title(f'Campbell-Diagramm für Messpunkt {i}')
    plt.colorbar(label='Amplitude')

    plt.show()