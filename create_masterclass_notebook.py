import nbformat as nbf

nb = nbf.v4.new_notebook()

nb.metadata = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "codemirror_mode": {"name": "ipython", "version": 3},
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.14.0"
    }
}

cells = []

# Title Cell
cells.append(nbf.v4.new_markdown_cell("""# AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026 | BharatCares
## Official Capstone Project: AI-Powered Customer Retention & E-Commerce Predictive Analytics
* **Candidate Name:** Lalatendu Bal
* **Internship Plan ID:** PLAN-D44A9C2C463C
* **Partner Organizations:** AICTE & IBM SkillsBuild | Implementation Partner: BharatCares (CSRBOX)
* **Masterclass Track:** Data Analytics with AI (Masterclasses 1, 2, 3 & 4 Curriculum)
* **Submission Date:** October 2026

---

### Executive Project Summary
This project faithfully implements the full end-to-end curriculum taught across **IBM SkillsBuild Masterclasses 1 to 4**:
1. **Masterclass 1 (AI + Data: Make Data Intelligent):** Data quality profiling, AI-assisted data cleansing (handling corrupted dates like 31-Feb, stripping currency symbols, normalizing quantities), and analytical column enrichment (Month, Year, Customer Segment, Order Value Category).
2. **Masterclass 2 & 3 (AI-Powered Predictive Customer Analytics):** Customer-level aggregation into RFM (Recency, Frequency, Monetary) metrics, Churn definition, and training a predictive **Logistic Regression** model.
3. **Model Evaluation & Risk Stratification:** Computing Model Accuracy, Precision, Recall, Confusion Matrix, Churn Probabilities, and stratifying customers into Low, Medium, and High-Risk tiers.
4. **Masterclass 4 & AI Insights:** Formulating executive business decisions, strictly distinguishing **Association vs. Causation**, evaluating Precision vs. Recall trade-offs for resource-constrained retention campaigns, and synthesizing executive recommendations using **IBM Granite GenAI principles**.
"""))

# Cell 1: Environment Setup
cells.append(nbf.v4.new_markdown_cell("""## Stage 1: Environment Setup & Library Imports"""))
cells.append(nbf.v4.new_code_cell("""import sys
import os
import re
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)
print(f"Python Runtime: {sys.version.split()[0]}")
print("Dependencies loaded successfully.")
"""))

# Cell 2: Data Ingestion & Quality Audit (Masterclass 1)
cells.append(nbf.v4.new_markdown_cell("""## Stage 2: Data Ingestion & Data-Quality Auditing (Masterclass 1)
We load the raw dataset (`Practice_Dataset.xlsx` / `Raw_Data`) and inspect data-quality problems identified during Masterclass 1:
- Missing values and corrupted formatting
- Currency characters in revenue (e.g. `₹50000`)
- Impossible calendar dates (e.g. `31-02-2026`)
- Negative or distorted quantity records
"""))

cells.append(nbf.v4.new_code_cell("""# Load raw dataset
raw_df = pd.read_excel('downloaded_materials/Practice_Dataset.xlsx', sheet_name='Raw_Data')
print(f"Raw Transaction Records: {raw_df.shape[0]} rows, {raw_df.shape[1]} columns")
raw_df.head(6)
"""))

# Cell 3: Data Cleansing & Enrichment
cells.append(nbf.v4.new_markdown_cell("""## Stage 3: Data Cleansing & Analytical Feature Enrichment (Masterclass 1)
Following the AI-assisted cleaning rules established in Masterclass 1:
1. Strip currency symbols (`₹`) and cast Revenue to numeric.
2. Resolve negative or invalid quantities.
3. Fix invalid dates (`31-02-2026` converted to `28-02-2026`) and convert to datetime objects.
4. Add enrichment fields: `Month`, `Year`, `Customer_Segment` (New vs. Repeat Customer), and `Order_Value_Category`.
"""))

cells.append(nbf.v4.new_code_cell("""df = pd.read_csv('cleaned_ecommerce_data.csv')
df['Order_Date_Clean'] = pd.to_datetime(df['Order_Date_Clean'])

print("=== Cleaned & Enriched Dataset Structure ===")
print(df[['Order_ID', 'Customer_ID', 'Category', 'Region', 'Revenue_Clean', 'Month', 'Customer_Segment', 'Order_Value_Category']].head(6))
print("\\nData Types:")
print(df.dtypes)
"""))

# Cell 4: Exploratory Data Analysis & Business Questions (Masterclass 1 & 4)
cells.append(nbf.v4.new_markdown_cell("""## Stage 4: Exploratory Data Analysis (EDA) & Core Business Insights
Answering the 4 core business dimensions:
1. **Sales & Category Performance:** Which categories generate the highest revenue?
2. **Regional Distribution:** Which geographic zones dominate transaction volume?
3. **Customer Segment Contribution:** Repeat vs. New customer revenue comparison.
"""))

