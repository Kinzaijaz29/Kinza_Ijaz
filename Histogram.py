

"""
Client Age Distribution Histogram

This program reads a dataset from a CSV file and creates a histogram to visualize the distribution
of client ages.

Author: Kinza Ijaz
Created on Tue Nov  7 20:30:53 2023

"""

import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("/Users/Ammad computer/Documents/ClientsAge.csv")

Age = dataset.Age
Age = dataset["Age"]

plt.figure(figsize = (10,5))
plt.hist(Age, bins = 50)
plt.title("Clients Age Distribution", fontsize = 20)

#Label x and y
plt.xlabel("Age", fontsize = 16)
plt.ylabel("Number of Clients", fontsize = 16)

# For see the ranges
plt.grid(axis = "y")
plt.show




