import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import pandas as pd


# Daten einlesen aus einer Excel-Datei
data = pd.read_excel("5r_5r.xlsx", header=None).iloc[1:, 0:3].values

# Zeit (1. Spalte), Hammermessung (2. Spalte) und Beschleunigung (3. Spalte)
time = data[:, 0]        # Zeit
force = data[:, 1]       # Hammermessung
acceleration = data[:, 2] # Beschleunigung
dim = len(time)          # Anzahl der Datenpunkte

# 2. Fourier-Transformation
force_fft = np.fft.fft(force) / dim          # Normierte FFT der Hammermessung
acceleration_fft = np.fft.fft(acceleration) / dim  # Normierte FFT der Beschleunigung

# Frequenzauflösung und Frequenzvektor
dF = 1 / (max(time) - min(time))  # Frequenzauflösung
fVec = np.arange(0, dim * dF, dF)  # Frequenzvektor

# 3. Berechnung der Übertragungsfunktion (TF)
transfer_function = acceleration_fft / force_fft  # Verhältnis von FFT der Beschleunigung zur FFT der Hammermessung
real_part = np.real(transfer_function)  # Realteil
imag_part = np.imag(transfer_function)  # Imaginärteil
magnitude = np.abs(transfer_function)  # Betrag
phase = np.angle(transfer_function)  # Phase der Übertragungsfunktion

# 4. Ergebnisse in eine neue Excel-Datei speichern
output_data = np.column_stack([time, fVec, force, acceleration, real_part, imag_part, magnitude, phase])

# Speichern in eine Excel-Datei
pd.DataFrame(output_data, columns=["Time", "Frequenz", "Force", "Acceleration", "Real Part", "Imaginary Part", "Magnitude", "Phase"]).to_excel("5r_5r_Python.xlsx", index=False)

# 5. Grafische Darstellung

# Erster Plot - Zeitsignale: Hammermessung und Beschleunigung
plt.figure(figsize=(10, 6))  # Neue Figur für das erste Plot
plt.subplot(2, 1, 1)  # Erstes Plot: Hammermessung
plt.plot(time, force, 'r', linewidth=1.5)
plt.xlabel('Zeit [s]')
plt.ylabel('Amplitude')
plt.title('Hammermessung')

plt.subplot(2, 1, 2)  # Zweites Plot: Beschleunigung
plt.plot(time, acceleration, 'b', linewidth=1.5)
plt.xlabel('Zeit [s]')
plt.ylabel('Amplitude')
plt.title('Beschleunigung')

# Zweites Plot-Fenster - Frequenzspektren: Hammermessung und Beschleunigung
plt.figure(figsize=(10, 6))  # Neue Figur für das zweite Plot
plt.subplot(2, 1, 1)  # Erstes Plot: FFT Hammermessung
plt.plot(fVec, np.abs(force_fft), 'r', linewidth=1.5)
plt.xlabel('Frequenz [Hz]')
plt.ylabel('Amplitude')
plt.title('FFT Hammermessung')

plt.subplot(2, 1, 2)  # Zweites Plot: FFT Beschleunigung
plt.plot(fVec, np.abs(acceleration_fft), 'b', linewidth=1.5)
plt.xlabel('Frequenz [Hz]')
plt.ylabel('Amplitude')
plt.title('FFT Beschleunigung')

# Drittes Plot-Fenster - Übertragungsfunktion
plt.figure(figsize=(10, 6))  # Neue Figur für das dritte Plot
plt.plot(fVec, np.abs(transfer_function), 'g', linewidth=1.5)
plt.xlabel('Frequenz [Hz]')
plt.ylabel('Amplitude')
plt.title('Übertragungsfunktion (Hammerkraft zu Beschleunigung)')

# Viertes Plot-Fenster - Realteil und Imaginärteil der Übertragungsfunktion
plt.figure(figsize=(10, 6))  # Neue Figur für das vierte Plot
plt.subplot(2, 1, 1)  # Realteil der Übertragungsfunktion
plt.plot(fVec, real_part, 'g', linewidth=1.5)
plt.xlabel('Frequenz [Hz]')
plt.ylabel('Amplitude')
plt.title('Realteil der Übertragungsfunktion')

plt.subplot(2, 1, 2)  # Imaginärteil der Übertragungsfunktion
plt.plot(fVec, imag_part, 'm', linewidth=1.5)
plt.xlabel('Frequenz [Hz]')
plt.ylabel('Amplitude')
plt.title('Imaginärteil der Übertragungsfunktion')

# Fünftes Plot-Fenster - Betrag und Phase der Übertragungsfunktion
plt.figure(figsize=(10, 6))  # Neue Figur für das fünfte Plot
plt.subplot(2, 1, 1)  # Betrag der Übertragungsfunktion
plt.plot(fVec, magnitude, 'b', linewidth=1.5)
plt.xlabel('Frequenz [Hz]')
plt.ylabel('Amplitude')
plt.title('Betrag der Übertragungsfunktion')

plt.subplot(2, 1, 2)  # Phase der Übertragungsfunktion
plt.plot(fVec, phase, 'r', linewidth=1.5)
plt.xlabel('Frequenz [Hz]')
plt.ylabel('Phase [rad]')
plt.title('Phase der Übertragungsfunktion')

# Alle Plots gleichzeitig anzeigen
plt.tight_layout()
plt.show()
