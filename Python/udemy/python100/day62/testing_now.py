import pandas as pd

# Read CSV file into DataFrame
df = pd.read_csv('cafe-data.csv', encoding='utf-8')

# Convert DataFrame to JSON
json_data = df.to_json(orient='records', force_ascii=False)

# Print or use JSON data
print(json_data)