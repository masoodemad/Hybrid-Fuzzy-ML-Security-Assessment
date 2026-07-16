import shap

def generate_shap_values(model, X):

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X)

    return shap_values
