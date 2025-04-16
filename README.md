# 📌 EmpAttrition

---

*This project aims to help organizations understand, predict, and reduce employee attrition for a more stable and efficient workforce.*

---

## 🔍 What is Attrition?
Attrition refers to the gradual reduction in the number of employees, customers, or other individuals in a group over time. It occurs naturally due to various reasons, such as resignation, retirement, or disengagement.

### 🏢 Employee Attrition
Employee attrition happens when employees leave an organization due to resignation, retirement, or layoffs, and the company does not immediately replace them.

## ⚠️ How Can Employee Attrition Impact a Company?
A decline in the workforce can lead to several negative consequences, such as:

- **Increased Hiring & Training Costs** – Replacing employees requires recruitment, onboarding, and training, which can be expensive and time-consuming.
- **Loss of Knowledge & Expertise** – When experienced employees leave, they take valuable skills and institutional knowledge with them, potentially affecting productivity and decision-making.
- **Lower Employee Morale** – High attrition can create uncertainty and stress among remaining employees, leading to disengagement and lower motivation.
- **Decreased Productivity** – Frequent employee turnover can disrupt workflows, causing delays and inefficiencies.

## 🛠 What Have I Done in This Project?
✅ Inspect various factors contributing to employee attrition.

✅ Utilize Machine Learning & Deep Learning models to predict Employee Attrition Likelihood.

✅ Analyze the outcomes and provide reports & recommendations.

## 🔍 What are the outcomes?

### 1. Key factors that effect employee resignation

- Feature importances and some analysis showed below.

<p align="center">
<img src="https://i.imgur.com/HhOWYA1.png" alt="Key Factors" width="600"/>
</p>
<p align="center">
<img src="https://i.imgur.com/yrVCJVV.png" width="500"> <img src="https://i.imgur.com/rGybojQ.png" width="400">
</p>

### 2. Which model has the best performance?

- Evaluations on various models and various number of features giving the results below

- **Neural Network** model outperforms other traditional models, and it is also chosen to deploy.

<p align="center">
<img src="https://i.imgur.com/cdNMeMw.png" alt="results" width="600"/>
</p>


---

## 🛠️ Deploy the model

- First, cd to the folder:
```bash
    cd DeployModel
```

- Install the libraries (if needed):
```bash
   pip install -r requirements.txt
```
 
- Host your server:
```bash
  python server.py
```
or 
```bash
  uvicorn app:app
```
- Access the address `http://localhost:8000/docs` or `http://127.0.0.1:8000/docs` to view the results.
