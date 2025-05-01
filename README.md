# Spatiotemporal Density Visualization

This repository contains a Python script to visualize spatiotemporal density data from a quantum spin system. The script identifies first arrival times based on a density threshold and overlays a best-fit line using the normal equation to capture the propagation front (e.g., a light cone).

## Overview

The script performs the following steps:

1. **Load Data**: Reads a time-resolved density matrix from a text file, where the first column represents time and remaining columns represent site densities.
2. **Extract First Arrivals**: For each site, detects the first time index where the density exceeds a given threshold.
3. **Linear Fit**: Computes a best-fit line through the first arrival points using the **normal equation** from linear regression.
4. **Plot**: Visualizes the full density matrix as a heatmap with overlays of the first arrival points and the fitted line.

## Normal Equation and Design Matrix

The normal equation is a standard method used to find the best-fit line in linear regression. It minimizes the sum of squared residuals (the difference between the observed and predicted values). The equation for the best-fit line is derived by solving for the parameters $\theta$ in the following form:

$$
\theta = (X^T X)^{-1} X^T y
$$

Where:

- $X$ is the design matrix, which includes a column of ones (for the intercept) and a column of independent variables (in this case, the spatial site indices).
- $y$ is the dependent variable (the first arrival times corresponding to the site indices).
- $\theta$ contains the model parameters (slope and intercept) of the best-fit line.

In the code:
-The design matrix $X$ is constructed using the spatial site indices (x-values of first arrivals) and a column of ones to account for the intercept.
-The normal equation is then applied to compute the best-fit line that represents the propagation front, or light cone, of the density wavefront.

## File Structure

- `src/plot_spatiotemporal.py`: Main script for processing and plotting.
- `src/N15TFIMNNB05J1.txt`: Sample data file with time and site-resolved density data.

Modify the file path and threshold directly in the script as needed.

## Applications

This code is designed for analyzing quantum dynamics in spin systems, particularly for studying propagation fronts and emergent light-cone behavior in long-range interacting systems.
