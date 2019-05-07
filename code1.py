import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import matplotlib.pyplot as plt

# Mount drive folders to use files inside
from google.colab import drive
drive.mount('/content/drive')