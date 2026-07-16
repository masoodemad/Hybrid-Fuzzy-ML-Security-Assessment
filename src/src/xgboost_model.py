from xgboost import XGBClassifier

def train_xgboost(X_train, y_train):

    model = XGBClassifier(
        n_estimators=300,
        max_depth=8,
        learning_rate=0.05,
        subsample=0.80,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model
