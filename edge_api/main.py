from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

class InputData(BaseModel):
    features: list

@app.post("/predict")
def predict(data: InputData):
    X = np.array(data.features).reshape(1, -1)

    # Auto-pad or trim to model size
    expected = model.n_features_in_

    if X.shape[1] < expected:
        X = np.pad(X, ((0,0),(0,expected-X.shape[1])))
    elif X.shape[1] > expected:
        X = X[:, :expected]

    pred = model.predict(X)[0]

    return {"prediction": int(pred)}
