# Problem Statement Code
import pandas as pd

# Loading the dataset
df = pd.read_excel("C:/Assessment_2/Assessment_2/DataSet.xlsx", engine="openpyxl")

# Converting joining_date to datetime format
df['joining_date'] = pd.to_datetime(df['joining_date'])

# Filtering employees who joined in or after April (month >= 4)
april_or_later = df[df['joining_date'].dt.month >= 4]

# Counting employees in HR and Account departments
hr_count = april_or_later[april_or_later['department'] == 'HR'].shape[0]
account_count = april_or_later[april_or_later['department'] == 'Account'].shape[0]

# If counts are identical
identical = hr_count == account_count

print("Below is the solution: ")
print("If HR and Account departments have identical employee counts for joining in or after April")
print("HR count:", hr_count)
print("Account count:", account_count)
print("Are counts identical?", identical)
