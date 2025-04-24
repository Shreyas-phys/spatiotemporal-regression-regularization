# src/plot_spatiotemporal.py

import os
import numpy as np
import matplotlib.pyplot as plt

def getFirstArrivals(density, threshold):
    """
    Finds the first time index where the density exceeds a given threshold
    for each spatial site.
    
    Parameters:
        density (2D array): Density matrix of shape (time, site).
        threshold (float): Minimum value considered a significant 'arrival'.

    Returns:
        arrivals (list of tuples): List of (site, time) tuples marking the first 
                                   time a signal arrives at each site.
    """
    num_times, num_sites = density.shape
    arrivals = []

    for site in range(num_sites):
        for time in range(num_times):
            if density[time, site] > threshold:
                arrivals.append((site, time))
                break  # Only take the first instance
    return arrivals


# === Load simulation data ===

# Define path to the data file
data_path = os.path.join("src", "N15TFIMNNB05J1.txt")

# Load data from file; first column = time, rest = spatial density over time
raw_data = np.loadtxt(data_path)

# Separate time axis and density matrix
times = raw_data[:, 0]         # Shape: (N_times,)
density = 1 - raw_data[:, 1:]  # Shape: (N_times, N_sites), flip to get occupation

# Get number of spatial sites
n_sites = density.shape[1]

# Threshold for detecting 'first arrival'
threshold = 0.2

# Detect first arrival points using threshold
arrivals = getFirstArrivals(density, threshold)

# === Preprocess arrival points for regression ===

# Remove first and last points to avoid edge effects or artifacts
trimmed_points = arrivals[1:-1]

# Separate site index (x) and arrival time (y) for plotting and regression
x_vals = np.array([p[0] for p in trimmed_points])
y_vals = np.array([p[1] for p in trimmed_points])

# === Fit a line using the Normal Equation ===

# Design matrix: first column = 1s (intercept), second = site index (x)
X = np.vstack([np.ones_like(x_vals), x_vals]).T

# Apply normal equation: θ = (XᵀX)^(-1) Xᵀy
theta = np.linalg.inv(X.T @ X) @ X.T @ y_vals
b, m = theta  # b = intercept, m = slope

# Generate x and y values for the fitted line
x_fit = np.linspace(0, 14, 100)       # Match plot range
y_fit = m * x_fit + b                 # y = mx + b

# === Plotting ===

plt.figure(figsize=(10, 5))  # Set plot size

# Display the density matrix as an image
im = plt.imshow(density, aspect='auto', origin='lower', 
                cmap='viridis', interpolation='none')

# Overlay first arrival points as black dots
plt.plot(x_vals, y_vals, 'ko', markersize=4, label='First Arrivals')

# Overlay best-fit line (light cone) as a red dashed line
plt.plot(x_fit, y_fit, 'r--', linewidth=2, label='Best Fit Light cone')

# Set plot limits
plt.xlim(0, 14)     # Site index range
plt.ylim(0, 3000)   # Time index range

# Add plot labels and colorbar
plt.colorbar(im, label='Density')
plt.xlabel('Site index')
plt.ylabel('Time index')
plt.title('Density Plot (Matrix View)')
plt.legend()        # Show legend for data points and line
plt.tight_layout()  # Avoid layout issues
plt.show()
