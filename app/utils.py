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


def get_missing_countries(countries: Iterable[str]) -> List[str]:
    """Return the subset of countries whose CSV paths do not exist locally."""

    missing: List[str] = []
    for country in countries:
        path = COUNTRY_FILES.get(country)
        if path is None or not path.exists():
            missing.append(country)
    return missing


def load_country_frames(
    countries: Iterable[str],
    sample_size: Optional[int] = None,
    parse_dates: bool = True,
    uploads: Optional[Dict[str, "UploadedFile"]] = None,
) -> pd.DataFrame:
    """Load and concatenate the cleaned datasets for the selected countries.

    ``uploads`` can contain ``streamlit.uploaded_file_manager.UploadedFile`` objects which override
    the on-disk CSVs.
    """

    frames: List[pd.DataFrame] = []
    date_cols = ["Timestamp"] if parse_dates else None
    uploads = uploads or {}

    for country in countries:
        uploaded_file = uploads.get(country)
        if uploaded_file is not None:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, parse_dates=date_cols)
            st.info(f"Using uploaded CSV for {country} (rows: {len(df):,}).", icon="📄")
        else:
            path = COUNTRY_FILES[country]
            if not path.exists():
                st.warning(
                    f"Dataset for {country} is missing: `{path}`. Upload the cleaned CSV via the sidebar.",
                    icon="⚠️",
                )
                continue
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
