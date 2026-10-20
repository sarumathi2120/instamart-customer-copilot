
import pandas as pd

# Read the original customer data
customers = pd.read_csv("data/raw/customers.csv")

# Check distinct city values before cleaning
print("Before cleaning:", customers["city"].nunique())

# Standardise city names
customers["city"] = customers["city"].str.strip().str.title()

# Check distinct city values after cleaning
print("After cleaning:", customers["city"].nunique())

# Display customers per city
print(customers["city"].value_counts())

#original gender data before cleaning
print("\nbefore cleaning:",customers["gender"].value_counts())

#strip spaces and change case
customers["gender"]=customers["gender"].str.strip().str.lower()

#replace m ad f with male and female
customers["gender"]=customers["gender"].replace({
    "m":"male",
    "f":"female"
})
#fill the null missing values with unknown
customers["gender"]=customers["gender"].fillna("unknown")

#original gender data after cleaning
print("\nafter cleaning:",customers["gender"].value_counts())
