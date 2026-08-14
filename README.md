# 📱 Google Playstore Data Analysis

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5%2B-green.svg)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)]()

## 📖 Overview

This project performs a comprehensive **Exploratory Data Analysis (EDA)** on the Google Playstore Apps dataset. The goal is to clean messy, real-world data and extract meaningful business insights about app categories, installs, ratings, pricing, and user engagement.

> **Key Question:** What makes an app successful on the Google Playstore?

---

## 📊 Dataset

- **Source:** Kaggle
- **Total Rows:** 10,841 (before cleaning) → 9,659 (after cleaning)
- **Total Columns:** 13
- **Key Columns:** App, Category, Rating, Reviews, Installs, Price, Type, Size, Last Updated, Content Rating

---

## 🛠️ Tech Stack

| Tool | Purpose |
|:---|:---|
| **Python 3.8+** | Core programming language |
| **Pandas** | Data cleaning, manipulation, and analysis |
| **NumPy** | Numerical operations |
| **Git & GitHub** | Version control and project hosting |

---

## 📁 Project Structure
Google_Playstore_Analysis/
│
├── data/
│   └── googleplaystore.csv        # Raw dataset
│
├── main.py                         # Full pipeline (cleaning + analysis)
├── README.md                       # Project documentation
├── requirements.txt                # Dependencies
└── .gitignore                      # Ignored files