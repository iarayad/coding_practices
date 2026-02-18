---
title: "Research Code Without Chaos"
subtitle: "Good Practices That Save Time"
format:
  revealjs:
    theme: [default]
    css: slides_custom.css
    slide-number: c/t
    progress: true
    transition: fade
    transition-speed: fast
    center: false
    controls: true
    navigation-mode: grid
    overview: true
    hash: true
    preview-links: auto
    code-overflow: wrap
    incremental: true
---

# The problem

Bad research code has a cost:

- We cannot read our own work two months later.
- Others cannot verify or extend results.
- Small changes take too long.
- Bugs hide in duplicated, tangled logic.

**Outcome:** we waste research time.

# The fix: be systematic

1. Separate exploration from reusable code.
2. Keep modules focused and small.
3. Follow style conventions like PEP 8.
4. Automate checks before every commit.
5. Make environments reproducible.

## The Zen of Python

```python
import this
```

```{.text code-line-numbers="2|3|7|15"}
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

This is not philosophy only. It is a practical checklist for research code 💜

# Examples

## Bad code: what it looks like

::: {.columns}
::: {.column width="60%"}
### Hidden state + magic numbers

```python
WTF_W = 20
PHI = 0.0

def run(alpha=0.4):
    global PHI
    PHI += 0.1
    H = build_system(20, 1.0, alpha, PHI)
    return solve(H)
```
:::
::: {.column width="40%"}
### Why this Hurts

- state changes silently
- unclear names
- same values repeated
- hard to test
- unclear if alpha was provided
:::
:::

## Better: explicit and testable

```python
def compute_dispersion_vs_phase(width, phases, momenta, params):
    system = make_infinite_junction(width=width)
    dispersions = []
    for phase in phases:
        bands = kwant.physics.Bands(system, params={**params, "phase": phase})
        dispersions.append(np.array([bands(k) for k in momenta]))
    return {"phases": phases, "momenta": momenta, "dispersions": dispersions}
```

Why better:

- we can read and understand the physics
- all inputs are explicit
- no mutable globals
- function is easy to unit test
- behavior is reproducible

## Bad code: mixed responsibilities

One function handling model, numerics, plotting, I/O.

```python
def do_everything():
    syst = build_model()
    energies = sweep_phase_and_momentum(syst)
    plt.plot(energies)
    save_csv(energies)
    print("done")
```

Why this hurts:

- producing and plotting data are separate tasks
- we cannot reuse the model or solver without the plotting

# Modular code: clear responsibilities

Each module has a single responsibility.

```text
systems.py  -> build Hamiltonian/model
solver.py   -> compute E(k, phase)
current.py  -> compute I(phase)
script       -> orchestrate + plot
```

Modules depend on each other but not on implementation details.

Advantages:

- Easier to read and understand
- Easier to test and debug
- Easier to extend

## Repository shape

Have a clear structure that reflects the modular design.

```text
clean/
  jj_supercurrent/  # reusable logic
    systems.py
    solver.py
    current.py
  tests/
  scripts/  # functions that run experiments, not reusable logic
    run_supercurrent.py
    make_supercurrent_plot.py
    run_supercurrent_scan.py
  pyproject.toml
  README.md
```

## Clean code principles

- One file, one responsibility.
- Names should describe physics intent (`phase`, `mu`, `delta`, `zeeman_x`).
- No hidden defaults that change behavior silently.
- Pass model parameters through `params`.
- Prefer simple functions over clever abstractions.

## Avoid premature Object-Oriented Programming {.scrollable}

Is it really necessary to have a class here?

```python
# Too much structure too soon
class SuperMegaSolverManager:
    def __init__(self, cfg):
        self.cfg = cfg
        self.system = self.build_system()

    def build_system(self):
        ...
```

\ 

Prefer this until complexity demands more:

```python
def compute_dispersion_vs_phase(width, phases, momenta, params):
    ...
```

\ 

Rule of thumb:

- start with pure functions + explicit inputs/outputs
- add classes only when state/lifecycle is truly complex

# Writing style: applying PEP 8

Not just style, but readability under pressure:

- predictable naming (`snake_case`, `UPPER_CASE`)
- consistent line length and imports
- clear function signatures

```python
# Bad
def f(W,p,k,PAR): return run(W,p,k,PAR)

# Better
def compute_dispersion_vs_phase(width, phases, momenta, params):
    return run_dispersion_scan(width, phases, momenta, params)
```

## PEP 8 guide

<iframe src="https://peps.python.org/pep-0008/" width="100%" height="560" loading="lazy"></iframe>


# Tools that make all this easier

::: {.columns}
::: {.column width="50%"}
Quality

- `ruff` (lint + format)
- `pre-commit` (enforce checks)
- `pytest` (regression safety)
:::
::: {.column width="50%"}
Reproducibility

- `pixi` (env + tasks)
- pinned dependencies
- shared commands across machines
:::
:::

## Ruff (Lint + Format)

<iframe src="https://docs.astral.sh/ruff/" width="100%" height="560" loading="lazy"></iframe>


## pre-commit (Git Hook Automation)

<iframe src="https://pre-commit.com/" width="100%" height="560" loading="lazy"></iframe>


## Pixi (Environments + Tasks)

<iframe src="https://pixi.sh/latest/" width="100%" height="560" loading="lazy"></iframe>


## VS Code Setup

Extensions that help:

- Python
- Ruff
- Pylance
- Jupyter (for exploration only)
- GitLens (optional for review)

A nice workflow:

1. Explore quickly in a notebook.
2. Move stable logic into `jj_supercurrent/`.
3. Run lint + tests before commit.

# Takeaway

Good research code is not "extra work."

It is how we protect scientific time and make collaboration possible 🫂
