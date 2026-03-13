# AI-Powered Personalized Learning Assistant

### Capstone Project

## Project Description
The **AI-Powered Personalized Learning Assistant** is an intelligent educational system designed to enhance learning experiences for school and college students using **Artificial Intelligence, Machine Learning, Deep Learning, Natural Language Processing, and Large Language Models (LLMs).**
Traditional education systems follow a **one-size-fits-all approach**, which does not adapt to the individual learning pace and abilities of students. This project aims to create an AI-driven system that can analyze student behavior, predict academic outcomes, personalize learning paths, and generate automated summaries and insights to support students and educators. 
The assistant integrates multiple AI components such as:
* Predictive analytics for student performance
* Learning style clustering
* Dropout risk detection
* NLP-based topic classification
* Computer vision for handwritten digit recognition
* LLM-based content summarization
By combining **machine learning models, deep learning architectures, and generative AI tools**, the system provides a comprehensive personalized learning environment.

---
# Table of Contents
1. Project Description
2. Problem Statement
3. Business Use Cases
4. Features
5. Technologies Used
6. Installation
7. Machine Learning & AI Models
8. Project Workflow
9. Evaluation Metrics
10. Key Insights
11. Future Improvements
12. Credits
13. Author

---
# Problem Statement
Students have **different learning speeds, styles, and preferences**, yet traditional teaching methods often treat all students the same. This results in:
* Slow learners struggling to keep up
* Advanced learners not being challenged
* Teachers being unable to provide individualized support

There is a growing need for an **AI-driven personalized learning system** that can:
* Continuously assess student performance
* Adapt content delivery dynamically
* Generate quizzes, summaries, and explanations automatically
* Provide insights to teachers and parents about student progress

This project addresses these challenges by building a **multi-model AI system** that supports adaptive learning. 

---

# Business Use Cases
The system can be used by:
### EdTech Platforms
To integrate personalized learning paths into their Learning Management Systems (LMS).

### Schools & Universities
To monitor student progress and provide targeted learning support.

### Parents
To understand their child’s learning behavior and identify areas needing improvement.

Potential revenue models include:
* Subscription-based learning platforms
* Institutional licensing
* AI-generated learning resources

---
# Features
* Predict student exam outcomes
* Predict future score ranges
* Identify student learning styles
* Detect dropout risk
* Classify essay topics using NLP
* Recognize handwritten digits using CNN
* Generate AI summaries of educational content
* Personalized learning insights and recommendations
* Interactive UI for analysis and predictions

---
# Technologies Used
### Programming & Data Processing
* Python
* Pandas
* NumPy

### Machine Learning
* Scikit-learn
* XGBoost

### Deep Learning
* TensorFlow
* PyTorch

### NLP & Generative AI
* Hugging Face Transformers
* GPT / LLM Models

### Data Visualization
* Matplotlib
* Seaborn

### Databases
* SQL 

### Deployment
* Streamlit

### Cloud Platforms
* AWS
These technologies are mentioned as part of the **skills required to complete the project**. 

---
# Installation
- Clone the repository - git clone https://github.com/VatsalMithal/AI-Powered-Personalized-Learning-Assistant
- Navigate to the project directory - cd AI-Powered-Personalized-Learning-Assistant
- Install dependencies - pip install -r requirements.txt
- Run the application - streamlit run streamlit_app.py

---
# Machine Learning & AI Models
The project implements **seven AI use cases**.

### 1️⃣ Student Pass/Fail Prediction
Model: **Logistic Regression**

Predict whether a student will pass or fail an exam based on:
* Time spent learning
* Past scores
* Activity history

---

### 2️⃣ Score Range Prediction
Models:
* Random Forest Regressor
* Linear Regression
  
Predict student exam scores (0-100) using learning behavior and topic difficulty.

---

### 3️⃣ Learning Style Clustering
Model: **K-Means Clustering**

Cluster students into categories such as:
* Fast learners
* Slow learners
* Visual learners

---
### 4️⃣ Dropout Risk Detection
Model: **XGBoost Classifier**

Identify students likely to drop out based on:
* Low engagement
* Inactivity
* Poor academic performance

---
### 5️⃣ Topic Detection from Student Answers
Model: **LSTM / BiLSTM**

Classify essay text into academic topics using deep learning NLP.

---

### 6️⃣ Handwritten Digit Recognition
Model: **Convolutional Neural Network (CNN)**

Recognize handwritten digits from student math assignments using the **MNIST dataset**.

---

### 7️⃣ AI Topic Summarizer
Model: **Large Language Model (LLM)**

Generate simplified summaries of long educational articles using **GPT or Hugging Face models**.

---
# Project Workflow
1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Machine Learning Model Training
6. Deep Learning Model Implementation
7. NLP Processing and Topic Classification
8. LLM-based Text Summarization
9. Model Evaluation
10. Interactive Dashboard Deployment

---
# Evaluation Metrics
### Classification Models
* Accuracy
* Precision
* Recall
* F1-Score
* AUC-ROC

### Regression Models
* Mean Absolute Error (MAE)
* Root Mean Square Error (RMSE)

### Clustering Models
* Silhouette Score
* Davies-Bouldin Index

### NLP Models
* BLEU Score
* ROUGE Score
These metrics are used to evaluate model performance and ensure reliable predictions. 

---

# Key Insights
* Student engagement data can strongly predict academic performance.
* Clustering helps identify **different learning behaviors among students**.
* Dropout prediction models can help institutions **intervene early**.
* Deep learning models can classify text topics effectively.
* CNN models perform highly accurately for handwritten digit recognition tasks.
* LLM-based summarization helps students **quickly understand complex learning materials**
These insights demonstrate how **AI can improve educational outcomes through adaptive learning systems.**

---
# Future Improvements
* Build a full **AI tutoring chatbot**
* Implement **real-time adaptive learning recommendations**
* Deploy the system on **cloud platforms**
* Integrate **voice-based learning assistance**
* Develop a **mobile learning application**

---
# Credits
This project was developed as part of the **Master of Data Science Certification Program** provided by **GUVI – HCL and IIT Madras(IITM)**
Project guidance and learning support were provided by the **program mentors**, with development assistance from **ChatGPT**.

---

# Author

**Vatsal Mithal**

Aspiring **Data / Business Analyst**

---
