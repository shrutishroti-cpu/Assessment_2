# Problem Statement Code
import pandas as pd

# Load the dataset
df = pd.read_excel("C:/Assessment_2/Assessment_2/DataSet.xlsx", engine="openpyxl")


# Convert joining_date to datetime format
df['joining_date'] = pd.to_datetime(df['joining_date'])

# Filter employees who joined in or after April (month >= 4)
april_or_later = df[df['joining_date'].dt.month >= 4]

# Count employees in the 'Admin' department
admin_count = april_or_later[april_or_later['department'] == 'Admin'].shape[0]

print("Below is the solution: ")
print("Number of employees in 'Admin' department who joined in or after April:", admin_count)

































# # Problem Statement Code
# import pandas as pd

# # Load the dataset
# df = pd.read_excel("DataSet.xlsx", engine="openpyxl")

# # Convert joining_date to datetime format
# df['joining_date'] = pd.to_datetime(df['joining_date'])

# # Filter employees who joined in or after April (month >= 4)
# april_or_later = df[df['joining_date'].dt.month >= 4]

# # Group by department and count employees
# employee_counts = april_or_later.groupby('department').size().reset_index(name='employee_count')

# # Sort by employee count in descending order
# sorted_counts = employee_counts.sort_values(by='employee_count', ascending=False)

# # Display the result
# print("Problem Statement Code")
# print("# Count employees by department who joined in or after April")
# print(sorted_counts)
