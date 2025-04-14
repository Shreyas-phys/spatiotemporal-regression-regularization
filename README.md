# Spatiotemporal Regression and Regularization

This project implements **regression from scratch** to model signal propagation using **spatiotemporal data**, with a focus on **understanding the effects of regularization** and the **bias-variance tradeoff**.

## 🧠 Motivation

In many areas of physics and medicine, such as quantum information or EEG/fMRI analysis, we encounter signals that propagate through space and time. Estimating the **velocity of propagation** or **first arrival points** becomes essential.

This project extracts **first arrival points** from noisy spatiotemporal data and fits a model using:
- **Linear Regression**
- **Polynomial Regression (to show overfitting)**
- **Ridge Regularization (L2)**

All models are implemented **from scratch** using gradient descent and cost minimization — no machine learning libraries.

## 🔍 Goals

- Preprocess spatiotemporal data to detect first-arrival points via thresholding
- Build a linear model from scratch minimizing MSE
- Fit polynomial models and observe overfitting with high-degree terms
- Use **Ridge regularization** to improve generalization
- Visualize the **bias-variance tradeoff**
- Compare all models using metrics such as:
  - Mean Squared Error (MSE)
  - Cross-Validation
  - Residual plots
  - Coefficient norms

## 🛠 Features

- 🧮 Gradient descent optimizer for cost minimization
- 🧠 L2 regularization (Ridge)
- 📈 Visualization of underfitting vs. overfitting
- 📊 Statistical comparison of fits
- 🔬 Application to physics-like spatiotemporal data

## 📂 Structure

- `src/` — All from-scratch implementations
- `data/` — Simulated or real spatiotemporal datasets
- `notebooks/` — Analysis, visualization, and exploration
- `results/` — Final figures and comparisons

## 📌 Sample Output

| Linear Fit | Polynomial Fit (Deg 5) | Ridge Regularized |
|------------|------------------------|-------------------|
| ![](results/plots/linear_fit.png) | ![](results/plots/poly_fit_deg5.png) | ![](results/plots/ridge_vs_lasso.png) |

## 🧪 Technologies

- Python (NumPy, Matplotlib)
- No ML libraries (sklearn, tensorflow, etc.)
- All models built from first principles

## 📘 Concepts Demonstrated

- Linear and polynomial regression
- Gradient descent optimization
- Bias-variance tradeoff
- Regularization (Ridge)
- Signal extraction from noisy data

## 🔧 Setup

```bash
git clone https://github.com/yourusername/spatiotemporal-regression-regularization.git
cd spatiotemporal-regression-regularization
pip install -r requirements.txt
