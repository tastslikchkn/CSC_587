import pandas as pd
import numpy as np

data = {
    'Department': ['sales', 'sales', 'sales', 'systems', 'systems', 'systems', 'systems', 'marketing', 'marketing', 'secretary', 'secretary'],
    'Age': ['31_35', '26_30', '31_35', '21_25', '31_35', '26_30', '41_45', '36_40', '31_35', '46_50', '26_30'],
    'Salary': ['46K_50K', '26K_30K', '31K_35K', '46K_50K', '66K_70K', '46K_50K', '66K_70K', '46K_50K', '41K_45K', '36K_40K', '26K_30K'],
    'Status': ['senior', 'junior', 'junior', 'junior', 'senior', 'junior', 'senior', 'senior', 'junior', 'senior', 'junior'],
    'Count': [30, 40, 40, 20, 5, 3, 3, 10, 4, 4, 6]
}

df = pd.DataFrame(data)

print(df)   

# Assuming df is your DataFrame and 'Status' is your target variable

# Calculate the entropy of the target variable
p_junior = df[df['Status'] == 'junior'].shape[0] / df.shape[0]
p_senior = df[df['Status'] == 'senior'].shape[0] / df.shape[0]
entropy_target = -p_junior*np.log2(p_junior) - p_senior*np.log2(p_senior)
print(f'Entropy of target variable: {entropy_target}')

# Calculate the entropy of each attribute and the information gain
# for attribute in df.columns.drop('Status'):
#     entropy_attribute = 0
#     for category in df[attribute].unique():
#         df_category = df[df[attribute] == category]
#         p_junior = df_category[df_category['Status'] == 'junior'].shape[0] / df_category.shape[0]
#         p_senior = df_category[df_category['Status'] == 'senior'].shape[0] / df_category.shape[0]
#         entropy_category = -p_junior*np.log2(p_junior) - p_senior*np.log2(p_senior)
#         entropy_attribute += df_category.shape[0] / df.shape[0] * entropy_category
#     information_gain = entropy_target - entropy_attribute
#     print(f'Information gain for {attribute}: {information_gain}')