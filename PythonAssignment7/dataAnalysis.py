# ========================
# 📊 Task 1: Load and Explore Dataset
# ========================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Error handling for dataset loading
try:
    # Load iris dataset
    iris = load_iris(as_frame=True)
    df = iris.frame  # Convert to pandas DataFrame
    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ File not found. Please check the path.")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")

# Display first 5 rows
print("🔹 First 5 rows of the dataset:")
print(df.head())

# Check data info
print("\n🔹 Dataset Info:")
print(df.info())

# Check for missing values
print("\n🔹 Missing values:")
print(df.isnull().sum())

# Clean dataset (fill or drop missing values if any)
df = df.dropna()  # In Iris dataset, there are no missing values


# ========================
# 📊 Task 2: Basic Data Analysis
# ========================

# Summary statistics
print("\n🔹 Summary statistics:")
print(df.describe())

# Grouping example: mean petal length per species
grouped = df.groupby("target")["petal length (cm)"].mean()
print("\n🔹 Average Petal Length per Species:")
print(grouped)

# Replace target numbers with species names
df["species"] = df["target"].map(dict(enumerate(iris.target_names)))


# ========================
# 📊 Task 3: Data Visualization
# ========================

# Set style
sns.set(style="whitegrid")

# 1. Line Chart (trend of sepal length over samples)
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart: Sepal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart (average petal length per species)
plt.figure(figsize=(8, 5))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None)
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(8, 5))
plt.hist(df["sepal width (cm)"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (sepal length vs petal length)
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()


# ========================
# 📊 Findings / Observations
# ========================

print("\n🔹 Findings / Observations:")
print("- Setosa flowers tend to have shorter petal lengths compared to other species.")
print("- Versicolor and Virginica have overlapping sepal lengths but differ in petal dimensions.")
print("- Sepal width is normally distributed around ~3 cm.")
print("- Strong positive correlation between sepal length and petal length.")
