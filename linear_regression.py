from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([40, 50, 60])

model = LinearRegression()
model.fit(X, y)

print(model.predict([[4]]))