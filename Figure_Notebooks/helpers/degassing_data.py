"""
Load standardized degassing-tool result CSVs.
"""
import os
from pathlib import Path

import pandas as pd

from sulfur_paper.data_directories import load_run_dirs


def _default_results_dir() -> Path:
    """Resolve the processed-output dir from $MODEL_RUN_DIR.

    Used only when callers don't pass ``results_dir`` explicitly.
    """
    return load_run_dirs(os.environ["MODEL_RUN_DIR"]).processed_output_dir


def load_system(
    sample: str,
    tools: list[str],
    results_dir: str | Path | None = None,
) -> dict[str, pd.DataFrame]:
    """Return ``{tool: DataFrame}`` for one sample.  Missing files are skipped."""
    if results_dir is None:
        results_dir = _default_results_dir()
    results_dir = Path(results_dir)
    out: dict[str, pd.DataFrame] = {}
    for m in tools:
        if m.startswith("VESIcal_"):
            path = results_dir / "VESIcal" / m / f"{sample.lower()}.csv"
        else:
            path = results_dir / m / f"{sample.lower()}.csv"
        if path.exists():
            out[m] = pd.read_csv(path)
    return out


def load_all_systems(
    samples: list[str],
    tools: list[str],
    results_dir: str | Path | None = None,
) -> dict[str, dict[str, pd.DataFrame]]:
    """Return ``{sample: {tool: DataFrame}}`` for every (sample, tool) pair found."""
    if results_dir is None:
        results_dir = _default_results_dir()
    return {s: load_system(s, tools, results_dir) for s in samples}
