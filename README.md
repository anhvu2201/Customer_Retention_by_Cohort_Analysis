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
# II. Data & Libraries Preparation
  ![image](https://github.com/user-attachments/assets/3539521d-b056-414f-9686-c3ff3ab5e976)
# III. Exploratory Data Analysis - EDA
## 1. Explore Data:
  ![image](https://github.com/user-attachments/assets/3b0fc118-582d-4b9e-bfde-e6c52c7d50a4)
## 2. Apply Condition & Correct Data Type On Dataset:
  ![image](https://github.com/user-attachments/assets/6010354c-c130-4699-a005-66e86265e9e0)
## 3. Check & Handle Null Values:
  ![image](https://github.com/user-attachments/assets/3eded006-2cae-4bd1-bb59-5e9864a9f601)
  ![image](https://github.com/user-attachments/assets/3af863e5-8395-4d66-ac15-1e9ce570a104)
  - Solution: Remove missing values.
## 4. Check & Handle Duplicate Values:
  ![image](https://github.com/user-attachments/assets/b9c89569-fb3e-4364-8a3e-4fc2e34bf377)
  ![image](https://github.com/user-attachments/assets/47b5f7ab-d312-4bca-8250-564d372d7843)
  - 179 duplicate values in primal key (transaction_id)
  - Solution: Remove duplicate values.
## 5. Conclusion:
  ![image](https://github.com/user-attachments/assets/c820e9e9-9ade-4942-a32d-00ffd6cf4824)
# IV. Cohort Analysis
## 1. Calculate Cohort Month:
  ![image](https://github.com/user-attachments/assets/107611dd-d09c-4438-b3ff-e50519fe3b9a)
## 2. Cohort Calculation:
  ![image](https://github.com/user-attachments/assets/d7f49e4e-ad58-46b7-a0a6-66c8b8aa8c9c)
## 3. Cohort Map Visualization:
  ![image](https://github.com/user-attachments/assets/41c20acd-66cb-43eb-a9b5-67e548d8f166)
# V. Insights
  ![image](https://github.com/user-attachments/assets/03949b44-464f-4732-a391-157146a6cd40)
# VI. Recommendations
  ![image](https://github.com/user-attachments/assets/22601f86-4c82-462d-95ae-657e1461e314)











