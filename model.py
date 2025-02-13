import numpy as np
from parameters import parameters
class DICEModel:
    def __init__(self, params):
        self.params = params
        self.time = np.arange(params["time_horizon"])
        self.K = np.zeros(params["time_horizon"])
        self.C = np.zeros(params["time_horizon"])
        self.Y = np.zeros(params["time_horizon"])
        self.D = np.zeros(params["time_horizon"])  # Damages

        # Set initial values based on Brazil-specific parameters
        self.K[0] = params["K0"]  # Brazil's initial capital stock
        self.L = params["L0"]      # Brazil's initial labor supply

    def production(self, K, L):
        """ Cobb-Douglas production function with Brazil's parameters """
        return self.params["A"] * (K ** self.params["alpha"]) * (L ** (1 - self.params["alpha"]))

    def utility(self, C):
        """ Utility function with Brazil's parameters """
        return (C ** (1 - self.params["gamma"])) / (1 - self.params["gamma"])

    def simulate(self):
        for t in self.time[:-1]:
            # Calculate Brazil-specific economic output
            self.Y[t] = self.production(self.K[t], self.L)
            
            # Calculate damages based on Brazil's carbon intensity
            self.D[t] = self.params["sigma"] * self.Y[t]
            self.C[t] = self.Y[t] - self.D[t]  # Consumption after damages
            self.C[t] = max(self.C[t], 0)      # Avoid negative consumption

            # Update capital stock for the next period
            self.K[t + 1] = (1 - self.params["delta"]) * self.K[t] + self.C[t]

            # Adjust labor growth using Brazil's forecasted growth rate
            self.L *= 1 + self.params["labor_growth_rate"]

    def results(self):
        return {
            "time": self.time,
            "K": self.K,
            "C": self.C,
            "Y": self.Y,
            "D": self.D,
        }
