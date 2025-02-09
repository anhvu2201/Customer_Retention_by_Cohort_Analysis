# Customer_Retention_by_Cohort_Analysis
# I. Introduction
## 1. Introduction to Cohort analysis:
- Cohort analysis is an analysis technique used to measure user engagement over time. It helps to know whether user engagement is actually getting better over time or is only appearing to improve because of growth. Customers are divided into mutually exclusive cohorts, which are then tracked over time. Its primary goal is to track and understand how specific groups interact with a product or service over time, identifying trends, problems, or opportunities for improvement.
- Generally, there are three major types of Cohort:
  - Time cohorts: for customers who signed up for a product or service during a particular time frame.
  - Behavior cohorts: for customers who purchased a product or subscribed to service in the past.
  - Size cohorts: refer to the various sizes of customers who purchase the company’s products or services.
- In this project, **Time cohort** will be focused. Customers will be grouped into acquisition cohorts based on the month of their initial purchase. A cohort index will then be attributed to each of the customer's transactions, reflecting the number of months since their first purchase.
## 2. Project Purpose:
- Progress KPMG transaction data to make a cohort retention rate map.
- Evaluate user engagement from their first transaction using the cohort map.
# II. Data Cleaning & Processing
## 1. Data Preparation:
  ![image](https://github.com/user-attachments/assets/bc470faf-6c73-4f5d-85a6-1b98f78ece62)
## 2. Explore Data:
  ![image](https://github.com/user-attachments/assets/5e9a7b27-084c-4518-ba4f-bdb5594cfda4)
## 3. Apply Condition & Correct Data Type On Dataset:
  ![image](https://github.com/user-attachments/assets/292b7592-4d4e-43cd-b5c9-1493a235b994)
## 4. Check & Handle Null Values:
  ![image](https://github.com/user-attachments/assets/cdfe19dc-7a5e-4dcb-8e1c-8882bc056c3a)
  ![image](https://github.com/user-attachments/assets/ccb1edba-585e-4788-8723-2d4444dbfc46)
  - Solution: Remove missing values.
## 5. Check & Handle Duplicate Values:
  ![image](https://github.com/user-attachments/assets/018f83af-46eb-4c22-8b31-7c9852c536ec)
  ![image](https://github.com/user-attachments/assets/52647bc9-bacf-4bbd-a109-31e324e0ccd7)
  - 179 duplicate values in primal key (transaction_id)
  - Solution: Remove duplicate values.
## 6. Conclusion:
  - Missing Data:
    - No action needed: No missing data in primal key (transaction_id) and transaction_date.
  - Duplicate Data:
    - Remove duplicate data: 179 duplicate values in primal key (transaction_id).
  - Incorrect Data Type:
    - Change data type: For 'transaction_date': from 'object' to 'datetime64'.
  - Incorrect Data Value:
    - No action needed: No incorrect value found.
# III. Cohort Analysis
## 1. Calculate Cohort Month:
  ![image](https://github.com/user-attachments/assets/c5bdefc9-5cd6-48f0-9c9d-cda01feb0eda)
  - Extract CohortMonth of customers by transforming transaction_date column into Year-Month format and finding the first purchase date of each customers (minimum purchase date).
## 2. Cohort Calculation:
  ![image](https://github.com/user-attachments/assets/11410e4a-b565-49be-9443-6961929cc8ca)
  - Calculate Cohort Index (by subtracting OrderMonth to CohortMonth.
  - Group data by CohortMonth and CohortIndex with unique customers' ID.
  - Create Cohort Pivot Table with CohortMonth as rows and CohortIndex as columns.
  - Calculate Customer Retention Rate by dividing each rows in cohort_pivot to cohort_size (number of customers in each cohort in first column).
## 3. Cohort Map Visualization:
  ![image](https://github.com/user-attachments/assets/75b9848b-3b07-4cff-98c8-d4cc1d14c548)
  - Illustrate the retention rate for each cohort group using a cohort heat map to see the insights and trends.
# IV. Insights & Recommendations
## 1. Insights:
  ![image](https://github.com/user-attachments/assets/edb83963-d084-4579-be2b-a2e9afc6e154)
## 2. Recommendations:
  ![image](https://github.com/user-attachments/assets/a8364f03-d105-4692-8c71-f752eaad9ed2)












