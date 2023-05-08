import pandas as pd
import random
from datetime import datetime, timedelta

# Helper function to generate random timestamps
def random_timestamp(start, end):
    random_time = start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
    return random_time

# Parameters
num_records = 50
num_users = 10
start_time = datetime(2023, 1, 1)
end_time = datetime(2023, 5, 3)

# Generate dataset
records = []
events = ['login', 'password_change', 'profile_update']
ip_addresses = [f'192.168.0.{i}' for i in range(1, num_users + 1)]

for _ in range(num_records):
    user_id = random.randint(1, num_users)
    timestamp = random_timestamp(start_time, end_time)
    ip_address = random.choice(ip_addresses)
    event = random.choice(events)
    
    genuine = random.random() > 0.3  # 70% chance of a genuine record
    label = 'genuine' if genuine else 'attack'
    
    # Introduce false positives
    if genuine and random.random() < 0.1:  # 10% chance of a genuine record being labeled as an attack
        label = 'attack'
    
    record = {'timestamp': timestamp, 'user_id': user_id, 'ip_address': ip_address, 'event': event, 'label': label}
    records.append(record)

# Create a DataFrame and sort by timestamp
df = pd.DataFrame(records)
df.sort_values('timestamp', inplace=True)
df.reset_index(drop=True, inplace=True)

# Save the dataset as a CSV file
df.to_csv('identity_security_dataset.csv', index=False)

# Display the dataset
print(df)
