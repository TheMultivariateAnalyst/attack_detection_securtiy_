import pandas as pd

# Load the dataset
data = pd.read_csv('identity_security_dataset.csv', parse_dates=['timestamp'])

# Calculate the time difference between events for each user
data['time_diff'] = data.groupby('user_id')['timestamp'].diff().dt.total_seconds().fillna(0)

# Calculate the frequency of certain event types for each user
event_counts = data.groupby(['user_id', 'event']).size().unstack(fill_value=0)
event_counts = event_counts.add_suffix('_count')
data = data.join(event_counts, on='user_id')

# Save the updated dataset as a CSV file
data.to_csv('identity_security_dataset_engineered.csv', index=False)

# Display the updated dataset
print(data)
