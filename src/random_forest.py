from sklearn.ensemble import RandomForestClassifier

def train_random_forest(X_train, y_train):

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=15,
        min_samples_split=5,
        random_state=42
    )

    model.fit(X_train, y_train)

    feature_importance = model.feature_importances_

    return model, feature_importance
