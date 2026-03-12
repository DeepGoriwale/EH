import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# === Load and Prepare Training Data ===
df = pd.read_csv(r"./Dataset.csv")
X = (df["covid"] + " " + df["fever"]).astype(str)
y = df["flu"]

# === Split Data ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# === Vectorize Text Data ===
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# === Train Model ===
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# === Evaluate Model ===
y_pred = model.predict(X_test_vec)
print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# === Test on New Data ===
test_df = pd.read_csv(r"./Test.csv")
new_X = (test_df["covid"] + " " + test_df["fever"]).astype(str)
new_X_vec = vectorizer.transform(new_X)
test_df["flu_prediction"] = model.predict(new_X_vec)

# === Save Results ===
test_df.to_csv(
    r"./Test1.csv", index=False)
print("\nPredictions saved to Test1.csv")
