#  <i> <mark> Mobile-Data-Analytics-Pipeline </mark> </i>

End-to-end smartphone data collection, preprocessing, and exploratory analytics pipeline built from real-world web data.

This project collects smartphone specifications directly from the Smartprix website using Selenium, transforms raw web data into a clean analytical dataset, and performs exploratory data analysis to uncover trends in the smartphone market.

---

## The Problem

Most data analysis projects begin with a ready-made CSV file.

Real-world data projects rarely work that way.

Before any analysis can begin, data must first be collected, cleaned, standardized, and validated. Raw web data often contains inconsistent formats, missing values, duplicate records, and noisy information that cannot be analyzed directly.

This project demonstrates the complete data analytics workflow—from data acquisition to meaningful insights.

---

## Project Pipeline

Smartprix Website
        ↓
Web Scraping
        ↓
Raw Dataset
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
Visualizations & Insights

---

## What This Project Does

- Collects smartphone specifications directly from Smartprix
- Extracts structured product information using Selenium
- Builds a raw dataset from real-world web data
- Cleans and standardizes inconsistent values
- Handles missing and duplicate records
- Performs exploratory data analysis (EDA)
- Generates visualizations to understand market trends
- Organizes the workflow using a modular project structure

---

## Example Use Case

Suppose a company wants to analyze the smartphone market to understand pricing trends, brand competition, RAM and storage distribution, battery capacity, and processor popularity.

Instead of manually collecting thousands of product specifications, this pipeline automatically gathers the data, prepares it for analysis, and produces meaningful insights that can support market research or machine learning projects.

---

## Project Structure

```
Mobile-Data-Analytics-Pipeline/
│
├── data/
│   ├── raw/                  # Raw scraped datasets
│   ├── interim/              # Intermediate cleaned datasets
│   ├── processed/            # Final analysis-ready datasets
│   └── external/             # Optional external datasets
│
├── src/
│   ├── scraping/             # Selenium scraping scripts
│   ├── preprocessing/        # Cleaning & transformation
│   ├── analysis/             # Exploratory data analysis
│   ├── visualization/        # Charts and plots
│   └── utils/                # Helper functions
│
├── notebooks/                # Jupyter notebooks
├── outputs/
│   ├── figures/              # Generated visualizations
│   └── reports/              # Analysis reports
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Tech Stack

- Python
- Selenium
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Dataset Attributes

The collected dataset contains smartphone specifications such as:

- Brand
- Model Name
- Price
- RAM
- Storage
- Processor
- Display Size
- Battery Capacity
- Camera Specifications
- Operating System
- Network Support

---

## How It Works

1. Scrape smartphone listings from Smartprix
2. Store raw web data
3. Clean and preprocess the dataset
4. Handle missing and inconsistent values
5. Prepare an analysis-ready dataset
6. Perform exploratory data analysis
7. Generate visual insights

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sanskarhere/Mobile-Data-Analytics-Pipeline.git

cd Mobile-Data-Analytics-Pipeline
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

macOS/Linux

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the scraper

```bash
python src/scraping/scraper.py
```

### 5. Perform data cleaning

```bash
python src/preprocessing/clean.py
```

### 6. Run exploratory analysis

```bash
python src/analysis/eda.py
```

---

## Current Scope

This project focuses on end-to-end data acquisition, preprocessing, and exploratory data analysis using real-world smartphone data.

It serves as a practical demonstration of data engineering fundamentals before machine learning.

---

## Future Roadmap

- Add feature engineering pipeline
- Build price prediction models
- Train machine learning models
- Evaluate model performance
- Create an interactive Streamlit dashboard
- Automate scheduled data collection
- Deploy REST APIs using FastAPI
- Containerize the project using Docker

---

## Why It Stands Out

Many beginner data analysis projects start with an already cleaned dataset.

This project begins with raw web data and demonstrates the complete workflow required in real-world analytics:

- Web scraping
- Data acquisition
- Data cleaning
- Data preprocessing
- Exploratory data analysis
- Data visualization
- Modular pipeline design

---

## Author

**Sanskar Gupta**

AI/ML Engineer | Data Analytics | Data Engineering | Python

---

## License

This project is licensed under the MIT License.

See the **LICENSE** file for details.