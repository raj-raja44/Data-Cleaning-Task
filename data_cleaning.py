import pandas as pd

# Load dataset
df = pd.read_csv('marketing_campaign.csv')

# Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Handle missing values
df['income'] = df['income'].fillna(df['income'].median())

# Remove duplicates
df = df.drop_duplicates()

# Standardize text
df['education'] = df['education'].str.lower().str.strip()
df['marital_status'] = df['marital_status'].str.lower().str.strip()

# Convert date
df['dt_customer'] = pd.to_datetime(df['dt_customer'], format='%d-%m-%Y')

# Fix data types
df['year_birth'] = df['year_birth'].astype(int)
df['income'] = df['income'].astype(float)

# Save cleaned data
df.to_csv('cleaned_customer_data.csv', index=False)
print("Data cleaning completed!")
