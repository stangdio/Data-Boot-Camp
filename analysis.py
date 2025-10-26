import pandas as pd
import numpy as np
import os

# 1. LOAD THE DATA
df = pd.read_csv('Suspects_Dataset.csv')

# 2. INITIAL EXPLORATION (what you already ran)
print("=== INITIAL DATA OVERVIEW ===")
df.info()
print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

# 3. DEEPER MISSING VALUE ANALYSIS (NEW - add this next)
print("\n=== DETAILED MISSING VALUE ANALYSIS ===")
print("Missing values per column:")
print(df.isnull().sum())
print(f"\nTotal missing values: {df.isnull().sum().sum()}")

# 4. FIND SPECIFIC ROWS WITH MISSING DATA (NEW)
print("\n=== MONSTERS WITH MISSING DATA ===")
missing_rows = df[df.isnull().any(axis=1)]
print(f"Number of monsters with missing data: {len(missing_rows)}")
print(missing_rows[['Monster', 'Age', 'Speed Level', 'Strength Level', 'Favorite Food']])

# 5. Check if certain monster types have more missing data
print("\n=== MISSING VALUES BY MONSTER TYPE ===")
for column in ['Age', 'Speed Level', 'Strength Level', 'Favorite Food']:
    missing_by_monster = df[df[column].isnull()]['Monster'].value_counts()
    if len(missing_by_monster) > 0:
        print(f"\nMissing {column}:")
        print(missing_by_monster)

# 6. Smart Filling of Missing Values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Speed Level'].fillna(df['Speed Level'].median(), inplace=True)
df['Strength Level'].fillna(df['Strength Level'].median(), inplace=True)
df['Favorite Food'].fillna(df['Favorite Food'].mode()[0], inplace=True)

# 7. Verify cleaning worked
print("\n=== AFTER CLEANING ===")
print(df.isnull().sum())
print(f"Total missing values remaining: {df.isnull().sum().sum()}")

df.to_csv('Suspects_Dataset_Cleaned.csv', index=False)
print("Cleaned dataset saved for visualization!")