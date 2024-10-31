# main.py
import matplotlib.pyplot as plt
from model import DICEModel
from parameters import parameters

if __name__ == "__main__":
    dice_model = DICEModel(parameters)
    dice_model.simulate()
    results = dice_model.results()

    # Plot results
    plt.figure(figsize=(12, 8))
    plt.subplot(3, 1, 1)
    plt.plot(results["time"], results["K"], label='Capital Stock (K)')
    plt.title('Capital Stock over Time')
    plt.xlabel('Time')
    plt.ylabel('Capital Stock')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(results["time"], results["C"], label='Consumption (C)', color='orange')
    plt.title('Consumption over Time')
    plt.xlabel('Time')
    plt.ylabel('Consumption')
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(results["time"], results["Y"], label='Output (Y)', color='green')
    plt.title('Output over Time')
    plt.xlabel('Time')
    plt.ylabel('Output')
    plt.grid()

    plt.tight_layout()
    plt.show()