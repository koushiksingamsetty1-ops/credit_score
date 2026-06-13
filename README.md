# 💳 Credit Score Predictor

An AI-powered Credit Risk Prediction System that helps evaluate loan approval eligibility using Machine Learning techniques.

This application analyzes customer financial and demographic information such as income, credit score, loan amount, education, employment type, and work experience to predict whether a loan is likely to be approved or rejected.

---

## 🚀 Live Demo

Access the deployed application on Hugging Face Spaces.

---

## ✨ Features

* Real-time loan approval prediction
* Interactive and user-friendly interface
* Machine Learning-based decision making
* Credit risk assessment
* Fast and accurate predictions
* Cloud deployment using Hugging Face Spaces

---

## 📊 Input Parameters

The model uses the following features:

| Feature         | Description               |
| --------------- | ------------------------- |
| Age             | Applicant age             |
| Income          | Annual income             |
| LoanAmount      | Requested loan amount     |
| CreditScore     | Customer credit score     |
| YearsExperience | Years of work experience  |
| Gender          | Male / Female             |
| Education       | Educational qualification |
| City            | Customer city             |
| EmploymentType  | Employment status         |

---

## 🤖 Machine Learning Models

The project explores multiple machine learning algorithms:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

The final prediction model is stored as:

```bash
credit_risk_model.pkl
```

---

## 🛠️ Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Gradio
* Joblib
* Hugging Face Spaces

---

## 📂 Project Structure

```text
.
├── app.py
├── credit_risk_model.pkl
├── requirements.txt
├── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd credit-score-predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## 📈 Prediction Output

The model predicts:

### ✅ Loan Approved

The applicant satisfies the credit approval criteria.

### ❌ Loan Rejected

The applicant does not meet the required lending criteria.

---

## 🎯 Use Cases

* Banking Applications
* Credit Risk Assessment
* Loan Eligibility Screening
* FinTech Platforms
* Educational Machine Learning Projects

---

## 🔮 Future Enhancements

* Probability-based predictions
* Credit score visualization dashboard
* Risk analysis charts
* Explainable AI (XAI) integration
* Advanced financial analytics

---

## 👨‍💻 Author

Koushik

Machine Learning & AI Enthusiast

---

## 📜 License

This project is intended for educational and demonstration purposes.
