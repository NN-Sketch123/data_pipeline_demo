# Step 1: Import necessary libraries
import pandas as pd # type: ignore
# Step 2: Create a sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
# Step 3: Transform the data - Add a new column for Tax
df["Tax"] = df["Salary"] * 0.2
print("Transformed Data:")
print(df)
# Step 4: Save the transformed data to a CSV file
df.to_csv("transformed_data.csv", index=False)
print("Data saved to transformed_data.csv")
