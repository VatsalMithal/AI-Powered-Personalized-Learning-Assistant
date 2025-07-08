## ✅ Problem Statement
Build a machine learning model to predict whether a student will pass or fail a quiz/exam based on their historical activity, time spent, and past scores.

## 📂 Dataset
- **File:** skill_builder_dataset.csv
- **Location:** `data/raw/`
- **Target Variable:** `correct` (1 = Pass, 0 = Fail)

## 🔍 EDA Highlights
- The dataset contains activity-level logs of student interactions.
- Majority of the questions are algebra-based and conducted in tutor mode.
- Several features like attempt count, time to first response, and hint count influence the pass/fail outcome.

## 🔧 Features Used
- attempt_count
- ms_first_response
- hint_count
- hint_total
- overlap_time
- first_action
- opportunity
- opportunity_original
- position
- tutor_mode (encoded)
- answer_type (encoded)
- skill_id (encoded)

## 🤖 Models Tried
- Logistic Regression
- Random Forest (**Best Model**)
- Decision Tree

## 🏆 Best Model
- **Random Forest Classifier**
- Saved as: `random_forest.pkl`

## 🚀 Streamlit App
### Files:
- `streamlit_app.py` → The main app
- Model files and encoders → Stored in `model/` folder

### To Run:
```bash
cd use_case_1/app
streamlit run app1.py
```

## 📈 Folder Structure
```
use_case_1/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── eda.ipynb
│   ├── preprocessing.ipynb
│   └── model_training.ipynb
├── model/
├── app/
│   └── app1.py
├── eda/
└── README.md
```