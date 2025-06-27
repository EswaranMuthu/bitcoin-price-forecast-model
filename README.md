# bitcoin-price-forecast-model
bitcoin price forecast ml



## 📊 Model Performance

The XGBoost model was evaluated on a 200-sample test set. Here's the classification report:

| Metric     | Class `0` (No Buy) | Class `1` (Buy) | Macro Avg | Accuracy |
|------------|-------------------|-----------------|-----------|----------|
| Precision  | 0.85              | 0.95            | 0.90      |          |
| Recall     | 0.96              | 0.82            | 0.89      |   0.895  |
| F1-Score   | 0.90              | 0.88            | 0.89      |          |
| Support    | 104               | 96              |           |   200    |

- ✅ **High precision for 'Buy' signals (0.95)** — fewer false positives
- ✅ Good **overall balance** in F1-score (~0.89)
- ✅ Can be used for **day trading signal filtering**

# 📈 Bitcoin Price Movement Prediction using XGBoost

This project aims to build a machine learning model that can **predict short-term Bitcoin (BTC) price direction**, labeling each day with a "Buy" signal (`1`) if the price is expected to go up the next day, or `0` otherwise. The model is trained using **enriched historical BTC data**, with technical features like volatility and volume changes, and evaluated using XGBoost.
download btc historical dataset.


## 📊 Dataset

- **Source**: [Kaggle - Historical Bitcoin Prices](https://www.kaggle.com/datasets) *(insert actual link if public)*
- Data contains daily BTC **timestamp, open, high, low, close, and volume**.

## 🏷️ Target Label Creation (Buy Signal)

## 🏷️ Train and test the ML model
