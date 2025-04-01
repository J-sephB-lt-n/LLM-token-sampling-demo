import numpy as np
import matplotlib.pyplot as plt

# Raw logits for the 3 tokens
logits = np.array([1.0, 2.0, 3.0])

# Temperature values from 0.01 to 2 (avoid 0 to prevent divide-by-zero)
temperatures = np.linspace(0.01, 2, 200)

# Compute probabilities for each temperature
probs = []
for T in temperatures:
    scaled_logits = logits / T
    exp_logits = np.exp(scaled_logits - np.max(scaled_logits))  # for numerical stability
    prob = exp_logits / exp_logits.sum()
    probs.append(prob)

probs = np.array(probs)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(temperatures, probs[:, 0], label="token1")
plt.plot(temperatures, probs[:, 1], label="token2")
plt.plot(temperatures, probs[:, 2], label="token3")

plt.axvline(x=1.0, color='gray', linestyle='--', label='temperature=1')

plt.xlabel("Temperature")
plt.ylabel("Token Probability")
plt.title("Effect of Temperature on Token Probabilities")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("example_temperature_plot.png")
