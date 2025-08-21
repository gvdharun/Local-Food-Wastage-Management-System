# 🍲 Local Food Wastage Management System

## 📌 Project Overview
Food wastage is a major challenge in society, while many people still struggle with hunger.  
The **Local Food Wastage Management System** connects **food providers** (restaurants, households, supermarkets) with **receivers** (NGOs, charities, shelters, and individuals in need).  

This system enables:
- 📂 Providers to **list surplus food**  
- 📞 Receivers/NGOs to **claim available food**  
- 📊 Admins to **analyze and reduce food wastage with insights and dashboards**  

---

## 🎯 Skills & Tech Used
- **Python** 🐍  
- **Streamlit** (Interactive Web App)  
- **SQLite3** (Database)  
- **Pandas** (Data Analysis)  
- **SQL Queries** (Insights & Reporting)  
- **Matplotlib / Seaborn** (Analytics Visualization)  

---

## ⚙️ Features

### 👤 Providers
- Add food listings (name, type, quantity, expiry date).
- Update or delete their listings.
- Provide contact details for quick communication.

### 🏠 Receivers
- Browse and search available food listings (filters by city, food type, meal type).
- Request/claim food.

### 🛠 Admin
- Manage providers, receivers, and food listings (CRUD operations).
- Monitor claim statuses (completed, pending, canceled).
- View SQL-based insights (15+ queries).
- Analyze wastage trends via the analytics dashboard.

---

## 📊 SQL Insights (15+ Key Queries)

- Food Providers & Receivers
1.	How many food providers and receivers are there in each city?
2.	Which type of food provider (restaurant, grocery store, etc.) contributes the most food?
3.	What is the contact information of food providers in a specific city?
4.	Which receivers have claimed the most food?

- Food Listings & Availability
5.	What is the total quantity of food available from all providers?
6.	Which city has the highest number of food listings?
7.	What are the most commonly available food types?

- Claims & Distribution
8. How many food claims have been made for each food item?
9. Which provider has had the highest number of successful food claims?
10. What percentage of food claims are completed vs. pending, vs. canceled?

- Analysis & Insights
11. What is the average quantity of food claimed per receiver?
12. Which meal type (breakfast, lunch, dinner, snacks) is claimed the most?
13.	What is the total quantity of food donated by each provider?
14. Which receiver type (NGO, Shelter, Family) benefits the most from claims?
15. Which food type contributes most to food wastage (unclaimed items)?

---

## 🚀 Deployment

### Option 1: **Local Setup**
1. Clone this repo:

    git clone `https://github.com/gvdharun/Local-Food-Wastage-Management-System.git`

    cd Local-Food-Wastage-Management-System

2. Install dependencies:
   
    pip install `pandas sqlite3 streamlit`

3. Run the application:

    streamlit run `food_app.py`

4. Streamlit Cloud:
- Push repository to **GitHub**  
- Deploy directly on **[Streamlit Community Cloud](https://streamlit.io/cloud/)**  
- Share the **public web-app link** with NGOs/providers.  
https://local-food-wastage-management-system-eszqfn3tmhmwq5nfap3zcr.streamlit.app/

---

## 📂 Repository Structure
```
📦 Local-Food-Wastage-Management-System
┣ 📂 data                                  # Dataset
┣ 📜 food_app.py                           # Main Streamlit application
┣ 📜 food_waste.db                         # SQLite database
┣ 📜 README.md                             # Project documentation
┗ 📂 food_waste_management.ipynb           # Jupyter notebooks for EDA & analysis
```

---

## 📈 Example Analytics
- Claim Status Distribution (Completed vs Pending vs Canceled)  
- Food Type Wastage Analysis (Unclaimed items)  
- Top 10 Providers by Total Donations  
- Most Popular Meal Type  

---

## ✨ Project Impact
- Reduces **food wastage** at local level.  
- Creates a **bridge between donors and NGOs/receivers**.  
- Provides **data-driven decision making** to monitor supply-demand mismatches.  
- Aims at **social good** 💚 by fighting hunger with technology.  

---

## 🏁 Conclusion

The **Local Food Wastage Management System** is a step towards solving two critical problems simultaneously:  
- ✅ **Reducing food wastage** from restaurants, supermarkets, and households.  
- ✅ **Addressing hunger** by connecting surplus food providers with NGOs, shelters, charities, and individuals in need.  

By combining **Python, SQL, and Streamlit**, this system not only acts as a **functional donation platform**, but also provides **data-driven insights** into food distribution patterns, most active providers/receivers, and areas where food wastage is highest.  

With real-time dashboards, SQL-powered analytics, and a user-friendly Streamlit interface, this project demonstrates how **technology can be leveraged for social good**.  

✨ Ultimately, this project showcases the potential of **data analysis and application development** in creating **impactful social solutions** while providing hands-on experience in **Python, SQL, Streamlit, and visualization tools**.  

---
