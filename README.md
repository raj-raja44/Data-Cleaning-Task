# 🧹 Data Cleaning & Preprocessing with Python

## 📌 Project Overview

This project demonstrates data cleaning and preprocessing using Python and Pandas.

The goal is to transform a raw marketing campaign dataset into a clean and structured dataset that can be used for further data analysis.

## 🎯 Objectives

- Handle missing values
- Remove duplicate records
- Standardize text values
- Convert date columns into the correct format
- Fix column names and data types
- Prepare clean data for further analysis

## 🛠️ Tools & Technologies

- Python
- Pandas
- CSV
- Data Cleaning
- Data Preprocessing

## 🧹 Data Cleaning Performed

The following cleaning operations were performed:

- Handled missing income values using the median
- Removed duplicate records
- Converted column names to lowercase
- Replaced spaces in column names with underscores
- Standardized education and marital status values
- Converted customer dates into datetime format
- Converted year of birth to integer
- Converted income to float

## 📂 Project Files

| File | Description |
|---|---|
| `marketing_campaign.csv` | Original raw marketing campaign dataset |
| `data_cleaning.py` | Python script used for data cleaning |
| `cleaned_customer_data.csv` | Cleaned dataset generated after processing |

## 🔄 Data Cleaning Workflow

```text
Raw Dataset
     ↓
Load Data using Pandas
     ↓
Clean Column Names
     ↓
Handle Missing Values
     ↓
Remove Duplicates
     ↓
Standardize Text
     ↓
Convert Date Format
     ↓
Fix Data Types
     ↓
Cleaned Dataset