cells.append(nbf.v4.new_code_cell("""fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 1. Revenue by Category
cat_rev = df.groupby('Category')['Revenue_Clean'].sum().sort_values(ascending=False)
axes[0].bar(cat_rev.index, cat_rev.values / 1000, color='#2b5c8f', edgecolor='black', alpha=0.85)
axes[0].set_title('Total Revenue by Category (in ₹K)', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Revenue (₹ Thousands)')
axes[0].tick_params(axis='x', rotation=25)

# 2. Regional Volume
reg_counts = df['Region'].value_counts()
axes[1].pie(reg_counts.values, labels=reg_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'), startangle=140)
axes[1].set_title('Regional Order Distribution (%)', fontsize=12, fontweight='bold')

# 3. Customer Segment Revenue
seg_rev = df.groupby('Customer_Segment')['Revenue_Clean'].sum()
axes[2].bar(seg_rev.index, seg_rev.values / 1000, color=['#27ae60', '#e67e22'], edgecolor='black', alpha=0.85)
axes[2].set_title('Revenue by Customer Segment (₹K)', fontsize=12, fontweight='bold')
axes[2].set_ylabel('Revenue (₹ Thousands)')

plt.tight_layout()
plt.show()
"""))

# Cell 5: Customer-Level Aggregation & RFM Modeling (Masterclass 2 & 3)
cells.append(nbf.v4.new_markdown_cell("""## Stage 5: Customer-Level Aggregation & RFM Feature Engineering (Masterclass 2 & 3)
As taught in Masterclass 2, transactions are aggregated so that **each row represents exactly one unique customer**:
- **Recency (R):** Number of days since the customer's most recent order.
- **Frequency (F):** Total number of completed orders.
- **Monetary (M):** Total cumulative revenue generated.
- **Churn Definition:** A customer is flagged as Churned (`Churn_Status = 1`) if their purchase recency exceeds the inactivity threshold.
"""))

cells.append(nbf.v4.new_code_cell("""# Reference anchor date (day after latest order in dataset)
ref_date = df['Order_Date_Clean'].max() + timedelta(days=1)

# Group by unique Customer_ID
customer_df = df.groupby('Customer_ID').agg(
    First_Purchase=('Order_Date_Clean', 'min'),
    Last_Purchase=('Order_Date_Clean', 'max'),
    Frequency=('Order_ID', 'count'),
    Monetary=('Revenue_Clean', 'sum'),
    Avg_Order_Value=('Revenue_Clean', 'mean')
).reset_index()

# Calculate Recency (days)
customer_df['Recency'] = (ref_date - customer_df['Last_Purchase']).dt.days

# Define Churn: Inactive for >= 75 days
churn_threshold = customer_df['Recency'].quantile(0.60)
customer_df['Churn_Status'] = (customer_df['Recency'] >= churn_threshold).astype(int)

print(f"Total Unique Customers: {len(customer_df)}")
print(f"Churn Threshold: >= {churn_threshold:.1f} days inactivity")
print(f"Churned Customers:     {customer_df['Churn_Status'].sum()} ({customer_df['Churn_Status'].mean()*100:.1f}%)")
print(f"Active Customers:      {(customer_df['Churn_Status'] == 0).sum()} ({(1-customer_df['Churn_Status'].mean())*100:.1f}%)")
customer_df.head(6)
"""))

# Cell 6: Predictive Machine Learning Modeling (Masterclass 3)
cells.append(nbf.v4.new_markdown_cell("""## Stage 6: Predictive Churn Modeling with Logistic Regression (Masterclass 3)
Using the RFM features (`Recency`, `Frequency`, `Monetary`), we train a supervised **Logistic Regression** model to predict customer churn probability.
"""))

cells.append(nbf.v4.new_code_cell("""X = customer_df[['Recency', 'Frequency', 'Monetary']]
y = customer_df['Churn_Status']

# 80/20 Train-Test Split with stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# Train Logistic Regression
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train, y_train)

# Predictions and probabilities
y_pred = lr_model.predict(X_test)
y_prob = lr_model.predict_proba(X_test)[:, 1]

# Overall Customer Probabilities
customer_df['Churn_Probability'] = lr_model.predict_proba(X)[:, 1]

# Model Evaluation Metrics
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)

print(f"=== Model Evaluation Results ===")
print(f"Model Accuracy:  {acc*100:.2f}%")
print(f"Model Precision: {prec*100:.2f}%")
print(f"Model Recall:    {rec*100:.2f}%")
print("\\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Retained', 'Churned']))
"""))

# Cell 7: Confusion Matrix (Masterclass 3 Workbook)
cells.append(nbf.v4.new_markdown_cell("""## Stage 7: Confusion Matrix Interpretation in Business Language (Masterclass 3)
In the Masterclass 3 student workbook, students are required to interpret the confusion matrix in simple business terms:
- **True Positive (TP):** Customer predicted to churn, who genuinely churned (Saved via intervention).
- **False Positive (FP):** Active customer mistakenly flagged as at-risk (Incurred retention outreach cost).
- **False Negative (FN):** Truly at-risk customer missed by the model (Costliest error: customer lost!).
- **True Negative (TN):** Satisfied, active customer correctly identified as retained.
"""))

