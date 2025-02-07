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
time = pd.read_excel("./02_03_BSA/a0_1r.xlsx", header = None).iloc[:, 0]

