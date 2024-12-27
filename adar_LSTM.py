from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Build LSTM model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(sequence_length, 2)),
    LSTM(50),
    Dense(2)  # Output: [Position, Velocity]
])

model.compile(optimizer='adam', loss='mse')
model.summary()

# Train the model
history = model.fit(X, y, epochs=20, batch_size=32, validation_split=0.2)
