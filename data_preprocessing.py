import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load the dataset
data = pd.read_csv('identity_security_dataset.csv')

# Encode categorical variables
encoder = LabelEncoder()
data['event_encoded'] = encoder.fit_transform(data['event'])
data['ip_address_encoded'] = encoder.fit_transform(data['ip_address'])

# Normalize numerical data (user_id)
scaler = MinMaxScaler()
data['user_id_normalized'] = scaler.fit_transform(data[['user_id']])

# Select features and target
features = ['user_id_normalized', 'event_encoded', 'ip_address_encoded']
target = ['label']

X = data[features]
y = data[target]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Save training and testing sets as CSV files
X_train.join(y_train).to_csv('train_set.csv', index=False)
X_test.join(y_test).to_csv('test_set.csv', index=False)

# Display the training and testing sets
print("Training set:")
print(X_train.join(y_train))
print("\nTesting set:")
print(X_test.join(y_test))
