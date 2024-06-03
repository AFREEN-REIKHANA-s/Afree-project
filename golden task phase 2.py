import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

# Load the dataset
df = pd.read_csv("C:\\Users\\HP\\Downloads\\emails.csv")

# Visualize spam distribution with a pie chart
plt.figure(figsize=(6, 6))
df['spam'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['blue', 'orange'])
plt.ylabel('')
plt.title('Spam Distribution')
plt.show()

# Prepare data
X = df['text'].astype(str)
y = df['spam'].replace({0: "Not Spam", 1: "Spam"}).astype("object")

# Vectorize text data
def create_vocabulary(data):
    vocabulary = defaultdict(lambda: len(vocabulary))
    for text in data:
        for word in text.split():
            vocabulary[word]
    return vocabulary

def vectorize_text(data, vocabulary):
    X_vectorized = np.zeros((len(data), len(vocabulary)))
    for i, text in enumerate(data):
        for word in text.split():
            if word in vocabulary:
                X_vectorized[i, vocabulary[word]] += 1
    return X_vectorized

# Box plot of email lengths
plt.figure(figsize=(8, 6))
email_lengths = X.str.len()
plt.boxplot(email_lengths, patch_artist=True, boxprops=dict(facecolor='skyblue', color='black'), 
            whiskerprops=dict(color='black'), capprops=dict(color='black'), 
            medianprops=dict(color='red'))
plt.xlabel('Emails')
plt.ylabel('Length')
plt.title('Box Plot of Email Lengths')
plt.grid(True)
plt.show()

# Heatmap of email lengths vs. spam
plt.figure(figsize=(8, 6))
spam_labels = y.replace({"Not Spam": 0, "Spam": 1})
heatmap_data = pd.DataFrame({'email_length': email_lengths, 'spam': spam_labels})
heatmap_data['count'] = 1
heatmap_pivot = heatmap_data.pivot_table(index='spam', columns='email_length', values='count', aggfunc='sum', fill_value=0)
plt.imshow(heatmap_pivot, aspect='auto', cmap='YlOrRd', interpolation='nearest')
plt.colorbar()
plt.xlabel('Email Length')
plt.ylabel('Spam')
plt.title('Heatmap of Email Length vs. Spam')
plt.yticks([0, 1], ['Not Spam', 'Spam'])
plt.show()

# Train and evaluate Naive Bayes classifier
class NaiveBayes:
    def _init_(self):
        self.log_prior = {}
        self.log_likelihood = {}
    
    def fit(self, X, y):
        classes, counts = np.unique(y, return_counts=True)
        total_docs = len(y)
        for cls, count in zip(classes, counts):
            self.log_prior[cls] = np.log(count / total_docs)
            class_indices = np.where(y == cls)
            word_counts = X[class_indices].sum(axis=0)
            total_words = word_counts.sum()
            self.log_likelihood[cls] = np.log((word_counts + 1) / (total_words + len(word_counts)))

    def predict(self, X):
        predictions = []
        for doc in X:
            posterior = {}
            for cls in self.log_prior:
                posterior[cls] = self.log_prior[cls] + np.dot(doc, self.log_likelihood[cls])
            predictions.append(max(posterior, key=posterior.get))
        return predictions

# Assuming we have fitted the model and have predictions to plot the confusion matrix

# Plot confusion matrix (dummy values used for illustration)
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay # type: ignore

# Assuming y_true and y_pred are obtained from model predictions
y_true = y
y_pred = y # Placeholder; replace with actual predictions

conf_matrix = confusion_matrix(y_true, y_pred, labels=["Not Spam", "Spam"])
fig, ax = plt.subplots(figsize=(6, 4))
disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=["Not Spam", "Spam"])
disp.plot(ax=ax, cmap='Blues')
plt.title('Confusion Matrix')
plt.show()

# Test with custom messages
custom_messages = [
    'Hi, my name is Harsh Shah and I am sending this email to you.',
    'Hi, it is Elon Musk here and I am giving you a $10,000,000 for free.'
]

for msg in custom_messages:
    print("Your message will be disappeared")