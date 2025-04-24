# Spatiotemporal Density Visualization

This repository contains a Python script to visualize spatiotemporal density data from a quantum spin system. The script identifies first arrival times based on a density threshold and overlays a best-fit line using the normal equation to capture the propagation front (e.g., a light cone).

## Overview

The script performs the following steps:

1. **Load Data**: Reads a time-resolved density matrix from a text file, where the first column represents time and remaining columns represent site densities.
2. **Extract First Arrivals**: For each site, detects the first time index where the density exceeds a given threshold.
3. **Linear Fit**: Computes a best-fit line through the first arrival points using the normal equation from linear regression.
4. **Plot**: Visualizes the full density matrix as a heatmap with overlays of the first arrival points and the fitted line.

## File Structure

- `src/plot_spatiotemporal.py`: Main script for processing and plotting.
- `src/N15TFIMNNB05J1.txt`: Sample data file with time and site-resolved density data.

## Requirements

- Python 3
- numpy
- matplotlib

Install dependencies with:

```bash
pip install numpy matplotlib
```

## Usage

Run the script:

```bash
python src/plot_spatiotemporal.py
```

Modify the file path and threshold directly in the script as needed.

## Applications

This code is designed for analyzing quantum dynamics in spin systems, particularly for studying propagation fronts and emergent light-cone behavior in long-range interacting systems.
