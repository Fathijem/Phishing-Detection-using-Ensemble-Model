import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

dataset_path = "cleaned_dataset.csv"  
df = pd.read_csv(dataset_path)
url_column = 'url' if 'url' in df.columns else 'URL'
url_texts = df[url_column].astype(str)
tfidf_vectorizer = TfidfVectorizer(max_features=500)
X_tfidf = tfidf_vectorizer.fit_transform(url_texts)
joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.pkl')
print("Feature extraction complete. TF-IDF vectorizer saved as tfidf_vectorizer.pkl")
