# StudentLife Analysis

Exploratory Analysis of the StudentLife Dataset
This project performs an exploratory data analysis on the public StudentLife dataset to investigate the relationship between passively collected mobile sensor data for physical activity and student academic performance (GPA). The analysis uses Python and common data science libraries to process, visualize, and model physical activity inferences over a 10 week academic semester.

The StudentLife dataset can be downloaded here: https://www.kaggle.com/datasets/dartweichen/student-life

Project Structure
```
.
├── data/               # Contains the raw dataset (must be downloaded manually)
│   └── studentlife/
│       └── activity/
├── results/            # Contains generated outputs (ignored by Git)
│   ├── figures/
│   └── dataframes/
├── src/                # Contains all Python source code
│   ├── activity_exploratory_analysis.ipynb
│   └── imports.py
├── .gitignore          # Specifies files and folders for Git to ignore
├── README.md           # This project overview and guide
└── requirements.txt    # A list of all required Python packages
```

Setup and Installation

Follow these steps to set up the project environment and run the analysis on your local machine.

1. Clone the Repository
First, clone this repository to your local machine using Git.

Bash

git clone https://github.com/mcmeans2/Student-Life-Analysis.git
cd Student-Life-Analysis

2. Download the Dataset
This repository does not contain the raw data due to its size. You must download the StudentLife dataset manually.

Once downloaded, locate the activity data.

Place all the activity_uXX.csv files inside the data/studentlife/activity/ directory in your project folder.

3. Create and Activate a Virtual Environment
This project uses a virtual environment to manage dependencies and avoid conflicts with your system's Python installation.
