#Task Assignment No. 4
#Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from zipfile import ZipFile

#Load dataset from ZIP

file_path = "C:/Users/ASUS/Downloads/archive (2).zip"
df = pd.read_csv(file_path)

#Basic info
print("First 5 rows:\n", df.head())
print("\nColumns:", df.columns.tolist())
print("\nData Summary:\n", df.describe(include='all'))
df.info()

#Visualizations

plt.figure(figsize=(12, 6))
sns.histplot(df["Average_Rating"], bins=20, kde=True)
plt.title("Distribution of Average Ratings")
plt.xlabel("Average Rating")
plt.ylabel("Count")
plt.show()

#Rating vs Price
plt.figure(figsize=(12, 6))
sns.scatterplot(x="Prices", y="Average_Rating", hue="Is_Bestseller", data=df)
plt.title("Price vs. Average Rating (Bestseller Highlighted)")
plt.xlabel("Price")
plt.ylabel("Average Rating")
plt.show()

#Cuisine vs Rating
plt.figure(figsize=(14, 6))
sns.boxplot(x="Cuisine", y="Average_Rating", data=df)
plt.title("Cuisine-wise Average Rating Distribution")
plt.xticks(rotation=45)
plt.show()



