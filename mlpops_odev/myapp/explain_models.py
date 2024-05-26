import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from .utils import load_and_prepare_data
import os

def explain_model():
    try:
        print("Veriler yükleniyor...")
        X_train, X_test, y_train, y_test = load_and_prepare_data('datasets/cleaned_data.csv')
        
        print("Model eğitiliyor...")
        model = RandomForestRegressor()
        model.fit(X_train, y_train)

        print("SHAP değerleri hesaplanıyor...")
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X_test)

        print("SHAP grafiği oluşturuluyor...")
        shap.summary_plot(shap_values, X_test)
        shap_plot_path = os.path.join('static', 'shap_summary_plot.png')
        plt.savefig(shap_plot_path)

        print(f"SHAP grafiği kaydedildi: {shap_plot_path}")
        return shap_plot_path

    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return None
