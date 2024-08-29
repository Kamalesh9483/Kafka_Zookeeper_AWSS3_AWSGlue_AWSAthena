import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Create a list of dates
dates = pd.date_range(start='2023-01-01', end='2024-01-01', periods=500)

# Generate data
data = {
    'Date': dates,
    'ID': [fake.unique.random_number(digits=5) for _ in range(500)],
    'Name': [fake.name() for _ in range(500)],
    'Age': [random.randint(18, 70) for _ in range(500)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('dataset.csv', index=False)

print("CSV file created successfully.")