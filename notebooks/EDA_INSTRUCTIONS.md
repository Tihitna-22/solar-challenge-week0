# EDA Notebook Instructions

## How to Use the EDA Template

The `country_eda_template.ipynb` notebook is a comprehensive template for performing Exploratory Data Analysis (EDA) on solar radiation data for any country.

### Step 1: Create Your Country Branch

```bash
git checkout -b eda-<country>
# Example: git checkout -b eda-benin
```

### Step 2: Copy and Rename the Template

1. Copy `country_eda_template.ipynb` to `<country>_eda.ipynb`

   - Example: `benin_eda.ipynb`

2. Open the notebook in Jupyter

### Step 3: Update Configuration

In the first code cell, update:

- `COUNTRY`: Replace `[COUNTRY]` with your country name (e.g., "Benin")
- `DATA_PATH`: Update the path to your country's raw data file
  - Example: `"../data/benin_raw.csv"`

### Step 4: Run the Notebook

Execute all cells sequentially. The notebook will:

1. Load and explore your data
2. Perform comprehensive EDA
3. Clean the data (handle missing values, outliers)
4. Generate all required visualizations
5. Export cleaned data to `data/<country>_clean.csv`

## Notebook Sections

### 1. Import Libraries and Load Data

- Imports all necessary libraries
- Loads the dataset
- Converts Timestamp to datetime

### 2. Summary Statistics & Missing Value Report

- `df.describe()` on all numeric columns
- Missing value analysis with >5% threshold flagging
- Visualization of missing values

### 3. Outlier Detection & Basic Cleaning

- Z-score computation for key columns (|Z| > 3)
- Box plots for outlier visualization
- Missing value imputation (median)
- Outlier capping at ±3 standard deviations

### 4. Time Series Analysis

- Line charts of GHI, DNI, DHI, Tamb over time
- Monthly patterns (bar charts)
- Diurnal cycle (hourly patterns)

### 5. Cleaning Impact Analysis

- Group by Cleaning flag
- Plot average ModA & ModB pre/post-clean
- Calculate improvement percentages

### 6. Correlation & Relationship Analysis

- Correlation heatmap
- Scatter plots: WS, WSgust, WD vs. GHI
- Scatter plots: RH vs. Tamb and RH vs. GHI

### 7. Wind & Distribution Analysis

- Wind rose (radial bar plot) of WS/WD
- Histograms for GHI and WS

### 8. Temperature Analysis

- RH vs. Tamb density plots
- RH vs. GHI density plots
- Temperature and GHI distributions by RH category

### 9. Bubble Chart

- GHI vs. Tamb with bubble size = RH
- GHI vs. Tamb with bubble size = BP

### 10. Summary & Export

- Final summary statistics
- Export cleaned data to CSV

## Key Features

- **Automatic column detection**: Works with any subset of expected columns
- **Comprehensive visualizations**: All required plots included
- **Statistical analysis**: Z-scores, correlations, distributions
- **Data cleaning**: Missing value imputation and outlier handling
- **Export functionality**: Automatically saves cleaned data

## Notes

- The notebook handles missing columns gracefully
- All visualizations are labeled with country name
- Temporary columns are removed before export
- The cleaned CSV is saved to `data/` directory (which is in `.gitignore`)

## Troubleshooting

1. **Import errors**: Make sure all packages in `requirements.txt` are installed
2. **File not found**: Check that your data file path is correct
3. **Memory issues**: For very large datasets, consider sampling in the bubble chart section
4. **Missing columns**: The notebook will skip analyses for missing columns automatically

## Next Steps

After completing EDA:

1. Commit your notebook: `git add <country>_eda.ipynb`
2. Commit cleaned data (if needed locally, but remember it's in .gitignore)
3. Create a Pull Request to merge your branch
