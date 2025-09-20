## 1. Introduction

This project analyzes a sample of the CORD-19 research dataset, a collection of scholarly articles related to COVID-19 and other coronaviruses.
Since the original dataset is over 1.7GB, only a sample of 1000 records is used for testing and demonstration purposes.

The script provides exploratory data analysis (EDA), highlighting publication trends, journal contributions, missing values, and textual insights from abstracts.

## 2. Dataset

Source: CORD-19 metadata CSV (metadata.csv)

Sample Size: 1000 rows extracted for test purposes

Columns: Includes article metadata such as title, authors, journal, abstract, publish_time, and identifiers (doi, pmcid, pubmed_id).

Key Features:

Textual Data: Titles, abstracts, authors

Categorical Data: Source, license, journal

Numerical Data: PubMed IDs

Date Data: Publish time

## 3. Workflow
### Step 1: Load Dataset

Reads the CSV file into a pandas DataFrame.

Displays the first 5 rows for preview.

Prints DataFrame structure (info()) and shape.

### Step 2: Handle Missing Values

Counts missing values per column.

Drops columns with excessive null values (mag_id, who_covidence_id, arxiv_id, s2_id).

Drops rows with missing title, abstract, or publish_time.

### Step 3: Data Cleaning

Converts publish_time to datetime format.

Extracts the publication year for trend analysis.

### Step 4: Exploratory Data Analysis (EDA)

Descriptive Statistics

Numerical columns summary (describe()).

Papers per Year

Count of publications by year.

Top Journals

10 most frequent journals by article count.

Word Cloud of Abstracts

Visualizes frequent words in research abstracts.

Heatmap of Missing Data

Displays missing values using Seaborn.

## 4. Outputs & Insights

Console Output:

Dataset preview (first rows, shape, info).

Missing value counts.

Papers per year distribution.

Top 10 journals.

Visualizations:

Bar chart - number of papers per year.

Bar chart - top 10 journals.

Word cloud - most common abstract terms.

Heatmap - missing values overview.


## 5. How to Run the Script
### Option A – Run in Python(terminal)

python cord19Analysis.py

Outputs will appear in the terminal and as matplotlib plots.

### Option B – Run in Streamlit

streamlit run cord19Analysis.py

Opens an interactive web app in the browser.

Displays tables, charts, and text interactively.

⚠️ If you run with plain python, you may see Streamlit warnings (missing ScriptRunContext).
These are safe to ignore but indicate that the app is best viewed with Streamlit.

## 6. Reflection

### Challenges:

Large dataset size (1.7GB) → solution: extract a smaller sample for local testing.

Many missing values in metadata → required dropping irrelevant or incomplete columns.

Some abstracts were missing → reduced dataset size further after cleaning.

### Learning Outcomes:

Handling large-scale scientific data with Pandas.

Importance of cleaning missing values for meaningful analysis.

Using EDA + visualization to gain insights from research metadata.

Building reproducible workflows for big dataset subsets.

### Limitations:

Only a sample (1000 records) is analyzed. Full dataset insights may differ.

Word cloud ignores context (e.g., synonyms, stopwords).

Journals with inconsistent naming may affect counts.
