""" CONSERVATIVE GROWHT
Description: This configuration assumes a lower capital share and a slightly higher discount factor, reflecting a conservative growth perspective. 
The depreciation rate is lower, suggesting more investment in maintaining capital. This model might be useful for assessing long-term sustainability 
under stable economic conditions.
parameters = {
    "alpha": 0.35,
    "beta": 0.95,
    "delta": 0.05,
    "gamma": 1.3,
    "sigma": 1.5,
    "A": 0.9,
    "K0": 1.0,
    "L0": 1.0,
    "time_horizon": 50,
}

parameters = {
    "alpha": 0.4,  # Capital share in output Brazil typically has a slightly higher capital share in developing economies.
    "beta": 0.92,  # Discount factor The discount rate might be lower due to concerns about future generations and sustainable development.
    "delta": 0.1,  # Depreciation rate
    "gamma": 1.5,  # Elasticity of utility with respect to consumption With income inequality, you might want a slightly higher value to reflect the diminishing marginal utility.
    "sigma": 2.0,  # Damage function parameter
    "A": 1.0,      # Total factor productivity
    "K0": 1.0,     # Initial capital stock
    "L0": 1.0,     # Initial labor supply
    "time_horizon": 50,  # Time horizon for the model
}
"""

parameters ={
    "time_horizon": 50,
    "K0": 4.5e12,                   # Brazil's initial capital stock (e.g., in USD)
    "L0": 1.05e8,                   # Initial labor force in Brazil
    "A": 0.9,                       # Total factor productivity specific to Brazil
    "alpha": 0.3,                   # Capital share in production for Brazil
    "gamma": 2.0,                   # Utility curvature specific to Brazil
    "sigma": 0.2,                   # Damage coefficient specific to Brazil
    "delta": 0.1,                  # Depreciation rate of capital
    "labor_growth_rate": 0.01       # Expected annual labor growth rate in Brazil
}