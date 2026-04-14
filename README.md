# Customer Attrition Prediction & Retention Strategy

## Business Problem

Customer attrition is one of the most critical drivers of revenue loss in subscription-based businesses. This project is designed to answer:

> **Which customers are most likely to attrite, when does attrition occur, and what actions can be taken to improve retention?**

From a business perspective, the goal is to:

* Reduce wasted customer acquisition cost
* Identify high-risk customers early
* Improve retention, especially in the early customer lifecycle

---

## Key Questions Answered

* What is the overall attrition rate and how severe is it?
* At what stage in the customer lifecycle does attrition primarily occur?
* Which customers are most at risk?
* How can the business intervene to reduce attrition?

---

## Executive Summary (Key Insights)

* **Extremely high attrition rate (~88.3%)** indicates a systemic retention issue.
* Attrition is **heavily concentrated in the first 6 months**, with a near-total drop-off in the earliest stage.
* Even after early stages, attrition remains consistently high (~76–80%), suggesting ongoing retention challenges.
* The business is experiencing **rapid early-stage drop-off**, meaning customers leave before generating meaningful long-term value.

---

## Business Insights

### 1. Early Lifecycle is the Critical Failure Point

* Customers with **0–6 months tenure have a 100% attrition rate**
* Customers with **6–12 months tenure have ~98% attrition**

👉This indicates:

* Weak onboarding experience
* Lack of early engagement
* Misalignment between product expectations and value

---

### 2. Retention Does Not Stabilize Over Time

* Even after 12+ months, attrition remains between **76–80%**

👉This suggests:

* Retention issues are not limited to onboarding
* There may be ongoing dissatisfaction or lack of long-term value

---

### 3. Attrition is a Structural Business Problem

* Only **117 out of 1000 customers are retained (~11.7%)**

👉 This indicates:

* A systemic issue, not a segment-specific problem
* High customer acquisition cost is likely being wasted

---

## Customer Lifecycle Funnel Analysis

To understand how customers move through the lifecycle, a funnel-style segmentation was created.

### Funnel Breakdown

| Stage                | Count |
| -------------------- | ----- |
| Total Customers      | 1000  |
| Retained             | 117   |
| At Risk (Tenure < 6) | 252   |
| Attrited             | 883   |

### Key Takeaways

* The majority of customers attrite, confirming a **critical retention problem**
* A large portion of users are still in the **high-risk early tenure stage**
* The business is experiencing **early drop-off rather than gradual attrition**

---

## Tenure-Based Retention Analysis (Cohort Proxy)

Due to the absence of customer start dates, a cohort proxy analysis was performed using tenure.

### Attrition Rate by Tenure Group

| Tenure Group | Retained | Attrited |
| ------------ | -------- | -------- |
| 0–6          | 0.00     | 1.00     |
| 6–12         | 0.02     | 0.98     |
| 12–24        | 0.23     | 0.77     |
| 24–48        | 0.22     | 0.78     |
| 48–72        | 0.20     | 0.80     |

### Interpretation

* **Attrition is highest at the earliest stages**, confirming lifecycle-driven loss
* Retention improves slightly after 12 months but remains weak overall
* The first 6 months represent the **highest-impact intervention window**

---

## Key Metrics (North Star Metrics)

* **Attrition Rate** → % of customers who leave
* **Retention Rate** → % of customers who stay
* **Average Tenure** → indicator of customer loyalty
* **Monthly Charges** → proxy for revenue per customer

---

## Exploratory Data Analysis (EDA)

The EDA phase focused on identifying patterns between customer characteristics and attrition.

### Key Findings

* Customers with **low tenure are significantly more likely to attrite**
* **Higher monthly charges** may correlate with increased attrition risk
* The dataset is heavily skewed toward attrited customers, reinforcing the severity of the problem

### Business Interpretation

Attrition is not random — it is **predictable and strongly tied to customer lifecycle stage**, particularly early tenure.

---

## Model Overview

A machine learning model was developed to predict attrition using:

* Age
* Gender
* Tenure
* Monthly Charges

---

## Deployment

A Streamlit application enables real-time attrition prediction. (https://customer-attrition-predictor-qj5nts4qsxw74mtp6uts3o.streamlit.app/)

---

## Business Recommendations

* Improve onboarding for early-stage customers
* Implement proactive retention strategies
* Investigate pricing sensitivity
* Monitor attrition continuously

---

## Final Takeaway

This project identifies:

* **Where attrition happens**
* **Why it happens**
* **How to reduce it**

> The largest opportunity lies in improving early-stage customer experience.

---

## Future Improvements

### 1. Cohort Analysis (with Proper Time Data)

If customer start dates or signup dates become available, a true cohort analysis could be performed to measure retention and attrition across customer groups over time. This would help identify whether newer customer groups perform better or worse than earlier ones.

### 2. Survival Analysis

A survival analysis could be used to estimate **when** customers are most likely to attrite, not just whether they are likely to attrite. This would improve the timing of business interventions and allow the company to focus retention efforts earlier in the customer lifecycle.

### 3. A/B Testing

Future work could test different retention strategies such as onboarding improvements, targeted discounts, or customer outreach campaigns. A/B testing would make it possible to determine which actions actually reduce attrition in a measurable way.

### 4. Model Explainability

Adding feature importance analysis or SHAP values would help explain why the model predicts attrition for certain customers. This would make the results easier to communicate to stakeholders and more useful for business decision-making.

### 5. Revenue Impact Analysis

A future extension of this project could estimate the financial cost of customer attrition by measuring lost monthly revenue or projected lifetime value. This would help the business prioritize retention efforts for the highest-value customers.

### 6. Additional Data Collection

This analysis was limited to the variables available in the dataset. Future studies would be stronger with additional customer-level information such as contract type, service usage, engagement behavior, support history, and acquisition channel. These features could improve both predictive performance and business insight.
