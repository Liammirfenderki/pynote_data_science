import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# -------------- call for data  -------------------- 

df= pd.read_csv("data_sets/irish.csv")
print(head(df))
#print(tail(df))
