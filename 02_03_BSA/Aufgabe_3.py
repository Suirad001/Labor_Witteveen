import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Daten einlesen aus einer Excel-Datei
data = pd.read_excel("./02_03_BSA./Aufgabe_3.xlsx", header=None).iloc[1:, 0:5].values

time = data[:, 0]               # Zeit
acceleration_0 = data[:, 1]     # Sensor 1
acceleration_1 = data[:, 2]     # Sensor 2
acceleration_2 = data[:, 3]     # Sensor 3
acceleration_3 = data[:, 4]     # Sensor 4

y = np.column_stack((acceleration_0, acceleration_1, acceleration_2, acceleration_3))

y = y.astype(float)

# Anzahl der Teile (Chunks), in die die Daten aufgeteilt werden sollen
num_chunks = 10
chunk_size = len(y) // num_chunks  # Anzahl der Daten pro Teil (Chunk)

# Tragflügel Grundform (4 Punkte)
tragflügel = np.array([[90, 30, 0], [40, 30, 0], [-40, 30, 0], [-90, 30, 0]])
z0 = tragflügel[:, 2]  # Z-Werte der Grundform des Tragflügels

# Funktion zum Zeichnen eines Vektors (Eigenvektor) im 2D Plot
def plot_eigenvector(ax, tragflügel, eigenvector, color, label):
    # X-Koordinaten und Z-Koordinaten (y bleibt konstant)
    x = tragflügel[:, 0]
    z = eigenvector  # Eigenvektor für Z-Werte
    
    # Grundform des Tragflügels (4 Punkte)
    ax.plot(x, z0, c='black', label='Grundform Tragflügel', marker='o', markersize=5)  # Grundform in schwarz mit 4 Punkten
    
    # Scatter plot der Punkte und Linienplot für die Eigenvektoren
    ax.scatter(x, z, c=color, marker='o')  # Eigenvektorpunkte
    ax.plot(x, z, c=color)  # Verbindungslinien der Eigenvektorpunkte

    # Label für den Vektor setzen
    ax.plot([], [], c=color, label=label)  # Leere Datenpunkte für die Legende

# Aktuellen Arbeitsordner herausfinden und den "Plots"-Ordner darin anlegen
current_dir = os.path.dirname(os.path.abspath(__file__))  # aktueller Ordner
output_dir = os.path.join(current_dir, 'Plots')  # Verzeichnis für Plots
if not os.path.exists(output_dir):  # Falls der Ordner nicht existiert
    os.makedirs(output_dir)  # Ordner erstellen

# 1. HKA für den gesamten Datensatz
Y_full = np.dot(y.T, y)  # Korrelationsmatrix für den gesamten Datensatz
eigenvalues_full, eigenvectors_full = np.linalg.eig(Y_full)

# Erstellen der 2D-Diagramme für alle Eigenvektoren des gesamten Datensatzes
fig, axes = plt.subplots(1, 4, figsize=(20, 4))  # 1x4 Subplots für 4 Eigenvektoren
axes = axes.flatten()  # Flatten für einfacheren Zugriff auf die Subplots

for i, eigenvector in enumerate(eigenvectors_full.T):  # Alle Eigenvektoren (Mode 1, Mode 2, Mode 3, Mode 4)
    ax = axes[i]  # Zugriff auf den i-ten Subplot

    # Grundform und Eigenvektor für den jeweiligen Mode plotten
    plot_eigenvector(ax, tragflügel, eigenvector, f'C{i+1}', f'Eigenvektor {i+1}')

    # Titel und Achsen
    ax.set_title(f'Eigenvektor {i+1}')
    ax.set_xlabel('X')
    ax.set_ylabel('Eigenvektor Z')

    # Berechnung der Z-Achsen-Grenzen unter Berücksichtigung der Grundform
    z_min = min(np.min(z0), np.min(eigenvector)) - 0.2  # Etwas Puffer unter dem kleinsten Wert
    z_max = max(np.max(z0), np.max(eigenvector)) + 0.2  # Etwas Puffer über dem größten Wert
    ax.set_ylim(z_min, z_max)

    # Legende immer in der rechten oberen Ecke
    ax.legend()

    # Eigenwert unter dem Plot anzeigen (Text fett und größer)
    ax.text(0.5, -0.3, f'Eigenwert: {eigenvalues_full[i]:.2f}', transform=ax.transAxes, ha='center', va='center', fontsize=14, fontweight='bold')

