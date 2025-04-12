# 🛍️ Customer Segmentation Using Clustering
This project focuses on segmenting mall customers using clustering algorithms like K-Means. It helps businesses understand different groups of customers based on their demographics and spending behavior to make data-driven decisions.

---

## 📊 Objective
To group customers into meaningful segments based on:
- Age
- Gender
- Annual Income
- Spending Score

This helps in targeting customers with personalized marketing strategies.

---

## 📁 Dataset
We used the **Mall Customer Segmentation Dataset** which includes the following features:
- `CustomerID`
- `Gender`
- `Age`
- `Annual Income (k$)`
- `Spending Score (1-100)`
---

## 🧪 Steps Performed
1. **Data Loading and Extraction**
   - Uploaded and extracted the ZIP file containing the dataset.
2. **Exploratory Data Analysis (EDA)**
   - Explored distributions and relationships using visualizations.
3. **Clustering**
   - Applied K-Means Clustering.
   - Found optimal number of clusters using the Elbow Method.
4. **Segment Interpretation**
   - Grouped customer data by cluster and analyzed behavioral traits.
5. **Streamlit App**
   - Built an interactive dashboard using Streamlit to visualize customer segments.
---

## 🧠 Key Insights
- Clusters identified customers with high income and high spending as premium customers.
- Low-income, high-spending groups can be risky but interesting.
- Age and income show strong patterns in customer behavior.
- Visual segmentation helped businesses target customers effectively.
---

## Clone the Repository
```bash
git clone https://github.com/Khansa05/customer-segmentation.git
cd customer-segmentation
pip install -r requirements.txt
streamlit run app.py
---
## Streamlit App Access
The Streamlit app is protected with a password for security reasons.

🔑 **Password**: `35.236.135.9`  
🌐 **Access the app via LocalTunnel**: [Click here](https://six-wings-repeat.loca.lt/)
