import os
os.system("python -m venv .venv")
os.system("source .venv/bin/activate")
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("your_project.csv")
plt.bar(df["column1"], df["column2"])
plt.show()
