import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import numpy as np

dataset_path = 'cleaned_dataset.csv'
df = pd.read_csv(dataset_path)

target_column = 'phishing' if 'phishing' in df.columns else 'label' if 'label' in df.columns else 'status'
url_column = 'URL' if 'URL' in df.columns else 'url' if 'url' in df.columns else None

if not url_column:
    raise ValueError("No URL column found in dataset")

y = df[target_column].map({'legitimate': 0, 'phishing': 1}) if target_column == 'status' else df[target_column]
url_texts = df[url_column].astype(str)

tfidf_vectorizer = TfidfVectorizer(max_features=500)
X_tfidf = tfidf_vectorizer.fit_transform(url_texts)

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_tfidf, y)
feature_importances = rf_model.feature_importances_
feature_names = tfidf_vectorizer.get_feature_names_out()

sorted_indices = np.argsort(feature_importances)[::-1][:20]
top_features = [(feature_names[i], feature_importances[i]) for i in sorted_indices]

print("Top 20 Most Important Features for Phishing Detection:")
for feature, importance in top_features:
    print(f"{feature}: {importance:.4f}")

thresh = np.percentile(feature_importances, 80)  
common_features = [feature_names[i] for i in sorted_indices if feature_importances[i] >= thresh]
print("\nCommon Phishing Features:", common_features[:10])  

thresh_unique = np.percentile(feature_importances, 95) 
unique_features = [feature_names[i] for i in sorted_indices if feature_importances[i] >= thresh_unique]
print("\nUnique Phishing Features:", unique_features[:10])

feature_analysis_path = 'phishing_feature_analysis.txt'
with open(feature_analysis_path, 'w') as f:
    f.write("Top 20 Most Important Features for Phishing Detection:\n")
    for feature, importance in top_features:
        f.write(f"{feature}: {importance:.4f}\n")
    f.write("\nCommon Phishing Features:\n" + ", ".join(common_features[:10]))
    f.write("\nUnique Phishing Features:\n" + ", ".join(unique_features[:10]))

print(f"Feature analysis saved to {feature_analysis_path}")
