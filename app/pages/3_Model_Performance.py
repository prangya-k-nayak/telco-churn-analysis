import sys
from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

project_root = Path(__file__).resolve().parent.parent.parent

if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import streamlit as st

from src.ui.styles import apply_theme
from src.data.loader import load_telco_churn_data
from src.models.evaluate import evaluate_model
from src.models.save_model import save_model
import joblib

st.set_page_config(page_title="Model Performance", page_icon="🤖")

apply_theme()

st.title("🤖 Model Performance")

df = load_telco_churn_data()

# ---------------- Preprocessing ---------------- #

df = df.drop("customerID", axis=1)

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce",
)

df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].median()
)

encoders = {}

for col in df.columns:
    if not pd.api.types.is_numeric_dtype(df[col]):
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col].astype(str))
        encoders[col] = encoder

X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

joblib.dump(encoders, "models/label_encoders.pkl")
joblib.dump(scaler, "models/scaler.pkl")

# ---------------- Logistic Regression ---------------- #

log_model = LogisticRegression(max_iter=1000)

log_model.fit(X_train, y_train)

save_model(log_model, "logistic_regression.pkl")

y_pred_log = log_model.predict(X_test)

log_acc, log_report, log_matrix = evaluate_model(
    y_test,
    y_pred_log,
)

# ---------------- Random Forest ---------------- #

rf_model = RandomForestClassifier(random_state=42)

rf_model.fit(X_train, y_train)

save_model(rf_model, "random_forest.pkl")

y_pred_rf = rf_model.predict(X_test)

rf_acc, rf_report, rf_matrix = evaluate_model(
    y_test,
    y_pred_rf,
)

# ---------------- Results ---------------- #

col1, col2 = st.columns(2)

col1.metric(
    "Logistic Regression Accuracy",
    f"{log_acc:.2%}",
)

col2.metric(
    "Random Forest Accuracy",
    f"{rf_acc:.2%}",
)

st.divider()

st.subheader("Classification Report")

model = st.selectbox(
    "Select Model",
    [
        "Logistic Regression",
        "Random Forest",
    ],
)

if model == "Logistic Regression":
    st.dataframe(pd.DataFrame(log_report).transpose(), width="stretch")
else:
    st.dataframe(pd.DataFrame(rf_report).transpose(), width="stretch")

st.divider()

st.subheader("Confusion Matrix")

if model == "Logistic Regression":

    fig, ax = plt.subplots(figsize=(5,4))

    ConfusionMatrixDisplay(
        confusion_matrix=log_matrix
    ).plot(ax=ax)

    st.pyplot(fig)

else:

    fig, ax = plt.subplots(figsize=(5,4))

    ConfusionMatrixDisplay(
        confusion_matrix=rf_matrix
    ).plot(ax=ax)

    st.pyplot(fig)

st.divider()

st.subheader("Top 10 Important Features")

feature_importance = pd.DataFrame(
    {
        "Feature": X.columns,
        "Importance": rf_model.feature_importances_,
    }
)

feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False,
).head(10)

import plotly.express as px

fig = px.bar(
    feature_importance,
    x="Importance",
    y="Feature",
    orientation="h",
    color="Importance",
    title="Top 10 Important Features",
)

fig.update_layout(
    yaxis=dict(autorange="reversed")
)

st.plotly_chart(
    fig,
    width="stretch",
)

st.caption(
    "Higher importance values indicate features that contributed more to the Random Forest model's predictions."
)

st.divider()

st.subheader("🏆 Model Summary")

best_model = (
    "Random Forest"
    if rf_acc > log_acc
    else "Logistic Regression"
)

st.success(f"""
### Best Performing Model

**{best_model}** achieved the highest accuracy on the test dataset.

The comparison suggests that this model is better suited for predicting customer churn for this dataset.

The feature importance chart above highlights the variables that contributed most to the predictions.
""")