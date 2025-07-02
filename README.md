# NBA High-Scorer Predictor

An end-to-end machine learning project that analyzes NBA player box-score statistics to predict whether a player will score 20 or more points in a single game. Built with Python, scikit-learn, and Streamlit for an interactive demo.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
  - [Analysis Notebook](#analysis-notebook)  
  - [Streamlit App](#streamlit-app)  
- [Project Structure](#project-structure)  
- [Modeling Pipeline](#modeling-pipeline)  
- [Threshold & Prediction](#threshold--prediction)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Project Overview

This project demonstrates a full data-science workflow, from raw data ingestion through model deployment:

1. **Data Cleaning & EDA**: Load NBA box-score data, inspect data types, handle missing values, and perform exploratory analysis.  
2. **Feature Engineering**: Convert performance stats (minutes, shooting percentages, rebounds, assists, etc.) to numeric form and create a binary target (`HighScorer`) for 20+ point games.  
3. **Modeling & Tuning**: Train a Logistic Regression baseline, remove leaking features, perform stratified cross-validation, and benchmark with a Random Forest.  
4. **Threshold Selection**: Optimize the decision threshold to maximize F1 score, balancing precision and recall.  
5. **Serialization & Deployment**: Serialize the final model, feature list, and threshold; wrap inference logic in a Python module; and build a Streamlit app for interactive predictions.

---

## Features

- **Accurate Predictions**: Classify high-scoring performances (20+ points) with > 97% F1 score.  
- **Flexible Thresholding**: Customize probability cutoff to meet precision/recall requirements.  
- **Interactive Demo**: Streamlit app accepts CSV uploads and displays predictions with probabilities.  
- **Reusable Code**: Clear `src/inference.py` module for loading artifacts and making predictions.  

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/nba-highscorer-predictor.git
   cd nba-highscorer-predictor
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the full dataset**  
   Place `nba_stats.csv` in the `data/` folder. An example CSV is provided in `data/example_nba_stats.csv`.

---

## Usage

### Analysis Notebook

1. Open `notebooks/analysis.ipynb` in VS Code or Jupyter.  
2. Follow the sections to load data, perform EDA, train and evaluate models, and serialize artifacts.

### Streamlit App

1. Run the app:  
   ```bash
   streamlit run app.py
   ```
2. Upload a CSV file (one or more rows of player stats).  
3. View the returned “HighScorer” predictions and probabilities in your browser.

---

## Project Structure

```
nba-highscorer-predictor/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── nba_stats.csv
│   └── example_nba_stats.csv
├── notebooks/
│   └── analysis.ipynb
├── models/
│   ├── highscorer_model.pkl
│   ├── features_list.pkl
│   └── threshold.pkl
├── src/
│   └── inference.py
└── app.py
```

---

## Modeling Pipeline

1. **Data Cleaning**: Inspect `df.dtypes`, convert object columns (e.g. `"FG%"`) to numeric, handle missing values.  
2. **Target Creation**: Create `HighScorer` = 1 if `PTS >= 20`, else 0.  
3. **Feature Selection**: Use key stats (`MP`, `FGA`, `FG%`, `3PA`, `3P%`, `FTA`, `FT%`, `TRB`, `AST`, `STL`, `BLK`, `TOV`).  
4. **Train-Test Split**: Stratified 80/20 split with `random_state=42`.  
5. **Baseline Model**: Logistic Regression → evaluate accuracy, confusion matrix, classification report, ROC AUC.  
6. **Refinement**: Drop leaking features, tune hyperparameters via `GridSearchCV`, benchmark with Random Forest.  

---

## Threshold & Prediction

- **Optimal Threshold**: 0.40 maximizes F1 score (~0.93), balancing precision (0.91) and recall (0.95) on the test set.  
- **Inference**: Use `src/inference.py` functions to load the model, feature list, and threshold, and generate predictions via `predict_highscorer()`.

---

## Contributing

Contributions and suggestions are welcome! Please open an issue or submit a pull request.

---

## License

This project is released under the MIT License.