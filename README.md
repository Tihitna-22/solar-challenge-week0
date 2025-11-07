# Solar Challenge Week 0

This repository contains the code and analysis for the Solar Challenge Week 0, focusing on solar radiation measurement data analysis.

## Dataset Overview

The data for this week's challenge is extracted and aggregated from Solar Radiation Measurement Data. Each row in the data contains the values for solar radiation, air temperature, relative humidity, barometric pressure, precipitation, wind speed, and wind direction, cleaned and soiled radiance sensor (soiling measurement), and cleaning events.

### Data Structure

- **Timestamp** (yyyy-mm-dd hh:mm): Date and time of each observation
- **GHI** (W/m²): Global Horizontal Irradiance
- **DNI** (W/m²): Direct Normal Irradiance
- **DHI** (W/m²): Diffuse Horizontal Irradiance
- **ModA** (W/m²): Measurements from module/sensor A
- **ModB** (W/m²): Measurements from module/sensor B
- **Tamb** (°C): Ambient Temperature
- **RH** (%): Relative Humidity
- **WS** (m/s): Wind Speed
- **WSgust** (m/s): Maximum Wind Gust Speed
- **WSstdev** (m/s): Standard Deviation of Wind Speed
- **WD** (°N): Wind Direction
- **WDstdev**: Standard Deviation of Wind Direction
- **BP** (hPa): Barometric Pressure
- **Cleaning** (1 or 0): Cleaning event indicator
- **Precipitation** (mm/min): Precipitation rate
- **TModA** (°C): Temperature of Module A
- **TModB** (°C): Temperature of Module B
- **Comments**: Additional notes

## Environment Setup

### Prerequisites

- Python 3.11 or higher
- Git
- GitHub account

### Installation Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/solar-challenge-week0.git
   cd solar-challenge-week0
   ```

2. **Create a virtual environment**

   Using `venv`:

   ```bash
   python -m venv venv
   ```

   Or using `conda`:

   ```bash
   conda create -n solar-challenge python=3.11
   conda activate solar-challenge
   ```

3. **Activate the virtual environment**

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Verify installation**
   ```bash
   python --version
   pip list
   ```

## Project Structure

```
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md
```

## Usage

### Running Jupyter Notebooks

```bash
jupyter notebook
```

Notebooks should be created in the `notebooks/` directory.

### Running Streamlit Dashboard

```bash
streamlit run app.py
```

### Running Tests

```bash
pytest tests/ -v
```

## Week's Topics Covered

- **Python Programming**: Task-specific programming assignments
- **GitHub Commands**: Continuous committing and repository management
- **Data Understanding and Exploration**: Applying exploratory data analysis techniques
- **CI/CD**: Understanding continuous integration and continuous deployment
- **Streamlit**: Creating a dashboard using Streamlit

## Team

**Facilitators:**

- Yabebal
- Kerod
- Mahbubah
- Filimon

## Key Dates

- **Challenge Introduction**: 9:30 AM UTC on Wednesday, 05 Nov 2025
- **Interim Submission**: 8:00 PM UTC on Sunday, 09 Nov 2025
- **Final Submission**: 8:00 PM UTC on Wednesday, 12 Nov 2025

## Contributing

1. Create a new branch for your work
2. Make your changes
3. Commit with clear messages
4. Push to your branch
5. Create a Pull Request

## License

This project is part of the 10 Academy Solar Challenge.
