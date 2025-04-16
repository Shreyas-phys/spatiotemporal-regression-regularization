# src/plot_spatiotemporal.py

import os
import numpy as np
import matplotlib.pyplot as plt

def getFirstArrivals(density,threshold):
    num_times,num_sites = densities.shape
    
    arrivals=[]

    for sites in range(num_sites):
        for time in range(num_times):
            if densities[time,sites] > threshold:
                arrivals.append((sites,time))
                break
    return arrivals

    
# Load data
data_path = os.path.join("src", "N15TFIMNNB05J1.txt")
raw_data = np.loadtxt(data_path)

# Extract time and spatial density
times = raw_data[:, 0]         # (N_times,)
density = 1-raw_data[:, 1:]    # (N_times, N_sites)
n_sites = density.shape[1]
threshold=0.1


# Get arrival data
arrivals = getFirstArrivals(density, threshold)
# Extract (site, time) → X = site, Y = time
x_vals, y_vals = zip(*arrivals)  # site, time

plt.figure(figsize=(10, 5))
    
# Show the density as a color image
im = plt.imshow(density, aspect='auto', origin='lower', cmap='viridis', interpolation='none')

# Plot black dots in correct (x, y) coordinates
plt.plot(x_vals, y_vals, 'ko', markersize=4, label='First Arrivals')

# Add a colorbar
plt.colorbar(im, label='Density')
# Labeling axes
plt.xlabel('Site index')
plt.ylabel('Time index')
plt.title('Density Plot (Matrix View)')
plt.tight_layout()
plt.show()
