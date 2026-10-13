# King County House Price Prediction

## Project Overview

This project uses machine learning to predict house sale prices in King County, Washington, USA, using historical property sales data.

The goal is to compare different regression algorithms and identify which provides the most accurate predictions on unseen test data.

## Dataset

- **Source:** [King County House Sales — Kaggle](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)
- **Records:** 21,613 house sales
- **Original columns:** 21
- **Target variable:** `price`

The dataset includes property characteristics such as living area, bedrooms, bathrooms, property grade and location.

## Data Preparation

The project included:

- Exploring the dataset and checking for missing values and duplicate rows.
- Investigating unusual values.
- Handling zero bedroom and bathroom values as missing for modelling.
- Imputing missing feature values.
- Encoding ZIP codes using one-hot encoding.
- Creating sale year and sale month features.
- Splitting the data into training and testing sets, keeping repeated property IDs separate.

## Models Compared

Three regression algorithms were evaluated:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

The models were compared using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE) and R-squared (R²).

## Results

Random Forest performed best among the three models tested.

| Metric | Random Forest |
|---|---:|
| Test MAE | Approximately $67,713 |
| Test RMSE | Approximately $119,702 |
| Test R² | Approximately 0.897 |

The test MAE means that the average absolute difference between predicted and actual house prices was approximately $67,713.

## Conclusion

Random Forest achieved the lowest test prediction error among the models evaluated. However, predictions are estimates, not guaranteed sale prices. Further independent validation would be needed before using the model in a real-world business setting.

## Tools and Technologies

- Python
- pandas
- NumPy
- Matplotlib
- Seaborn
- scikit-learn
- Jupyter Notebook

## How to Run

1. Download or obtain the dataset from the source above.
2. Set up the project's Python environment and install its dependencies.
3. Open the Jupyter Notebook in VS Code.
4. Run all notebook cells from beginning to end.