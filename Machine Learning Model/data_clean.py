import pandas as pd

dataset1_path = 'PhiUSIIL_Phishing_URL_Dataset1.csv'  

def clean_dataset(dataset_path, cleaned_dataset_path):
    df = pd.read_csv(dataset_path, engine='python')
    df = df.drop_duplicates()
    print(f"Duplicates removed: {df.duplicated().sum()}")
    df = df.dropna()
    print(f"Missing values removed: {df.isnull().sum().sum()}")
    df.to_csv(cleaned_dataset_path, index=False)
    print(f"Cleaned dataset saved to {cleaned_dataset_path}")
clean_dataset(dataset1_path, 'cleaned_dataset1.csv')