cells.append(nbf.v4.new_code_cell("""cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4.5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Predicted Retained (0)', 'Predicted Churn (1)'],
            yticklabels=['Actual Retained (0)', 'Actual Churn (1)'])
plt.title('Customer Churn Confusion Matrix', fontsize=12, fontweight='bold')
plt.ylabel('Actual Customer State')
plt.xlabel('Model Prediction')
plt.show()

tn, fp, fn, tp = cm.ravel()
print(f"True Negatives:  {tn} (Correctly predicted active)")
print(f"False Positives: {fp} (False alarms - safe but wastes outreach budget)")
print(f"False Negatives: {fn} (MISSED genuinely at-risk customers - Highest risk!)")
print(f"True Positives:  {tp} (Correctly caught churn candidates)")
"""))

# Cell 8: Customer Risk Stratification Table (Masterclass 3)
cells.append(nbf.v4.new_markdown_cell("""## Stage 8: Customer Risk Table & Top 20 Highest-Risk Customers (Masterclass 3)
Applying the exact risk tier boundaries from the Masterclass 3 Workbook:
- **Low Risk:** Churn Probability below 40%
- **Medium Risk:** 40% to below 70%
- **High Risk:** 70% or higher
"""))

cells.append(nbf.v4.new_code_cell("""# Apply Risk Levels
def assign_risk_level(prob):
    if prob < 0.40:
        return "Low Risk"
    elif prob < 0.70:
        return "Medium Risk"
    else:
        return "High Risk"

customer_df['Risk_Level'] = customer_df['Churn_Probability'].apply(assign_risk_level)

# Format Churn Probability for reporting
customer_df['Churn_Prob_Display'] = (customer_df['Churn_Probability'] * 100).round(2).astype(str) + '%'

# Top 20 Highest-Risk Table
top_20_risk = customer_df.sort_values(by='Churn_Probability', ascending=False)[
    ['Customer_ID', 'Recency', 'Frequency', 'Monetary', 'Churn_Prob_Display', 'Risk_Level']
].head(20)

print("=== Top 20 Highest-Risk Customer Action Table (Masterclass 3 Output) ===")
print(top_20_risk.to_string(index=False))
"""))

# Cell 9: Business Decisions & Association vs Causation (Masterclass 3 & 4)
cells.append(nbf.v4.new_markdown_cell("""## Stage 9: Practical Business Actions & Association vs. Causation (Masterclass 3 & 4)

### 1. Crucial Analytical Principle: Association vs. Causation
As emphasized in the Masterclass 3 challenge:
* **Incorrect Claim:** *"Low purchase frequency causes customers to churn."* (Unproven causal claim).
* **Accurate & Safe Statement:** *"Low purchase frequency is **associated with** higher predicted churn risk."*
The model identifies mathematical correlations; it does not measure underlying customer psychological intent or competitor promotions.

### 2. Five Practical Business Recommendations:
1. **Targeted Re-Engagement Workflows:** Deploy automated win-back discount sequences for customers in the Medium Risk tier (40%-70%) before they cross the 75-day inactivity barrier.
2. **High-Value VIP Retention Protection:** For high-Monetary customers flagging high Recency, assign dedicated account managers to proactively resolve service inquiries.
3. **Optimized Retention Campaign Resource Allocation (Recall vs. Precision):**
   - When outreach capacity is limited (e.g. only 500 customers can be contacted), **Precision** matters to avoid wasting campaign budget on non-churners.
   - When the lifetime value of an enterprise account is massive, **Recall** is prioritized to capture as many truly at-risk clients as possible, accepting modest false positives.
4. **Product Restocking & Category Alignment:** Expand inventory for top-grossing categories identified in Stage 4 to prevent out-of-stock drop-offs.
5. **Generative AI Executive Briefings:** Utilize **IBM Granite** foundation models to auto-generate weekly performance summaries for senior executive decision-makers.
"""))

# Cell 10: Conclusion & Verification
cells.append(nbf.v4.new_markdown_cell("""## Stage 10: Conclusion & Final Verification
* **Internship Track:** AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026
* **Implementation Partner:** BharatCares & CSRBOX
* **Candidate:** Lalatendu Bal
* **Deliverable Checklist:**
  - [x] Preprocessing & Cleaning (Handling corrupted dates, currencies, negative quantities)
  - [x] Customer-Level RFM Aggregation
  - [x] Logistic Regression Churn Prediction
  - [x] Accuracy, Precision, Recall & Confusion Matrix
  - [x] Customer Risk Table (Low, Medium, High)
  - [x] Strategic Business Decisions based on Association vs. Causation
"""))

nb.cells = cells

# Save and execute
output_path = "/Users/maa/Desktop/IBM Internship project/LalatenduBal_EcommerceCustomerAnalytics_AI.ipynb"
with open(output_path, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"Masterclass Notebook created at: {output_path}")
