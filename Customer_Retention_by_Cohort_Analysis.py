# -*- coding: utf-8 -*-
"""DAC K28 - Phan Anh Vũ - Hometest_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HMM_mzTPZBClPgcSNdFOrzDHq90guFHV

# I. Preparation
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

org_report = pd.read_csv('/content/drive/MyDrive/KPMG.csv')

"""# II. EDA"""

org_report.head()

org_report.info()

org_report['transaction_date'] = pd.to_datetime(org_report['transaction_date'], format='%d/%m/%Y')

report = org_report[(org_report['order_status'] == 'Approved')]

report.describe()

report.isnull().sum()

report.nunique()

clear_report = report.drop_duplicates()
clear_report = report.dropna(subset=['customer_id'])

"""Conclusion:
- Missing Data:
  - No missing data in primal key (transaction_id) and transaction_date
> **Next Step: Remove Missing Values**
- Duplicates:
  - 179 values in primal key (transaction_id)
> **Next Step: Remove Duplicate Values**
- Incorrect Data Type:
  - transaction_date: object -> datetime64
> **Next Step: Change Data Type**
- Incorrect Value:
  - No incorrect value found
> **Next Step: No Action**

# III. Cohort Analysis

## 1. Calculate Cohort Month:
"""

clear_report['OrderMonth'] = clear_report['transaction_date'].dt.to_period('M')
clear_report['CohortMonth'] = clear_report.groupby('customer_id')['OrderMonth'].transform('min')
clear_report.head()

"""## 2. Cohort Calculation:"""

def calculate_month_difference(row):
    return (row['OrderMonth'].year - row['CohortMonth'].year) * 12 + (row['OrderMonth'].month - row['CohortMonth'].month)
clear_report['CohortIndex'] = clear_report.apply(calculate_month_difference, axis=1)

cohort_data = clear_report.groupby(['CohortMonth', 'CohortIndex'])['customer_id'].nunique().reset_index()
cohort_pivot = cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='customer_id')
cohort_size = cohort_pivot.iloc[:, 0]
retention = cohort_pivot.divide(cohort_size, axis=0)

"""## 3. Cohort Map Visualization:"""

sns.set_theme(style="darkgrid")
plt.figure(figsize=(16, 9))
sns.heatmap(retention, annot=True, fmt=".0%", cmap="YlGnBu")
plt.title('MoM Retention Rate For Customer Transaction Data', fontdict={'fontsize': 20, 'fontweight': 'bold'}, loc='center', pad=12)
plt.ylabel('Cohort Month')
plt.xlabel('Cohort Index')
plt.show()

"""# IV. Insights

- Cohort with higher retention rate:
  - Customer with first order in **07-2017** (up to 48%)
  - Customer with first order in **04-2017**(up to 45%)
  - Customer with first order in **06-2017** (up to 44%)
> It indicates that there may be some successful business or marketing strategies during the period.
- Cohort with lower or sharp drop in retention rate:
  - Customer with first order in **08-2017** (drop from 43% to 25%)
> It is suggested that the business have to do further investigation to identify reasons, such as service changes or ineffective strategies badly affecting this period
- Overall, at mostly 30% or more, KPMG's retention rate in 2017 is **excellent**.

# V. Recommendations

- In order to enhance customer retention throughout the year, KPMG needs to implement compelling preferential policies during the initial months is essential to drive higher order rates over time.
- Retention rates are significantly higher in mid-year months compared to other periods. This calls for an in-depth analysis—supported by relevant data and visualizations—to uncover the underlying factors and strategically apply these insights to improve performance during other months.
"""