import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulation parameters
num_steps = 1000  # Number of time steps
time = np.linspace(0, 10, num_steps)  # 10 seconds

# Simulate target position and velocity
position = 100 * np.sin(0.5 * time) + 500  # Example: Sine wave motion
velocity = 50 * np.cos(0.5 * time)  # Derivative of position

# Create a DataFrame
data = pd.DataFrame({'Time': time, 'Position': position, 'Velocity': velocity})

# Visualize the data
plt.figure(figsize=(10, 6))
plt.plot(data['Time'], data['Position'], label='Position')
plt.plot(data['Time'], data['Velocity'], label='Velocity')
plt.title("Simulated Radar Data")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()
