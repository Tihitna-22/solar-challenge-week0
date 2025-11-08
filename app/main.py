import altair as alt
import pandas as pd
import streamlit as st

try:  # Prefer package-relative import when executed as part of the app package.
    from . import utils
except ImportError:  # Fallback for `streamlit run app/main.py` style execution.
    import utils  # type: ignore


st.set_page_config(
    page_title="Solar Resource Comparison Dashboard",
    page_icon="☀️",
    layout="wide",
)

st.title("☀️ Solar Resource Comparison Dashboard")
st.caption(
    "Interactively explore irradiance and weather metrics across Benin, Sierra Leone, and Togo."
)

if "uploaded_csvs" not in st.session_state:
    st.session_state["uploaded_csvs"] = {}

with st.sidebar:
    st.header("Controls")
    selected_countries = st.multiselect(
        "Select countries",
        options=list(utils.COUNTRY_FILES.keys()),
        default=list(utils.COUNTRY_FILES.keys()),
        help="Choose the locations you want to compare in the visuals below.",
    )

    metric = st.selectbox(
        "Metric",
        options=utils.METRIC_COLUMNS,
        index=0,
        help="Select which column to use in the plots and summary table.",
    )

    sample_toggle = st.checkbox(
        "Sample rows per country (recommended for faster loading)",
        value=True,
        help="Limit the number of rows loaded per country to keep the dashboard responsive.",
    )

    sample_size = None
    if sample_toggle:
        sample_size = st.slider(
            "Rows per country",
            min_value=500,
            max_value=10_000,
            step=500,
            value=5_000,
        )

    st.markdown("---")
    with st.expander("Upload local CSV overrides", expanded=False):
        st.write(
            "If the cleaned datasets are not available in the `data/` directory, upload replacements here."
        )
        for country in utils.COUNTRY_FILES.keys():
            uploaded = st.file_uploader(
                f"{country}",
                type="csv",
                key=f"upload_{country}",
            )
            if uploaded is not None:
                st.session_state["uploaded_csvs"][country] = uploaded

    st.subheader("Date filter")
    use_date_filter = st.checkbox(
        "Filter by date range",
        value=False,
        help="Enable to restrict the analysis to a specific period.",
    )

if not selected_countries:
    st.warning("Select at least one country to display the dashboard.")
    st.stop()

uploads = st.session_state.get("uploaded_csvs", {})

with st.spinner("Loading cleaned datasets..."):
    data = utils.load_country_frames(
        selected_countries,
        sample_size=sample_size,
        uploads=uploads,
    )

if data.empty:
    st.error("No data available. Please ensure the cleaned CSVs exist in the data/ directory.")
    st.stop()

if use_date_filter and "Timestamp" in data.columns:
    min_date = pd.to_datetime(data["Timestamp"]).min().date()
    max_date = pd.to_datetime(data["Timestamp"]).max().date()
    date_start, date_end = st.sidebar.date_input(
        "Analysis window",
        (min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    if isinstance(date_start, pd.Timestamp):
        date_start = date_start.date()
    if isinstance(date_end, pd.Timestamp):
        date_end = date_end.date()

    if date_start > date_end:
        st.sidebar.error("Start date must be before end date.")
    else:
        mask = data["Timestamp"].dt.date.between(date_start, date_end)
        data = data.loc[mask]

st.subheader("Distribution Overview")

chart = (
    alt.Chart(data)
    .mark_boxplot(extent="min-max")
    .encode(
        x=alt.X("Country:N", title="Country"),
        y=alt.Y(f"{metric}:Q", title=f"{metric} (units)"),
        color=alt.Color("Country:N", legend=None),
        tooltip=["Country", alt.Tooltip(metric, format=",.2f")],
    )
    .properties(height=420)
)

st.altair_chart(chart, use_container_width=True)

summary = utils.compute_metric_summary(data, metric)
summary_display = summary.copy()
summary_display[["mean", "median", "std", "p95"]] = summary_display[["mean", "median", "std", "p95"]].applymap(
    utils.format_metric_value
)

st.subheader("Metric Summary by Country")
st.dataframe(
    summary_display.set_index("Country"),
    use_container_width=True,
)

st.subheader("Top Regions (Highest Mean)")
col_rank, col_desc = st.columns([1.4, 2])
with col_rank:
    st.metric(
        label="Highest mean",
        value=f"{summary.iloc[0]['Country']} ({summary.iloc[0]['mean']:.1f})",
        delta=None,
    )
with col_desc:
    st.write(
        "The table above ranks countries by the selected metric. Use the sidebar to change the metric or filter by date."
    )

with st.expander("Show raw data (first 1,000 rows)"):
    st.write(data.head(1_000))

st.markdown(
    "---\n"
    "### Usage Tips\n"
    "- Use the sidebar to subset countries, change metrics, and optionally limit the date range.\n"
    "- Sampling helps keep the UI responsive with large CSVs; disable it when you need exact aggregates.\n"
    "- The summary table includes the 95th percentile (p95) to highlight high-end production events.\n"
)
