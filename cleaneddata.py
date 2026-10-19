
import pandas as pd

df = pd.read_csv("data.csv", encoding="ISO-8859-1")

# Remove whitespace from column names
df.columns = df.columns.str.strip()

# Remove completely empty rows
df = df.dropna(how="all").copy()

# Standardize department names
department_map = {
    "BT": "Biotechnology",
    "CE": "Civil Engineering",
    "CSE": "Computer Science & Engineering",
    "ECE": "Electronics & Communication",
    "EE": "Electrical Engineering",
    "TT": "Textile Technology",
    "ME": "Mechanical Engineering",
    "CH": "Chemical Engineering",
    "CY": "Chemistry",
    "IT": "Information Technology",
    "MC": "Mathematics & Computing",
    "ICE": "Instrumentation & Control",
    "IPE": "Industrial & Production",
    "Physics": "Physics",
    "Physcis": "Physics",
    "Textile": "Textile Technology",
}

df["Department"] = (
    df["Department"].astype("string").str.strip()
    .replace(department_map)
    .fillna("Not specified")
)

# Standardize missing text fields
for col in ["Funding Agency", "Status"]:
    df[col] = df[col].fillna("Not specified").astype(str).str.strip()

# Convert numeric funding values
# This simple conversion is only a first pass.
df["Amount"] = pd.to_numeric(
    df["Amount, Rs."].astype(str).str.replace(",", "", regex=False),
    errors="coerce"
)

print(df[["Department", "Funding Agency", "Amount", "Status"]].head())
print("\nMissing funding amounts:", df["Amount"].isna().sum())

# Save a first-pass cleaned file
df.to_csv("cleaned_data.csv", index=False)

print("\nSaved cleaned_data.csv")
