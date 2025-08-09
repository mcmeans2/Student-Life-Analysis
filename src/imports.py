# src/imports.py
# This script contains all standard imports for the exploratory analysis notebook.

# Core data handling and visualization libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Modeling libraries 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

# preset settings and styles for plotting
pd.set_option('display.max_columns', 100)
sns.set_style('whitegrid')

print("Imports and settings loaded.")