# 🎯 Career Suggestion System

A machine learning-based career recommendation system that predicts the most suitable career path based on a user's skills. Built using **K-Nearest Neighbors (KNN)** and **TF-IDF vectorization**, the system maps skill inputs to career categories and suggests relevant roles.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Notebooks](#notebooks)
- [Career Categories](#career-categories)
- [Contributing](#contributing)

---

## 📖 Overview

The Career Suggestion System helps individuals identify the most fitting career path based on their skills. A user simply enters their skills (e.g., *Python, Cloud, Mobile*), and the model predicts the best matching career category along with specific role suggestions.

---

## ✨ Features

- Skill-based career prediction using KNN classification
- TF-IDF vectorization for converting text skills into numerical features
- Clustering of sub-careers into broader main categories
- Suggests a **best role** plus up to **4 additional matching roles**
- Clean, modular Jupyter notebooks covering each pipeline step

---

## 📁 Project Structure

```
Carrer_Suggestion/
│
├── data/                          # Raw and intermediate data files
├── career_dataset_fixed.xlsx      # Cleaned career-skill dataset
├── career_dataset_clustered.xlsx  # Dataset with cluster/category labels
│
├── load_data.ipynb                # Step 1: Load and inspect the dataset
├── step_fix_dataset.ipynb         # Step 2: Fix and clean the dataset
├── preprocess.ipynb               # Step 3: Preprocessing and feature engineering
├── train_model.ipynb              # Step 4: Train the KNN model
├── evaluate.ipynb                 # Step 5: Evaluate model performance
├── predict_career.ipynb           # Step 6: Interactive career prediction
├── main.ipynb                     # Full pipeline notebook
│
└── main.py                        # Standalone Python script for career prediction
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.x | Core programming language |
| pandas | Data loading and manipulation |
| scikit-learn | TF-IDF vectorization & KNN model |
| openpyxl | Reading/writing Excel files |
| Jupyter Notebook | Interactive development and exploration |

---

## 📊 Dataset

The project uses two Excel datasets:

- **`career_dataset_fixed.xlsx`** — Contains `Career` and `Skill` columns with cleaned entries.
- **`career_dataset_clustered.xlsx`** — Extends the fixed dataset with a `Main_Category` column that groups careers into broader domains.

Each row maps a **career role** to a set of **skills** required for that role.

---

## ⚙️ How It Works

1. **Load Dataset** — Read career-skill mappings from Excel.
2. **Clustering** — Sub-careers are grouped into 9 main categories using keyword-based logic.
3. **Vectorization** — Skills are converted to numerical vectors using TF-IDF.
4. **Model Training** — A KNN classifier (`n_neighbors=5`, `weights='distance'`) is trained on the vectorized skills.
5. **Prediction** — User-entered skills are vectorized and passed to the model.
6. **Output** — The system returns the predicted career category, the best role, and up to 4 additional suggested roles.

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NavabhavanaAdapala/Carrer_Suggestion.git
   cd Carrer_Suggestion
   ```

2. **Install dependencies**
   ```bash
   pip install pandas scikit-learn openpyxl jupyter
   ```

---

## ▶️ Usage

### Run as a Python script

```bash
python main.py
```

You will be prompted to enter your skills:

```
Enter your skills (e.g., Python, Cloud, Mobile): Python, data, analytics

Recommended Main Career Category:
Data Science & Analytics

Best Role:
Data Scientist

Suggested Roles:
Data Analyst
Machine Learning Engineer
Business Intelligence Analyst
Data Engineer
```

### Run as a Jupyter Notebook

```bash
jupyter notebook main.ipynb
```

---

## 📓 Notebooks

| Notebook | Description |
|---|---|
| `load_data.ipynb` | Load and explore the raw dataset |
| `step_fix_dataset.ipynb` | Fix inconsistencies and clean data |
| `preprocess.ipynb` | Feature engineering and TF-IDF setup |
| `train_model.ipynb` | Train and save the KNN model |
| `evaluate.ipynb` | Measure accuracy and model performance |
| `predict_career.ipynb` | Run interactive predictions |
| `main.ipynb` | End-to-end pipeline in one notebook |

---

## 🗂️ Career Categories

The system classifies careers into the following main categories:

| Category |
|---|
| Artificial Intelligence |
| Mobile App Development |
| Cloud Computing |
| Cybersecurity |
| Data Science & Analytics |
| DevOps |
| UI/UX Design |
| Backend Development |
| Web Development |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements such as:

- Adding more career domains and skills
- Improving the classification model
- Building a web-based front end
- Adding support for multi-label career prediction

---

## 📄 License

This project is open-source. Feel free to use, modify, and distribute it.

---

> Built with ❤️ by [NavabhavanaAdapala](https://github.com/NavabhavanaAdapala)
