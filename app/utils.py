import pandas as pd
from pathlib import Path
from typing import Dict, Iterable, List, Optional

import streamlit as st

# Mapping between human-friendly country names and their cleaned CSV paths.
COUNTRY_FILES: Dict[str, Path] = {
    "Benin (Malanville)": Path("data/benin-malanville_clean.csv"),
    "Sierra Leone (Bumbuna)": Path("data/sierraleone-bumbuna_clean.csv"),
    "Togo (Dapaong)": Path("data/togo_clean.csv"),
}

# Columns that we will expose for comparison/visualisation.
METRIC_COLUMNS: List[str] = ["GHI", "DNI", "DHI", "ModA", "ModB", "Tamb", "RH", "WS"]


@st.cache_data(show_spinner=False)
def load_country_frames(
    countries: Iterable[str],
    sample_size: Optional[int] = None,
    parse_dates: bool = True,
) -> pd.DataFrame:
    """Load and concatenate the cleaned datasets for the selected countries.

    Args:
        countries: Country labels that need to be loaded.
        sample_size: Optional number of rows to sample from each country to keep
            the UI responsive. If ``None`` the full dataset is used.
        parse_dates: Whether to parse the ``Timestamp`` column as datetime.

    Returns:
        A concatenated dataframe containing a ``Country`` column for faceting.
    """

    frames: List[pd.DataFrame] = []
    date_cols = ["Timestamp"] if parse_dates else None

    for country in countries:
        path = COUNTRY_FILES[country]
        if not path.exists():
            raise FileNotFoundError(
                f"Dataset for {country!r} is missing: {path}. Ensure cleaned CSVs are in the data/ directory."
            )

        df = pd.read_csv(path, parse_dates=date_cols)
        df["Country"] = country

        if sample_size is not None:
            sample_n = min(sample_size, len(df))
            df = df.sample(sample_n, random_state=42).sort_index()

        frames.append(df)

    if not frames:
        return pd.DataFrame()

    return pd.concat(frames, ignore_index=True)


def compute_metric_summary(df: pd.DataFrame, metric: str) -> pd.DataFrame:
    """Return aggregated statistics for the requested metric per country."""

    if metric not in df.columns:
        raise ValueError(f"Metric {metric!r} not found in dataframe columns: {list(df.columns)}")

    summary = (
        df.groupby("Country")[metric]
        .agg(mean="mean", median="median", std="std", p95=lambda x: x.quantile(0.95))
        .reset_index()
        .sort_values("mean", ascending=False)
    )
    return summary


def format_metric_value(value: float) -> str:
    """Helper for pretty-printing numeric metric values inside Streamlit tables."""

    if pd.isna(value):
        return "–"
    if abs(value) >= 1000:
        return f"{value:,.1f}"
    return f"{value:.2f}"
