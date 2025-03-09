import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Punkte für die Grundform des Flugzeugs (12 Punkte: 5 Tragflügel, 4 Rumpf, 3 Finne)
points0 = np.array([
    [90, 30],    # Tragflügel Punkt 1
    [40, 30],    # Tragflügel Punkt 2
    [0, 30],     # Tragflügel Punkt 3
    [-40, 30],   # Tragflügel Punkt 4
    [-90, 30],   # Tragflügel Punkt 5
    [0, 0],      # Rumpf Punkt 1
    [0, 30],     # Rumpf Punkt 2
    [0, 90],     # Rumpf Punkt 3
    [0, 140],    # Rumpf Punkt 4
    [30, 140],   # Finne Punkt 1
    [0, 140],    # Finne Punkt 2
    [-30, 140]   # Finne Punkt 3
])

# Z-Werte für die verschiedenen Moden
z_vectors = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Grundform
    [1.281, 0.641, 0.017, -0.587, -1.202, -0.013, 0.017, -0.020, -0.027, 0.790, -0.027, -0.603],            # Mode 1: 5,01 Hz
    [0.036, -0.012, 0.019, -0.0143, 0.057, 0.008, 0.019, 0.020, 0.061, 0.883, 0.061, 0.608],                # Mode 2: 20,23 Hz
    [-0.121, 0.215, 0.171, -0.373, -1.179, -0.121, 0.171, 0.466, 0.363, -3.336, 0.363, -2.808],             # Mode 3: 46,2 Hz
    [0.224, -0.081, -0.102, -0.386, -0.649, 0.1340, -0.102, -0.391, -0.483, 11.076/10, -0.483, -8.212/10]   # Mode 4: 49,8 Hz (Die punkte von der Finne wurden skaliert (diviediert durch 10))
]

colors = ['black', 'red', 'blue', 'green','pink']  # Farben für jedes Flugzeug
labels = ['Flugzeug Grundform', '5,048 [Hz]', '20,02 [Hz]', '46,34 [Hz]', '49,707 [Hz]']  # Labels für die Legende

# Funktion zum Zeichnen eines Flugzeugs
def plot_aircraft(ax, points, z_values, color, label):
    x = points[:, 0]
    y = points[:, 1]
    z = z_values  # Z-Werte aus dem Vektor

    ax.scatter(x, y, z, c=color, marker='o')
    ax.plot(x[:5], y[:5], z[:5], c=color)  # Tragflügel
    ax.plot(x[5:9], y[5:9], z[5:9], c=color)  # Rumpf
    ax.plot(x[9:], y[9:], z[9:], c=color)  # Finne

    # Das Label direkt beim Plotten festlegen, sodass es richtig angezeigt wird
    ax.plot([], [], c=color, label=label)  # Leere Datenpunkte für die Legende

# Erstellen der 3 Fenster für Mode 1, Mode 2 und Mode 3
for i, z_vector in enumerate(z_vectors[1:]):  # Nur Mode 1, Mode 2 und Mode 3
    fig = plt.figure(figsize=(12, 6))

    # Erster Plot: Grundform und Mode im selben Diagramm
    ax = fig.add_subplot(111, projection='3d')

    # Flugzeug in Grundform (immer schwarz)
    plot_aircraft(ax, points0, z_vectors[0], 'black', 'Flugzeug Grundform')

    # Flugzeug für den jeweiligen Mode (in verschiedenen Farben)
    plot_aircraft(ax, points0, z_vector, colors[i+1], f'Mode {i+1}: {labels[i+1]}')

    # Titel und Achsen
    ax.set_title(f'Mode {i+1}: {labels[i+1]}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Imaginärteil')

    # Berechnung der z-Achsen-Grenzen automatisch basierend auf den z-Daten
    z_min = min(np.min(z_vectors[0]), np.min(z_vector))
    z_max = max(np.max(z_vectors[0]), np.max(z_vector))
    ax.set_zlim(z_min, z_max)

    # Legende hinzufügen
    ax.legend()

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()
