# Contributing

## Setup
```bash
cd clean
pixi run lint
pixi run test
```

## Workflow
1. Make focused changes.
2. Run `pixi run lint` and `pixi run test` before committing.
3. Open a pull request with:
   - What changed.
   - Why it changed.
   - How it was tested.

## Style
- Keep functions short and single-purpose.
- Keep names descriptive and domain-specific.
- Avoid hidden state and duplicated logic.
