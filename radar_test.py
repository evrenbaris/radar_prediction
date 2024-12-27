# Make predictions
predictions = model.predict(X)

# Inverse transform predictions to original scale
predicted_data = scaler.inverse_transform(predictions)
actual_data = scaler.inverse_transform(y)

# Visualize predictions vs actual
plt.figure(figsize=(10, 6))
plt.plot(actual_data[:, 0], label="Actual Position", alpha=0.7)
plt.plot(predicted_data[:, 0], label="Predicted Position", alpha=0.7)
plt.title("Position Prediction")
plt.xlabel("Time Steps")
plt.ylabel("Position")
plt.legend()
plt.grid()
plt.show()
