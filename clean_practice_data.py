import pandas as pd
import numpy as np
import nbformat as nbf
import re
from datetime import datetime

# 1. LOAD RAW DATA
raw_df = pd.read_excel('downloaded_materials/Practice_Dataset.xlsx', sheet_name='Raw_Data')

# 2. CLEAN DATA AS TAUGHT IN MASTERCLASS 1
# Clean Revenue
def clean_currency(val):
    if pd.isna(val):
        return np.nan
    s = str(val)
    s = re.sub(r'[^\d.-]', '', s)
    try:
        return float(s)
    except:
        return np.nan

raw_df['Revenue_Clean'] = raw_df['Revenue'].apply(clean_currency)
raw_df['Profit_Clean'] = pd.to_numeric(raw_df['Profit'], errors='coerce')
raw_df['Quantity_Clean'] = pd.to_numeric(raw_df['Quantity'], errors='coerce').abs() # fix negative quantity

# Clean Dates
def parse_date(val):
    if pd.isna(val):
        return pd.NaT
    if isinstance(val, (datetime, pd.Timestamp)):
        return val
    s = str(val).strip()
    if '31-02' in s or '29-02' in s and '2026' in s: # impossible date fix to 28-02-2026
        s = '28-02-2026'
    for fmt in ('%Y-%m-%d %H:%M:%S', '%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y', '%Y/%m/%d'):
        try:
            return pd.to_datetime(s, format=fmt)
        except:
            pass
    return pd.to_datetime(s, errors='coerce')

raw_df['Order_Date_Clean'] = raw_df['Order_Date'].apply(parse_date)
raw_df['Order_Date_Clean'] = raw_df['Order_Date_Clean'].fillna(pd.to_datetime('2026-03-01'))

# Fill missing revenue/profit with median
raw_df['Revenue_Clean'] = raw_df['Revenue_Clean'].fillna(raw_df['Revenue_Clean'].median())
raw_df['Profit_Clean'] = raw_df['Profit_Clean'].fillna(raw_df['Profit_Clean'].median())
raw_df['Quantity_Clean'] = raw_df['Quantity_Clean'].fillna(1.0)

# Enrichment (Masterclass 1)
raw_df['Month'] = raw_df['Order_Date_Clean'].dt.month_name()
raw_df['Year'] = raw_df['Order_Date_Clean'].dt.year

order_counts = raw_df.groupby('Customer_ID')['Order_ID'].transform('count')
raw_df['Customer_Segment'] = np.where(order_counts > 1, 'Repeat Customer', 'New Customer')

raw_df['Order_Value_Category'] = pd.qcut(raw_df['Revenue_Clean'], q=3, labels=['Low', 'Medium', 'High'])

cleaned_csv_path = 'cleaned_ecommerce_data.csv'
raw_df.to_csv(cleaned_csv_path, index=False)
print(f"Saved cleaned dataset: {cleaned_csv_path} with {len(raw_df)} records.")
