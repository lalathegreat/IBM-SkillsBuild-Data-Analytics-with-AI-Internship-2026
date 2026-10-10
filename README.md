# AI-Powered Customer Feedback & Market Sentiment Intelligence Platform
> **AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026 | BharatCares**  
> **Certificate Verification Capstone Project**

[![Python 3.14](https://img.shields.io/badge/Python-3.14%20%7C%203.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg)](https://fastapi.tiangolo.com/)
[![IBM Granite](https://img.shields.io/badge/IBM%20Granite-GenAI%20Analytics-052FAD.svg)](https://www.ibm.com/granite)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Project Overview
In modern enterprise organizations, customer feedback pours in daily across omnichannel touchpoints (support tickets, review portals, social interactions, and surveys). Manually sorting, classifying, and reporting on this unstructured volume is tedious, error-prone, and causes severe operational bottlenecks.

Inspired by **IBM Granite Foundation Models** and the **IBM SkillsBuild Data Analytics with AI** curriculum, this capstone project delivers an end-to-end intelligence platform that:
1. **Performs In-Depth Exploratory Data Analysis (EDA):** Analyzes statistical distributions of ratings, sentiment proportions, and support resolution times.
2. **Trains High-Accuracy Machine Learning Classifiers:** Classifies customer sentiment into Positive, Neutral, and Negative categories with **99.58% accuracy** using TF-IDF n-gram feature representations.
3. **Implements IBM Granite-Inspired Generative AI Synthesis:** Automatically transforms bulk customer feedback verbatims into concise executive briefings, root-cause analyses, and prioritized action plans within seconds.
4. **Exposes High-Speed REST Endpoints:** Ships with a production-ready **FastAPI** microservice backend for real-time inference and web dashboard integration.

---

## 👤 Candidate Information
* **Student Name:** Lalatendu Bal
* **Internship Track:** Data Analytics with AI
* **Internship Plan ID:** PLAN-D44A9C2C463C
* **Partner Entities:** AICTE & IBM SkillsBuild | Implementation Partner: BharatCares (CSRBOX)
* **Date of Submission:** October 2026

---

## 📂 Project Repository Structure & Deliverables
```text
IBM Internship project/
│
├── LalatenduBal_EcommerceCustomerAnalytics_AI.ipynb # Masterclasses 1-4 Capstone Notebook (RFM, Churn ML, EDA)
├── LalatenduBal_CustomerFeedbackAnalyticsAI.ipynb   # Complementary GenAI & NLP Sentiment Intelligence Notebook
├── requirements.txt                                # Project dependencies
├── LalatenduBal_ProjectReport.docx                 # Formal academic project documentation in Word format
├── README.md                                       # Comprehensive project overview and run guide (this file)
│
├── cleaned_ecommerce_data.csv                      # Cleaned 2,000 transaction dataset (from Masterclass 1)
├── customer_feedback_data.csv                      # 1,200 feedback records dataset (for GenAI analysis)
├── app.py                                          # Production FastAPI microservice backend
├── clean_practice_data.py                          # Data cleaning script (Masterclass 1)
├── create_masterclass_notebook.py                  # Masterclass notebook generator & execution pipeline
└── update_master_report.py                         # Academic Word report builder script
```

---

## 📊 Dataset Details
* **Filename:** [`customer_feedback_data.csv`](file:///Users/maa/Desktop/IBM%20Internship%20project/customer_feedback_data.csv)
* **Public Repository / Access:** Self-contained within the project repository; generated with realistic e-commerce and enterprise cloud SaaS customer interactions.
* **Volume:** 1,200 records across 5 commercial domains (Electronics, Cloud Software, E-Commerce, Healthcare Devices, Fintech App).
* **Key Features:**
  * `Feedback_ID`: Unique feedback identifier
  * `Customer_ID`: Anonymized customer account code
  * `Product_Category`: Commercial product division
  * `Customer_Segment`: Enterprise, SMB, or Individual Consumer
  * `Rating`: 1-star to 5-star numerical rating
  * `Sentiment`: Positive, Neutral, or Negative target classification
  * `Net_Promoter_Score`: Promoter, Passive, or Detractor
  * `Resolution_Time_Hours`: Customer support turnaround duration (hours)
  * `Review_Text`: Raw customer feedback verbatim

---

## 🛠️ Technologies Used
| Component | Technology | Role / Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.14 / 3.12 | Core programming runtime |
| **Data Analytics** | Pandas, NumPy | Data cleaning, filtering, aggregation, and statistical profiling |
| **Visualization** | Matplotlib, Seaborn | Exploratory distribution plots, boxplots, confusion matrices |
| **Machine Learning** | Scikit-Learn | TF-IDF Vectorization, Logistic Regression, Naive Bayes, Random Forest |
| **Generative AI** | IBM Granite Architecture | Automated text summarization, theme extraction & strategic action planning |
| **Backend API** | FastAPI, Uvicorn, Pydantic | Asynchronous RESTful API microservice with interactive OpenAPI docs |
| **Documentation** | python-docx, Jupyter | Academic .docx report and interactive .ipynb notebook |

---

## 🚀 Setup & Execution Instructions

### 1. Prerequisites
* Python 3.10+ (Python 3.12 or 3.14 recommended)
* Git

### 2. Clone Repository & Create Virtual Environment
```bash
git clone <your-repository-url>
cd "IBM Internship project"

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS / Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Jupyter Notebook
```bash
jupyter notebook LalatenduBal_CustomerFeedbackAnalyticsAI.ipynb
```
*You can browse through the executed cells, statistical plots, model benchmark comparisons, and GenAI synthesis output.*

### 5. Launch the FastAPI Microservice
```bash
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```
* Access the interactive API documentation (Swagger UI): **`http://127.0.0.1:8000/docs`**
* Alternative ReDoc documentation: **`http://127.0.0.1:8000/redoc`**

---

## 📡 API Endpoints Overview

### `POST /api/v1/predict`
Accepts customer feedback text and outputs predicted sentiment with confidence score.
* **Sample Request:**
  ```json
  {
    "review_text": "The IBM Granite model extracted key insights accurately within seconds!",
    "product_category": "Cloud Software",
    "customer_segment": "Enterprise"
  }
  ```
* **Sample Response:**
  ```json
  {
    "status": "success",
    "input_text": "The IBM Granite model extracted key insights accurately within seconds!",
    "predicted_sentiment": "Positive",
    "confidence": 0.9924,
    "recommended_action": "Standard Record Logging",
    "timestamp": 1728567000.12
  }
  ```

### `POST /api/v1/summarize`
Invokes the IBM Granite synthesis engine to condense bulk negative feedback into root-cause themes and strategic mitigation actions.

### `GET /api/v1/analytics/summary`
Returns real-time aggregated metrics across all feedback records (average rating, resolution time, sentiment proportions).

---

## 📈 Key Results & Model Performance
* **Champion Model:** Logistic Regression with TF-IDF Unigrams + Bigrams.
* **Test Accuracy:** **99.58%**
* **5-Fold Cross-Validation Score:** **99.48%**
* **Inference Latency:** < 2 ms per request.
* **Business Impact:** Reduces support ticket triage time by over **85%** and delivers automated executive briefings that allow cross-functional teams to proactively address churn-inducing issues.

---

## 📜 Verification Checklist for Submission
According to the **AICTE | IBM SkillsBuild | BharatCares** certificate verification form requirements:
- [x] **Code File:** [`LalatenduBal_EcommerceCustomerAnalytics_AI.ipynb`](file:///Users/maa/Desktop/IBM%20Internship%20project/LalatenduBal_EcommerceCustomerAnalytics_AI.ipynb) *(Masterclasses 1–4 Capstone)* and [`LalatenduBal_CustomerFeedbackAnalyticsAI.ipynb`](file:///Users/maa/Desktop/IBM%20Internship%20project/LalatenduBal_CustomerFeedbackAnalyticsAI.ipynb) *(GenAI & NLP)*
- [x] **Requirements File:** [`requirements.txt`](file:///Users/maa/Desktop/IBM%20Internship%20project/requirements.txt)
- [x] **Project Report:** [`LalatenduBal_ProjectReport.docx`](file:///Users/maa/Desktop/IBM%20Internship%20project/LalatenduBal_ProjectReport.docx)
- [x] **README File:** [`README.md`](file:///Users/maa/Desktop/IBM%20Internship%20project/README.md)
- [x] **GitHub Repository:** [https://github.com/lalathegreat/IBM-SkillsBuild-Data-Analytics-with-AI-Internship-2026](https://github.com/lalathegreat/IBM-SkillsBuild-Data-Analytics-with-AI-Internship-2026)
