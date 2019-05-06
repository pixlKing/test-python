import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
######################################

from google.colab import drive
drive.mount('/content/drive')
######################################

# PASOS:
# leer archivos .txt
# filtrarlos segun un diciconario "array"
# Armar un csv con los resultados con dataFrame
# Pintar un grafico con esos datos

# file = pd.read_csv('/content/drive/My Drive/resume/data2.txt')

# dataFrame = pd.DataFrame(file)

# print(dataFrame['asdasd'])