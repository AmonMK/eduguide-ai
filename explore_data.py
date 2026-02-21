# EduGuide AI - Step 1: Load and Explore the Data
import pandas as pd

# Load the dataset
df = pd.read_csv('data/student-mat.csv', sep=',')

# Let's see what we're working with
print("=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== SHAPE (rows, columns) ===")
print(df.shape)

print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())

print("\n=== BASIC STATS ===")
print(df.describe())

print("\n=== ANY MISSING VALUES? ===")
print(df.isnull().sum())
