import pandas as pd
import scipy.sparse

# Dataset paths
dataset1_path = 'PhiUSIIL_Phishing_URL_Dataset1.csv'  # Change this to your first dataset

def clean_and_extract_features(dataset_path, cleaned_dataset_path, feature_extraction_path):
    df = pd.read_csv(dataset_path, engine='python')
    df = df.drop_duplicates()
    df = df.dropna()
    target_column = 'phishing' if 'phishing' in df.columns else 'label' if 'label' in df.columns else 'status'
    if target_column not in df.columns:
        raise ValueError("No valid target column found in dataset")
    y = df[target_column].map({'legitimate': 0, 'phishing': 1}) if target_column == 'status' else df[target_column]
    url_column = 'URL' if 'URL' in df.columns else 'url' if 'url' in df.columns else None
    if not url_column:
        raise ValueError("No URL column found in dataset")
    df.to_csv(cleaned_dataset_path, index=False)
    print(f"Cleaned dataset saved to {cleaned_dataset_path}")

    from sklearn.feature_extraction.text import TfidfVectorizer
    df_cleaned = pd.read_csv(cleaned_dataset_path)
    url_texts = df_cleaned[url_column].astype(str)
    tfidf_vectorizer = TfidfVectorizer(max_features=200)
    X_tfidf = tfidf_vectorizer.fit_transform(url_texts)
    scipy.sparse.save_npz(feature_extraction_path, X_tfidf)
    print(f"Feature extracted dataset saved to {feature_extraction_path}")

# Process both datasets
clean_and_extract_features(dataset1_path, 'cleaned_dataset1.csv', 'feature_extracted1.npz')
clean_and_extract_features(dataset2_path, 'cleaned_dataset2.csv', 'feature_extracted2.npz')
