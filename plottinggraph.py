import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# getting the csv file
cars = pd.read_csv("C:/Users/sachi/Downloads/archive/Cars93.csv" , header=0, sep=",")

# getting the axes
x_label = cars.Make[0:11]
y_label = cars.Weight[0:11]

# plotting the graph
plt.bar(x_label,y_label ,color='g');

plt.xlabel("Make")
plt.ylabel("Years")

plt.show()
