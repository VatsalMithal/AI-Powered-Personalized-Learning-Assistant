
# 🎓 AI-Powered Personalized Learning Assistant

This repository contains the code, models, and Streamlit apps for multiple educational machine learning use cases designed to assist and personalize student learning.

---

## ✅ Use Case 1: Student Pass/Fail Prediction
### Problem:
Predict whether a student will pass or fail a quiz/exam based on their historical activity.

### Dataset:
- **File:** skill_builder_dataset.csv
- **Target:** `correct` (1 = Pass, 0 = Fail)

### Best Model:
Random Forest Classifier

### Streamlit App:
```bash
cd use_case_1/app
streamlit run app1.py
```

---

## ✅ Use Case 2: Student Score Prediction
### Problem:
Predict a student's future score (0-100) using historical data.

### Dataset:
- **File:** skill_builder_dataset.csv
- **Target:** Continuous score (calculated)

### Best Model:
Random Forest Regressor

### Streamlit App:
```bash
cd use_case_2/app
streamlit run app2.py
```

---

## ✅ Use Case 3: Student Learning Style Clustering
### Problem:
Cluster students based on their learning behavior into groups like Fast Learners, Visual Learners, Slow Learners.

### Dataset:
- **File:** skill_builder_dataset.csv (processed)

### Best Clustering:
MiniBatchKMeans & DBSCAN

### Streamlit App:
```bash
cd use_case_3/app
streamlit run app3.py
```

---

## ✅ Use Case 4: Student Dropout Prediction
### Problem:
Predict whether a student is at risk of dropping out.

### Dataset:
- **File:** student_dropout_data.csv
- **Target:** `dropout_flag`

### Best Model:
Random Forest Classifier

### Streamlit App:
```bash
cd use_case_4/app
streamlit run app4.py
```

---

## ✅ Use Case 5: Topic Detection from Essays
### Problem:
Classify student essays into topics.

### Dataset:
- **File:** essay_dataset.csv
- **Target:** Essay topic

### Best Model:
LSTM Model

### Streamlit App:
```bash
cd use_case_5/app
streamlit run app5.py
```

---

## ✅ Use Case 6: Handwritten Digit Recognition
### Problem:
Recognize handwritten digits from images.

### Dataset:
- **Dataset:** MNIST

### Best Model:
CNN Model

### Streamlit App:
```bash
cd use_case_6/app
streamlit run app6.py
```

---

## ✅ Use Case 7: AI-Based Topic Summarizer
### Problem:
Summarize educational topics using AI-based text summarization.

### Dataset:
- **File:** topics.csv

### Best Model:
T5-small (Huggingface Transformers)

### Streamlit App:
```bash
cd use_case_7/app
streamlit run app7.py
```

---

## 👨‍💻 Created By:
Vatsal Mithal
---

## 📂 General Folder Structure:
```
use_case_X/
├── data/
├── notebooks/
├── app/
├── model/
├── eda/
└── README.md
```
