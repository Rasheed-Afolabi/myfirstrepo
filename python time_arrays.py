import time
import numpy as np


# Create an array of evenly spaced time values (e.g., from 0 to 10 seconds)
time = np.linspace(0, 10, 5)

# Multiply each time by 2 to simulate some transformation (like speed or scaling)
scaled_time = time * 2

print("Original time array:", time)
print("Scaled time array:", scaled_time)
