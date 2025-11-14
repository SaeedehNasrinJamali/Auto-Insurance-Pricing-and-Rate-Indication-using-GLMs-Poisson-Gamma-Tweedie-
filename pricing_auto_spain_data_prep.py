import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os
os.makedirs("outputs/figures", exist_ok=True)
data_cols = [
    "ID", "Date_start_contract", "Date_last_renewal", "Date_next_renewal",
    "Date_birth", "Date_driving_licence", "Distribution_channel", "Seniority",
    "Policies_in_force", "Max_policies", "Max_products", "Lapse", "Date_lapse",
    "Payment", "Premium", "Cost_claims_year", "N_claims_year", "N_claims_history",
    "R_Claims_history", "Type_risk", "Area", "Second_driver", "Year_matriculation",
    "Power", "Cylinder_capacity", "Value_vehicle", "N_doors", "Type_fuel",
    "Length", "Weight"
]

path = "data/motor_vehicle_insurance_data.csv"
df = pd.read_csv(path, sep=";", header=0)

df.head(10)

# Filter and create the severity variable
df = df[df["N_claims_year"] > 0]
df["severity"] = df["Cost_claims_year"] / df["N_claims_year"]

# Feature Engineering
date_cols = ["Date_birth", "Date_driving_licence"]
for c in date_cols:
    df["Date_birth"] = pd.to_datetime(df["Date_birth"], format="%d/%m/%Y", errors="coerce")

# Data Cleaning and Transfrming
df_gamma

df["Date_birth"] = pd.to_datetime(df["Date_birth"], errors="coerce", dayfirst=True)
df["Date_driving_licence"] = pd.to_datetime(df["Date_driving_licence"], errors="coerce", dayfirst=True)
df["Year_matriculation"] = pd.to_numeric(df["Year_matriculation"], errors="coerce")

#Engineer features on df 
REF_YEAR = 2025
df["Age"] = (REF_YEAR - df["Date_birth"].dt.year).clip(lower=0)
df["Driving_experience"] = (REF_YEAR - df["Date_driving_licence"].dt.year).clip(lower=0)
df["Vehicle_age"] = (REF_YEAR - df["Year_matriculation"]).clip(lower=0)

# Now subset to df_gamma
cat_cols = ["Type_risk", "Area", "Type_fuel", "Second_driver", "Distribution_channel"]
num_cols = ["Power","Cylinder_capacity","Value_vehicle","Length","Weight",
            "Seniority","Premium","Vehicle_age","Age","Driving_experience","N_claims_history"]

df_gamma = df.loc[:, cat_cols + num_cols + ["severity"]].copy()

df_gamma

# Exploratory Data Analysis (EDA)

df_gamma.describe()

df_gamma.info()



num_cols = ["Power","Cylinder_capacity","Value_vehicle","Length","Weight",
            "Seniority","Premium","Vehicle_age","Age","Driving_experience","N_claims_history"]
for col in num_cols:
    plt.figure()
    sns.histplot(df_gamma[col], kde=True)
    plt.title(f"Distribution of {col}")
    # NEW: save each numeric histogram
    plt.savefig(f"outputs/figures/hist_{col}.png", bbox_inches="tight")
    plt.show()

# Severity Distribution
plt.figure(figsize=(8,4))
sns.histplot(df["severity"], bins=50, kde=True)
plt.xscale("log")
plt.title("Distribution of Severity (log scale)")
plt.xlabel("Severity (log scale)")
plt.ylabel("Count")
# NEW: save severity log histogram
plt.savefig("outputs/figures/severity_log_hist.png", bbox_inches="tight")
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(12,4))

# Left: Original scale
sns.histplot(df["severity"], bins=50, kde=True, ax=axes[0])
axes[0].set_title("Severity (Original Scale)")
axes[0].set_xlabel("Severity")
axes[0].set_ylabel("Count")

# Right: Log scale
sns.histplot(df["severity"], bins=50, kde=True, ax=axes[1])
axes[1].set_xscale("log")
axes[1].set_title("Severity (Log Scale)")
axes[1].set_xlabel("Severity (log scale)")
axes[1].set_ylabel("Count")

plt.tight_layout()
# NEW: save the side-by-side plot
fig.savefig("outputs/figures/severity_original_vs_log.png", bbox_inches="tight")
plt.show()

# Target boxplot
sns.boxplot(x=df_gamma["severity"])
plt.title("Severity Outliers")
# NEW: save boxplot
plt.savefig("outputs/figures/severity_boxplot.png", bbox_inches="tight")
plt.show()

#encoding the categorical variables
df_model = pd.get_dummies(df_gamma, columns=cat_cols, drop_first=True)
#  Handle missing values in Length 
df_model.isna().sum()  
median_length = df_model["Length"].median()
df_model["Length"] = df_model["Length"].fillna(median_length)
# Save cleaned model-ready dataset 
os.makedirs("outputs/clean_data", exist_ok=True)
df_model.to_csv("outputs/clean_data/df_model_clean.csv", index=False)
