# 📚 Book Review Sentiment Classifier

This project builds a **sentiment analysis classifier** using book reviews data. The model categorizes reviews into **Positive**, **Negative**, or **Neutral** based on the rating score, and uses **Machine Learning** techniques like SVM, Decision Tree, Logistic Regression, and more.

---

## 💡 What is Sentiment Analysis?

Sentiment Analysis is the process of **identifying the emotional tone** behind a piece of text. Here, we use it to classify reviews as:

* `POSITIVE` (rating > 3)
* `NEUTRAL` (rating == 3)
* `NEGATIVE` (rating <= 2)

---

## 🗂 Dataset

* 📁 **File:** `Books_small_10000.json`
* 📌 Format: JSON lines (`.jsonl`)
* 📌 Fields used:

  * `reviewText`: The content of the review
  * `overall`: The rating (used for determining sentiment)

---

## 🏗️ Project Structure

```plaintext
.
├── models/
│   └── sentiment_classifier.pkl  # Saved trained model
├── Books_small_10000.json        # Dataset
├── sentiment_analysis.py         # Main code
└── README.md                     # Project guide
```

---

## 🛠️ Steps and Concepts

### 1. 📦 Data Loading & Preprocessing

```python
with open(file_name, "r") as f:
    for line in f:
        review = json.loads(line)
        reviews.append(Review(review["reviewText"], review["overall"]))
```

**Concepts:**

* JSONL: Each line is a separate JSON object.
* `Review` class: Converts rating to sentiment using a helper function.

---

### 2. 📤 Data Splitting

```python
from sklearn.model_selection import train_test_split
training, test = train_test_split(reviews, test_size=0.33, random_state=42)
```

**Concepts:**

* Splits data into training (67%) and test (33%) sets to evaluate performance.

---

### 3. 📏 Balancing Classes

```python
train_container.evenly_distribute()
```

**Concept:**

* Keeps equal number of positive and negative samples for unbiased training.

---

### 4. ✨ Vectorization

```python
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
```

**Concepts:**

* `Bag of Words`: Converts text to numerical vectors.
* `TF-IDF`: Adds importance based on frequency across documents.

---

### 5. 🤖 Classifiers Used

#### 🔹 Support Vector Machine (SVM)

```python
from sklearn import svm
clf_svm = svm.SVC(kernel='linear')
```

#### 🔹 Decision Tree

```python
from sklearn.tree import DecisionTreeClassifier
clf_dec = DecisionTreeClassifier()
```

#### 🔹 Naive Bayes *(Note: GaussianNB not used correctly here — works with dense arrays only)*

```python
from sklearn.naive_bayes import GaussianNB
# Would throw error unless converted to dense arrays
```

#### 🔹 Logistic Regression

```python
from sklearn.linear_model import LogisticRegression
clf_log = LogisticRegression()
```

---

### 6. 📊 Evaluation

```python
from sklearn.metrics import f1_score
```

**Metrics:**

* `.score()`: Returns **accuracy**.
* `f1_score()`: Balanced metric considering both precision and recall.

---

### 7. 🔎 Grid Search

```python
from sklearn.model_selection import GridSearchCV
```

**Concept:**

* Finds best model hyperparameters using cross-validation.

---

### 8. 💾 Saving and Loading Model

```python
import pickle
with open('sentiment_classifier.pkl', 'wb') as f:
    pickle.dump(clf, f)

with open('sentiment_classifier.pkl', 'rb') as f:
    loaded_clf = pickle.load(f)
```

**Concept:**

* Save model for future use without retraining.

---

### 9. 🧪 Test It

```python
test_set = ["Yooo it was a really good movie", "bad book bro"]
new_test = vectorizer.transform(test_set)
clf_svm.predict(new_test)
```

---

## 🧰 Dependencies

Install the required packages using:

```bash
pip install scikit-learn numpy
```

---

## 🧠 Concepts Recap

| Concept           | Explanation                                               |
| ----------------- | --------------------------------------------------------- |
| **Sentiment**     | Opinion category (Positive, Negative, Neutral)            |
| **TF-IDF**        | Text-to-number technique; boosts words that are important |
| **Vectorization** | Converting raw text into numerical form                   |
| **SVM**           | Classifier that finds the best margin between classes     |
| **GridSearchCV**  | Automated way to find best model parameters               |
| **F1 Score**      | Accuracy measure combining precision and recall           |
| **Pickle**        | Python's object serialization tool                        |

---

## 🚀 Future Improvements

* Add support for `NEUTRAL` class in classification.
* Use `GaussianNB` correctly with `.toarray()`.
* Include stopword removal and stemming.
* Visualize with a confusion matrix.

---
