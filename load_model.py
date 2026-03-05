import joblib
import numpy as np

model = joblib.load("model.joblib")

sample = np.array([[14.23, 1.71, 2.43, 15.6, 127, 2.80, 3.06,
                    0.28, 2.29, 5.64, 1.04, 3.92, 1065]])

prediction = model.predict(sample)

print("Przewidziana klasa wina:", prediction[0])