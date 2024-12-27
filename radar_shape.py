from sklearn.preprocessing import MinMaxScaler

# Normalize the data
scaler = MinMaxScaler()
data[['Position', 'Velocity']] = scaler.fit_transform(data[['Position', 'Velocity']])

# Create sequences for LSTM input
sequence_length = 20
X, y = [], []

for i in range(len(data) - sequence_length):
    X.append(data[['Position', 'Velocity']].iloc[i:i + sequence_length].values)
    y.append(data[['Position', 'Velocity']].iloc[i + sequence_length].values)

X = np.array(X)
y = np.array(y)

print(f"Shape of X: {X.shape}, Shape of y: {y.shape}")