# Titel für die gesamte Figur
fig.suptitle(f'HKA für gesamten Datensatz', fontsize=16)
# Bildname für das Speichern
plot_filename_full = f"{output_dir}/HKA_Gesamt.png"

# Diagramm anzeigen und speichern
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Platz für die Gesamtüberschrift oben
plt.savefig(plot_filename_full)  # Speichern des Plots als PNG-Datei
plt.close(fig)  # Schließt das Bild, um Speicherplatz zu sparen

# 2. HKA für die 10 Teile der Daten
for chunk_idx in range(num_chunks):
    # Teile die Daten in num_chunks Teile auf
    start_idx = chunk_idx * chunk_size
    end_idx = (chunk_idx + 1) * chunk_size if chunk_idx < num_chunks - 1 else len(y)
    y_chunk = y[start_idx:end_idx, :]  # Chunk der Daten

    # Berechnung der Eigenwerte und Eigenvektoren für den aktuellen Chunk
    Y_chunk = np.dot(y_chunk.T, y_chunk)
    eigenvalues, eigenvectors = np.linalg.eig(Y_chunk)

    # Erstellen der 2D-Diagramme für alle Eigenvektoren des aktuellen Chunks
    fig, axes = plt.subplots(1, 4, figsize=(20, 4))  # 1x4 Subplots für 4 Eigenvektoren
    axes = axes.flatten()  # Flatten für einfacheren Zugriff auf die Subplots

    for i, eigenvector in enumerate(eigenvectors.T):  # Alle Eigenvektoren (Mode 1, Mode 2, Mode 3, Mode 4)
        ax = axes[i]  # Zugriff auf den i-ten Subplot

        # Grundform und Eigenvektor für den jeweiligen Mode plotten
        plot_eigenvector(ax, tragflügel, eigenvector, f'C{i+1}', f'Eigenvektor {i+1}')

        # Titel und Achsen
        ax.set_title(f'Eigenvektor {i+1}')
        ax.set_xlabel('X')
        ax.set_ylabel('Eigenvektor Z')

        # Berechnung der Z-Achsen-Grenzen unter Berücksichtigung der Grundform
        z_min = min(np.min(z0), np.min(eigenvector)) - 0.2  # Etwas Puffer unter dem kleinsten Wert
        z_max = max(np.max(z0), np.max(eigenvector)) + 0.2  # Etwas Puffer über dem größten Wert
        ax.set_ylim(z_min, z_max)

        # Legende immer in der rechten oberen Ecke
        ax.legend()

        # Eigenwert unter dem Plot anzeigen (Text fett und größer)
        ax.text(0.5, -0.3, f'Eigenwert: {eigenvalues[i]:.2f}', transform=ax.transAxes, ha='center', va='center', fontsize=14, fontweight='bold')

    # Titel für die gesamte Figur
    fig.suptitle(f'Datensatz: {chunk_idx+1}/10', fontsize=16)

    # Bildname für das Speichern
    plot_filename = f"{output_dir}/Datensatz_{chunk_idx+1}.png"

    # Diagramm anzeigen und speichern
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Platz für die Gesamtüberschrift oben
    plt.savefig(plot_filename)  # Speichern des Plots als PNG-Datei
    plt.show()
    plt.close(fig)  # Schließt das Bild, um Speicherplatz zu sparen

