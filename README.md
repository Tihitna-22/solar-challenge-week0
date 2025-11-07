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
