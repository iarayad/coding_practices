"""Compute dispersion vs phase and the supercurrent-phase relation."""

# %%
import matplotlib.pyplot as plt
import numpy as np

from jj_supercurrent import compute_dispersion_vs_phase, current_from_dispersion

# %%


def closest_phase_index(phases, target):
    return int(np.argmin(np.abs(phases - target)))


# %%

phases = np.linspace(0.0, 2.0 * np.pi, 61)
momenta = np.linspace(-np.pi, np.pi, 121)
params = {"mu": 0.4, "delta": 0.2, "t": 1.0}
params["alpha"] = 0.5
params["zeeman_x"] = 0
params["zeeman_z"] = 0
# %%
result = compute_dispersion_vs_phase(
    phases=phases, momenta=momenta, params=params, width=20
)
current = current_from_dispersion(result["phases"], result["dispersions"])
# %% Plotting
fig, (ax_dispersion, ax_current) = plt.subplots(2, 1, figsize=(8, 8))

for target in [0.0, np.pi / 2.0, np.pi]:
    idx = closest_phase_index(result["phases"], target)
    ax_dispersion.plot(
        result["momenta"],
        result["dispersions"][idx],
        lw=1,
        alpha=0.65,
        label=rf"$\phi={result['phases'][idx]:.2f}$",
    )

ax_dispersion.set_title("Dispersion relation E(k) at selected phases")
ax_dispersion.set_xlabel("k")
ax_dispersion.set_ylabel("Energy")
ax_dispersion.grid(alpha=0.3)
ax_dispersion.set_ylim(-1, 1)
ax_dispersion.set_xlim(-2, 2)

ax_current.plot(result["phases"], current, lw=2)
ax_current.set_title("Current-phase relation")
ax_current.set_xlabel("Phase")
ax_current.set_ylabel("I(phase) [arb.]")
ax_current.grid(alpha=0.3)

fig.tight_layout()
plt.show()

# %%
