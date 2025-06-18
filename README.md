# 🔐 Phishing URL Detection using Ensemble Learning

This project aims to detect phishing URLs in real-time using machine learning techniques. It combines **TF-IDF character-level feature extraction** with an **ensemble model** of **XGBoost** and **Random Forest** classifiers, providing accurate and efficient URL classification.

---

## 🚀 Features

- ✅ Detects phishing vs safe URLs with ~96–98% accuracy
- 🔠 Uses character-level n-gram features (TF-IDF)
- 🧠 Ensemble model: XGBoost + Random Forest
- 🌐 Real-time prediction via Flask API
- 🔐 Prevents false negatives for lookalike domains (e.g., `gooogle.com`)
- ✅ Accepts legitimate domains like `google.com` or `www.amazon.com` as safe
- 📦 Exports trained model using `joblib` and `.npz` formats

---

## 🧪 How It Works

1. **Feature Extraction**
   - URLs are vectorized using `TfidfVectorizer` with character n-grams (3 to 5) to capture URL patterns.
   - A sparse matrix is saved using `.npz` format.

2. **Model Training**
   - XGBoost and Random Forest are trained with balanced class weights to prevent bias.
   - VotingClassifier (soft voting) combines both models for better performance.

3. **Prediction**
   - A Flask server takes a URL as input and returns:
     - `safe` or `phishing`
     - A confidence score (rounded to 0 or 1)

---

## 📂 File Structure

```bash
.
├── cleaned_dataset.csv             # Input dataset
├── X_train_sparse.pkl              # TF-IDF features for training (sparse)
├── X_test_sparse.pkl               # TF-IDF features for testing
├── y_train.csv                     # Training labels
├── y_test.csv                      # Test labels
├── phishing_ensemble_model.pkl    # Saved ensemble model
├── tfidf_vectorizer.pkl           # Saved vectorizer
├── app.py                          # Flask API for predictions
├── train_model.py                  # Model training script
├── data_split.py                   # Splits dataset and saves as CSV/sparse
```

## 🧰 Tech Stack
- Python
- Scikit-learn
- XGBoost
- Flask
- Pandas / NumPy
- Joblib
- SciPy

## 🖥️ Running the Project
1. Train the Model
``` bash
python train_model.py
```

2. Start the Flask Server
``` bash
python app.py
```

3. Enable the extension through Chrome adding it to the Chrome Extensions through developer mode
Go to Chrome Extensions (chrome://extensions/) - Enable Developer mode on the top right - Upload the chrome folder from local computer.
![image](https://github.com/user-attachments/assets/14feee8d-4b1c-4be4-87d1-967077027273)

Ensure flask server is running in the background.

4. Using Chrome Extension
Type in any URL in the chrome extension to detect if it's legitimate or phishing website.

Safe Website detection:

![image](https://github.com/user-attachments/assets/f357a475-5422-4708-a4d3-c1743b76e5e3)

Phishing website detection:

![image](https://github.com/user-attachments/assets/f342aaf7-0841-4d6a-bbce-b38f840598f1)
