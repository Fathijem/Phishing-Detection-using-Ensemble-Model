import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier, VotingClassifier  # Fixed import
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

dataset_path = "cleaned_dataset.csv"
df = pd.read_csv(dataset_path)

url_column = 'url' if 'url' in df.columns else 'URL'
target_column = 'phishing' if 'phishing' in df.columns else 'label'

tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
X_tfidf = tfidf_vectorizer.transform(df[url_column].astype(str))

y = df[target_column].map({'legitimate': 0, 'phishing': 1}) if target_column == 'status' else df[target_column]

X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

xgb = XGBClassifier(eval_metric='logloss')
rf = RandomForestClassifier(n_estimators=100, random_state=42)

ensemble_model = VotingClassifier(estimators=[('xgb', xgb), ('rf', rf)], voting='soft')  # Corrected
ensemble_model.fit(X_train, y_train)

y_pred = ensemble_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Ensemble Model Accuracy: {accuracy:.4f}")
print("Classification Report:\n", classification_report(y_test, y_pred))

joblib.dump(ensemble_model, 'phishing_ensemble_model.pkl')
print("Model saved as phishing_ensemble_model.pkl")
