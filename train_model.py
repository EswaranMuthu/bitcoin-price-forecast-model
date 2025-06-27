import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report


# Replace with the actual filename you see
df = pd.read_csv("/kaggle/input/bitcoin-historical-data/btcusd_1-min_data.csv")

df_sorted = df.sort_values(by='Timestamp', ascending=False)

# Step 3: Select the top 1000 latest rows
df = df_sorted.head(1000)

df['target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
df['return'] = (df['Close'] - df['Open']) / df['Open']
df['volatility'] = (df['High'] - df['Low']) / df['Low']
df['volume_change'] = df['Volume'].pct_change().fillna(0)

features = ['Open', 'Close', 'High', 'Low', 'Volume', 'return', 'volatility', 'volume_change']
X = df[features]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

model = XGBClassifier(missing=np.inf)
model.fit(X_train, y_train)
preds = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, preds))
print(classification_report(y_test, preds))


# Show first few rows as a table
#print(df)
