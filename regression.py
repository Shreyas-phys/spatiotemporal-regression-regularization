# src/plot_spatiotemporal.py

import os
import numpy as np
import matplotlib.pyplot as plt

# Load data
data_path = os.path.join("src", "N15TFIMNNB05J1.txt")
raw_data = np.loadtxt(data_path)

# Extract time and spatial density
times = raw_data[:, 0]         # (N_times,)
densities = raw_data[:, 1:]    # (N_times, N_sites)
n_sites = densities.shape[1]

# Increase figure size and use 'nearest' interpolation for sharp data representation
plt.figure(figsize=(12, 8))  # Larger figure size for better resolution
plt.imshow(
    densities,
    aspect='auto',
    origin='lower',
    cmap='viridis',
    interpolation='nearest',  # Avoids blurring by using nearest neighbor interpolation
    extent=[0, n_sites - 1, times[0], times[-1]]
)

# Labeling
plt.xlabel("Site Index")
plt.ylabel("Time")
plt.title("Spatiotemporal Evolution (Density)")
plt.colorbar(label="Density")

# Save the figure with higher DPI
os.makedirs("results/plots", exist_ok=True)
plt.tight_layout()
plt.savefig("results/plots/spatiotemporal_plot.png", dpi=600)  # Higher DPI for better resolution
plt.show()
