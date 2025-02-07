# Import benötigter Bibliotheken
#===============================
import numpy as np
import pandas as pd

#====================================================================#
#                         CAMPBELL-DIAGRAMM                          #
#====================================================================#

# 1 - Einlesen der Messdaten
#===========================
a0 = pd.read_excel("./02_03_BSA/a0_1r.xlsx", engine = "openpyxl").iloc[:, 1]


print(a0)