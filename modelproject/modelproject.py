import numpy as np
from scipy import optimize
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd

# Base parameters
alpha_base = 0.3
eta_base = 0.05
delta_base = 0.1
rho_base = 0.02
sigma_base = 0.02

# Constants
alpha = 0.5    # Output elasticity of capital
beta = 0.9     # Discount factor
delta = 0.1    # Depreciation rate
eta = 0.1      # Population growth rate
rho = 0.03     # Preference rate
sigma = 2.0    # Intertemporal elasticity of substitution

# Derived parameters
L_initial = 100  # Initial labor supply
A = 1.0          # Technology level
L_new = L_initial * (1 + eta)  # New labor supply after population growth

# Model functions
def production_function(K, L):
    return A * (K**alpha) * (L**(1 - alpha))

def utility_function(c):
    return (c**(1 - sigma) - 1) / (1 - sigma)

# Steady state calculations
k_star = ((beta * (1 - delta + A * alpha * (L_initial / k_star)**(1 - alpha))) / (1 + eta))**(1 / (1 - alpha))
y_star = production_function(k_star, L_initial)
c_star = y_star - delta * k_star

# Sensitivity analysis
alpha_varied = np.linspace(0.25, 0.35, 11)
eta_varied = np.linspace(0.03, 0.07, 11)

# Simulation settings
max_iterations = 5000
tolerance = 1e-6
solution_y_t = np.zeros(max_iterations)

# Steady state population calculation
steady_state_population = L_initial / (1 - eta)
