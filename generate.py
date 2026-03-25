import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Load data
data_root = "https://github.com/ageron/data/raw/main/"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")

# 2. Prepare data (Corrected spelling: 'capita' and 'satisfaction')
X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

# 3. Visualize data (Corrected spelling: 'capita')
lifesat.plot(kind='scatter', grid=True,
             x="GDP per capita (USD)", y="Life satisfaction")

# 4. Set axis limits (Corrected syntax: use parentheses () to call the function)
plt.axis([23_500, 62_500, 4, 9])
plt.show()

# 5. Select and train the model
model = LinearRegression()
model.fit(X, y)

# 6. Make a prediction
X_new = [[37_655.2]]
print(f"Prediction for Cyprus: {model.predict(X_new)}")
