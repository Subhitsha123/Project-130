import pandas as pd
import csv

df = pd.read_csv("bright_stars.csv")
print(df.head)
print(df.shape)

del df["Luminosity"]

df = df[df["Star_name"].notna()]
df = df[df["Distance"].notna()]
df = df[df["Mass"].notna()]
df = df[df["Radius"].notna()]

print(df.shape)

df.to_csv('main.csv')