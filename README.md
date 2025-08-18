# 🍲 Local Food Wastage Management System

## 📌 Overview

Food wastage is a global challenge, where surplus food often goes to waste while millions of people face hunger and food insecurity. This project tackles the issue by building a **Local Food Wastage Management System** using **Python, SQL, and Streamlit**.

The system allows:

* **Providers** (restaurants, grocery stores, individuals) to list surplus food.
* **Receivers** (NGOs, community centers, individuals) to claim the food.
* **Admins** to manage providers, receivers, food listings, and claims using CRUD operations.
* **Data analysis** via SQL queries and EDA to uncover wastage patterns and improve efficiency.

This project demonstrates the integration of **data engineering, analysis, and app development** to create a solution for **waste reduction** and **social good**.

---

## 🛠️ Skills Learned

* Python programming
* SQL database design & querying
* CRUD operations implementation
* Data cleaning and preparation
* Exploratory Data Analysis (EDA)
* Streamlit app development
* Dashboard & visualization

---

## 🌍 Domain

* **Food Management**
* **Waste Reduction**
* **Social Good / Community Welfare**

---

## 🚨 Problem Statement

Food wastage is widespread. Restaurants and households discard edible surplus food daily, while many individuals and NGOs struggle to access sufficient food.
This project develops a **centralized system** to:

* Connect **food providers** with **receivers**.
* Reduce waste by redistributing surplus food efficiently.
* Provide **analytics & insights** into wastage trends.

---

## 💡 Business Use Cases

* Efficient redistribution of surplus food.
* Transparency and accountability in donations.
* Insights into trends for **policy-making** and **donation drives**.
* Support for **NGOs and communities** to access food easily.

---
## Live Web App 
[Click here to view the app](https://local-food-waste-management-app.streamlit.app/)


---
## How to run locally

```bash
# 1) Install all dependancies
pip install -r requirements.txt
# 2) Initialize DB and load CSVs (put your 4 CSVs under data/ with the exact names)
python data/database/load_data.py
# 3) Launch Streamlit
pythom -m streamlit run streamlit_app/app.py
```

### File structure

<img width="454" height="802" alt="image" src="https://github.com/user-attachments/assets/9948e596-0b81-484e-ab4e-1ba790518a4f" />


### Notes
- Uses **SQLite** (`food.db`) for simplicity. Switch to PostgreSQL/MySQL by replacing the connection helpers.
- Ensure your CSV headers match the dataset description.

---

## 🔎 Approach

### 1. **Data Preparation**

* Collected CSV datasets for **providers, receivers, food listings, and claims**.
* Cleaned and formatted data for consistency.

### 2. **Database Creation**

* Designed SQL schema for 4 key entities:

  * Providers
  * Receivers
  * Food Listings
  * Claims
* Populated data into SQL tables.

### 3. **Data Analysis**

* Wrote **15 SQL queries** to answer key business questions.
* Performed **EDA** to visualize provider types, food types, and wastage trends.

### 4. **Application Development (Streamlit)**

* Developed an **interactive dashboard**:

  * Filter available food by **city, provider type, food type, and meal type**.
  * Show contact details for providers.
  * CRUD operations for managing data.
  * SQL query outputs with insights.

### 5. **Deployment**

* Streamlit app deployed for real-time interaction and accessibility.

---

## 🏗️ Data Flow & Architecture

**Data Storage** → SQL Database (Providers, Receivers, Food Listings, Claims)
**Processing Pipeline** → SQL Queries + Python Analysis
**Application Layer** → Streamlit UI for CRUD + Filtering + Visualization

---

## 📂 Dataset Details

### 1. Providers Dataset (`providers.csv`)

| Column       | Description                                     |
| ------------ | ----------------------------------------------- |
| Provider\_ID | Unique ID                                       |
| Name         | Provider name (e.g., restaurant, grocery store) |
| Type         | Provider type                                   |
| Address      | Provider address                                |
| City         | City of provider                                |
| Contact      | Contact info                                    |

### 2. Receivers Dataset (`receivers.csv`)

| Column       | Description                     |
| ------------ | ------------------------------- |
| Receiver\_ID | Unique ID                       |
| Name         | Receiver name (NGO, individual) |
| Type         | Receiver category               |
| City         | Receiver’s city                 |
| Contact      | Contact info                    |

### 3. Food Listings Dataset (`food_listings.csv`)

| Column         | Description                |
| -------------- | -------------------------- |
| Food\_ID       | Unique ID                  |
| Food\_Name     | Food item                  |
| Quantity       | Available quantity         |
| Expiry\_Date   | Expiry date                |
| Provider\_ID   | Linked provider            |
| Provider\_Type | Provider type              |
| Location       | City                       |
| Food\_Type     | Vegetarian, Non-Veg, Vegan |
| Meal\_Type     | Breakfast, Lunch, Dinner   |

### 4. Claims Dataset (`claims.csv`)

| Column       | Description                     |
| ------------ | ------------------------------- |
| Claim\_ID    | Unique ID                       |
| Food\_ID     | Linked food item                |
| Receiver\_ID | Linked receiver                 |
| Status       | Pending / Completed / Cancelled |
| Timestamp    | Claim date & time               |

---

## ❓ Key SQL Queries & Insights

1. Providers & receivers by city
2. Top provider types contributing food
3. Provider contact details by city
4. Most active receivers
5. Total food quantity available
6. Cities with most food listings
7. Most common food types
8. Claims per food item
9. Providers with most successful claims
10. Claim status distribution
11. Avg quantity claimed per receiver
12. Most claimed meal types
13. Total food donated by each provider
14. Expiry trends of food items
15. Top locations with high wastage

---

## 📊 Results

✅ **Functional Streamlit App**

* Filtering & searching of food listings
* CRUD operations for providers, receivers, food, and claims
* Visualization of SQL query results

✅ **SQL-powered Analytics**

* Provider trends
* Receiver activity
* Claim success ratios
* Food wastage insights

---

## 📏 Evaluation Metrics

* Completeness of SQL database
* Accuracy of SQL queries
* Functionality of CRUD operations
* User-friendliness of Streamlit app
* Clarity of EDA visualizations

---

## 🧰 Tech Stack

* **Python** (data handling, analysis)
* **SQL** (database & queries)
* **Streamlit** (app interface)
* **Pandas / Matplotlib** (EDA & visualization)

---

## 🚀 Deliverables

* Cleaned datasets (CSV)
* SQL database schema + 15 queries
* Streamlit app with:

  * EDA Dashboard
  * CRUD Operations
  * SQL Query Results Viewer
* Documentation (README, schema, insights)

---

## 📌 Technical Tags

`Python` `SQL` `Streamlit` `Data Analysis` `Food Management` `Waste Reduction` `Social Good`