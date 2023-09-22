import pandas as pd

# Specify the CSV file name
file_name = 'sales_data.csv'

# Load the sales data from a CSV file into a DataFrame
sales_data = pd.read_csv(file_name)

# Specify the product category you want to analyze
target_category = 'Electronics'

# Filter the DataFrame to select rows with the target category
filtered_data = sales_data[sales_data['Category'] == target_category]

# Calculate the total sales amount for the target category
total_sales_amount = filtered_data['Sales'].sum()

# Print the result
print(f'Total sales amount for {target_category}: ${total_sales_amount:.2f}')
