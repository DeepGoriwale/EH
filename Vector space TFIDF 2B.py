from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from nltk.corpus import stopwords
import nltk, numpy as np
from numpy.linalg import norm

#nltk.download('stopwords')
vectorizer = CountVectorizer(stop_words=stopwords.words('english'))
transformer = TfidfTransformer()

train = ["The sky is blue.", "The sun is bright."]
test = ["The sun in the sky is bright."]

train_tfidf = transformer.fit_transform(vectorizer.fit_transform(train)).toarray()
test_tfidf = transformer.transform(vectorizer.transform(test)).toarray()

cosine = lambda a, b: round(np.dot(a, b) / (norm(a) * norm(b)), 3)

for i, v in enumerate(train_tfidf, 1):
    print(f"Cosine similarity (Test vs Train {i}): {cosine(v, test_tfidf[0])}")

print("Performed by 740_Pallavi & 743_Deepak")
