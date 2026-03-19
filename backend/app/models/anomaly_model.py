from sklearn.ensemble import IsolationForest

def train_model(X):
    model = IsolationForest(
        n_estimators=100,
        contamination=0.1,  # 10% anomalies expected
        random_state=42
    )
    model.fit(X)
    return model


def predict(model, X):
    preds = model.predict(X)
    return preds