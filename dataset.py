import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cities.csv")


plt.figure(figsize=(12,6))
plt.bar(df["City"][:10], df["Population"][:10])
plt.title("Top 10 Cities by Population")
plt.xticks(rotation=45)
plt.ylabel("Population")
plt.show()