
import pandas as pd

# ==========================================
# STEP 1: Read the raw CSV files
# ==========================================

customers = pd.read_csv("data/raw/customers.csv")
products = pd.read_csv("data/raw/products.csv")
orders = pd.read_csv("data/raw/orders.csv")


# ==========================================
# STEP 2: Inspect customer data
# ==========================================

print("\nFIRST FIVE CUSTOMER RECORDS")
print(customers.head())

print("\nCUSTOMER DATASET SHAPE")
print(customers.shape)

print("\nCUSTOMER COLUMN NAMES")
print(customers.columns.tolist())

print("\nCUSTOMER DATA TYPES")
print(customers.dtypes)


# ==========================================
# STEP 3: Check customer missing values
# ==========================================

print("\nCUSTOMER MISSING VALUES")
print(customers.isna().sum())

print("\nCUSTOMER MISSING PERCENTAGES")
print((customers.isna().mean() * 100).round(2))

# ==========================================
# STEP 5: Audit order duplicates and status
# ==========================================

print("\nTOTAL RAW ORDER ROWS")
print(len(orders))

print("\nEXACT DUPLICATE ORDER ROWS")
print(orders.duplicated().sum())

print("\nPENDING ORDER ROWS")
print((orders["status"] == "pending").sum())

print("\nUNIQUE ORDER IDS")
print(orders["order_id"].nunique())


# ==========================================
# STEP 6: Identify invalid order amounts
# ==========================================
amounts=pd.to_numeric(
    orders["order_amount"],
    errors="coerce"
)
invalid_amounts=amounts.isna().sum()
print(invalid_amounts)

# ==========================================
# STEP 7: Find negative delivery durations
# ==========================================
delivery_duration=pd.to_numeric(
    orders["delivery_minutes"],
    errors="coerce"
)
negative_minutes=(delivery_duration<0).sum()
print(negative_minutes)

# ==========================================
# STEP 8:Blank delivery durations
# ==========================================
blank_delivery=delivery_duration.isna().sum()
print(blank_delivery)

# ==========================================
# STEP 8:unique city spellings
# ==========================================
print("\nUNIQUE CITY SPELLINGS")
city_spellings=customers["city"].nunique()
print(city_spellings)
city_spellings_list=customers["city"].unique()
print(city_spellings_list)

print("\nUNIQUE GENDER SPELLINGS")
print(customers["gender"].dropna().nunique())

print("\nGENDER VALUES")
print(customers["gender"].dropna().unique())

print("\nINVALID AGES")
invalid_age=(
    (customers["age"]<10) | (customers["age"]>100)
)

print(invalid_age.sum())


