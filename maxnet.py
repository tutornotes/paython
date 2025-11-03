
import numpy as np

def MaxNet():
    # Given initial activations
    activations = np.array([0.3, 0.5, 0.7, 0.9])
    epsilon = 0.2
    m = len(activations)
    iteration = 0

    print("Initial Activations:", activations)

    while np.count_nonzero(activations > 1):
        new_activations = np.zeros_like(activations)
        for j in range(m):
            # Sum of all other activations except self
            inhibition = epsilon * sum(activations[i] for i in range(m) if i != j)
            new_activations[j] = activations[j] - inhibition
            new_activations[j] = max(0, new_activations[j]) # No negative values

        activations = new_activations
        iteration += 1
        print(f"After iteration {iteration}: {activations}")

    winner_index = np.argmax(activations)
    print(f"\nWinning Neuron: Neuron {winner_index + 1} with final activation {activations[winner_index]}")

MaxNet()