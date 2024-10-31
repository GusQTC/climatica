# main.py
import matplotlib.pyplot as plt
from model import DICEModel
from parameters import parameters

if __name__ == "__main__":
    dice_model = DICEModel(parameters)
    dice_model.simulate()
    results = dice_model.results()

    # Plot Capital Stock
    plt.figure(figsize=(10, 6))
    plt.plot(results["time"], results["K"], label='Capital Stock (K)', color='blue')
    plt.title('Capital Stock over Time')
    plt.xlabel('Time')
    plt.ylabel('Capital Stock')
    plt.grid()
    plt.legend()
    plt.show()

    # Plot Consumption
    plt.figure(figsize=(10, 6))
    plt.plot(results["time"], results["C"], label='Consumption (C)', color='orange')
    plt.title('Consumption over Time')
    plt.xlabel('Time')
    plt.ylabel('Consumption')
    plt.grid()
    plt.legend()
    plt.show()

    # Plot Output
    plt.figure(figsize=(10, 6))
    plt.plot(results["time"], results["Y"], label='Output (Y)', color='green')
    plt.title('Output over Time')
    plt.xlabel('Time')
    plt.ylabel('Output')
    plt.grid()
    plt.legend()
    plt.show()