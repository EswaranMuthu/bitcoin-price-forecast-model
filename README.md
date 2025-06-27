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
