"""Synthetic stage illustration; no diagnosis, model, network, or database."""

from math import isfinite
from statistics import mean


def summarize(values: tuple[float | None, ...]) -> dict[str, int | float]:
    """Validate a made-up series while preserving missing observations."""
    present = [value for value in values if value is not None]
    if not present:
        raise ValueError("The illustration requires at least one observation.")
    if any(not isfinite(value) for value in present):
        raise ValueError("Observations must be finite numbers.")
    return {
        "observations": len(present),
        "missing": len(values) - len(present),
        "mean": mean(present),
    }


def main() -> None:
    # Invented dimensionless numbers; no vehicle telemetry or private input.
    summary = summarize((1.0, 2.0, None, 3.0, 4.0))
    print("Synthetic illustration; this output is not a diagnostic conclusion.")
    print(f"Input summary: {summary}")

    stages = (
        ("Data intake", "Synthetic input was checked and summarized above."),
        ("Applicable knowledge", "Role described only; no catalogs are loaded."),
        ("Hypotheses", "Role described only; no model or diagnosis is simulated."),
        ("Hypothesis review", "Role described only; no conclusions are verified."),
        ("Instrumental checks", "Role described only; no recommendations are issued."),
    )
    for number, (name, boundary) in enumerate(stages, start=1):
        print(f"{number}. {name}: {boundary}")
    print("Real conclusions require an authorized workflow and specialist review.")


if __name__ == "__main__":
    main()
