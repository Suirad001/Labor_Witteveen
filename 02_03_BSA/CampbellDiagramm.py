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
def readMeas(name):
    # Excel einlesen
    a = pd.read_excel(name, header = None).iloc[1:, 1]

    # In numpy-Array umwandeln
    a = np.array(a)

    # Einträge alle zu float machen
    a = a.astype(float)

    return a

# Beschleunigungen der Messpunkte
#--------------------------------
a0 = readMeas("./02_03_BSA/a0_1r.xlsx")
a1 = readMeas("./02_03_BSA/a1_r2.xlsx")
a2 = readMeas("./02_03_BSA/a2_r4.xlsx")
a3 = readMeas("./02_03_BSA/a3_r5.xlsx")
#============================================================================

# 2 - Transformation in den Freq.-Bereich
#========================================

# Shortterm-FFT
#--------------
fAbtast = 1.6516129 * 10**3
f, t_stft, A0 = stft(a0, fAbtast, nperseg=500, window="hamming")

# Drehzahl des Motors
#--------------------
def getRot(U):
    # Lineare Interpolation zw. 2 Messwerten
    n = 572.142857 * U - 93
    return n

# Definition des Spannungsvektors
Ustart = 0
Uend = 5
U = np.linspace(Ustart, Uend, len(t_stft))

# Bestimmen des Drehzahlvektors
n = getRot(U)

# STFT plotten
#-------------
plt.pcolormesh(n, f, np.abs(A0), cmap="jet")
plt.ylabel('Frequenz [Hz]')
plt.xlabel('Drehzahl [min^-1]')
plt.title('Short-Time Fourier Transform (STFT)')
plt.colorbar(label='Amplitude')
plt.show()






#==========================================================================#
#                           EVT. DOCH BENÖTIGT                             #
#==========================================================================#

# Zeitvektor
#-----------
# fAbtast = 1.6516129 * 10**3
# dt = 1 / fAbtast
# nMeas = len(a0)
# tStart = 0
# tEnd = nMeas * dt

# time = np.arange(tStart, tEnd, dt)

# Funktion zum Aufsplitten eines Vektors
#---------------------------------------
# def splitVec(vec, size):
#     return np.array_split(vec, np.ceil(len(time) / size))

# # Aufteilen des Zeit- und Beschl.-vektors
# #----------------------------------------
# splitSize = 1000
# timeSplit = splitVec(time, splitSize)
# a0Split = splitVec(a0, splitSize)

# # Erstellen des Frequenzvektors
# #------------------------------
# fStart = 0
# df = 1 / (nMeas * dt)
# freq = np.arange(fStart, nMeas, df)

# Transformation in den Frequenzbereich
#--------------------------------------
# Anlegen einer 0-Matrix (n = Länge eines Subvektors, m = Anz. Subvektoren)
# A00 = np.zeros((splitSize, len(a0Split)))

# # Schleife über alle Subvektoren -> FFT
# for i in range(splitSize):
#     # Ablegen der FFT-transformierten Beschl. in den Spalten der Matrix
#     A00[:, i] = np.fft.fft(a0Split[i])

# plt.figure(figsize=(12,6))
# plt.plot(freq, abs(A00[:, 8]))
# plt.show()