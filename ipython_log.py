# IPython log file

get_ipython().run_line_magic('logstart', '')
import pandas as pd
import numpy as np
pd.read_csv("irisdata.csv")
df = pd.read_csv("irisdata.csv")

print (df.describe())


