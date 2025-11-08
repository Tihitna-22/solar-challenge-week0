# Streamlit Dashboard

This mini package contains the Streamlit application used to explore the cleaned solar datasets for Benin, Sierra Leone, and Togo.

## Getting Started

1. **Install dependencies** (preferably in a virtual environment):

   ```bash
   pip install -r requirements.txt
   # or, if requirements are managed elsewhere
   pip install streamlit pandas altair
   ```

2. **Run the dashboard locally** from the project root:

   ```bash
   streamlit run app/main.py
   ```

   The app expects the cleaned CSV files to live in the `data/` directory:

   - `data/benin-malanville_clean.csv`
   - `data/sierraleone-bumbuna_clean.csv`
   - `data/togo_clean.csv`

   The files are ignored from version control; ensure you download/generate them before running the UI.

## App Features

- Sidebar controls to pick countries, metrics, and optional date ranges.
- Optional sampling per country to keep the UI responsive with large CSVs.
- Boxplot view for distribution comparisons across the selected metric.
- Summary table with mean/median/std/p95 for the active metric.
- Quick “top region” highlight and expandable raw-data preview for quality checks.

## Deployment

You can deploy the app to [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push your branch (e.g. `dashboard-dev`) to GitHub.
2. Create a new Streamlit app pointing to `app/main.py`.
3. Configure secrets (if any) and ensure the `data/` directory is populated on the remote instance (e.g. via uploaded assets or a storage bucket).

For more advanced setups, consider building a Docker image and running it on your preferred PaaS.
