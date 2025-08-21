import streamlit as st
import sqlite3
import pandas as pd


# -----------------------------
# Database connection functions
# -----------------------------
def get_connection():
    conn = sqlite3.connect("food_waste.db")
    return conn, conn.cursor()


# Run SQL with DataFrame output
def run_query(query, params=()):
    conn, cursor = get_connection()
    result = cursor.execute(query, params).fetchall()
    cols = [desc[0] for desc in cursor.description]
    conn.close()
    return pd.DataFrame(result, columns=cols)


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Local Food Wastage Management System", layout="wide")
st.title("🍲 Local Food Wastage Management System Dashboard")

menu = [
    "🏠 Home",
    "📂 Food Listings",
    "📞 Providers & Receivers",
    "🛠 CRUD Operations",
    "📊 SQL Insights",
    "📈 Analytics Dashboard"
]
choice = st.sidebar.selectbox("Menu", menu)

# -----------------------------
# 1. Home Section
# -----------------------------
if choice == "🏠 Home":
    st.markdown("""
        Welcome to the **Local Food Wastage Management System**.
        - Browse available food items (For food donations)
        - Contact providers & receivers  
        - Manage food listings (CRUD)  
        - Explore insights from SQL-powered analysis  
    """)

# -----------------------------
# 2. Food Listings with Filters
# -----------------------------
elif choice == "📂 Food Listings":
    st.subheader("📂 Available Food Listings")

    city = st.text_input("Filter by City")
    provider_type = st.selectbox("Filter by Provider Type", ["", "Restaurant", "Grocery Store", "Supermarket", "Catering Service"])
    food_type = st.selectbox("Filter by Food Type", ["", "Vegetarian", "Non-Vegetarian", "Vegan"])
    meal_type = st.selectbox("Filter by Meal Type", ["", "Breakfast", "Lunch", "Dinner", "Snacks"])

    query = "SELECT * FROM Food_Listings WHERE 1=1"
    params = []

    if city:
        query += " AND Location=?"
        params.append(city)
    if provider_type:
        query += " AND Provider_Type=?"
        params.append(provider_type)
    if food_type:
        query += " AND Food_Type=?"
        params.append(food_type)
    if meal_type:
        query += " AND Meal_Type=?"
        params.append(meal_type)

    df = run_query(query, params)
    st.dataframe(df)

# -----------------------------
# 3. Providers & Receivers Directory
# -----------------------------
elif choice == "📞 Providers & Receivers":
    st.subheader("📞 Contact Providers & Receivers")

    tab1, tab2 = st.tabs(["Providers", "Receivers"])

    with tab1:
        provider_id = st.number_input("Filter by Provider ID")
        provider_name = st.text_input("Filter by Provider Name")

        query_providers = "SELECT * FROM Providers WHERE 1=1"
        params = []

        if provider_id:
            query_providers += " AND Provider_ID=?"
            params.append(provider_id)
        if provider_name:
            query_providers += " AND Name=?"
            params.append(provider_name)

        df = run_query(query_providers, params)
        st.dataframe(df)

    with tab2:
        receiver_id = st.number_input("Filter by Receiver ID")
        receiver_name = st.text_input("Filter by Receiver Name")

        query_receivers = "SELECT * FROM Receivers WHERE 1=1"
        params = []

        if receiver_id:
            query_receivers += " AND Receiver_ID=?"
            params.append(receiver_id)
        if receiver_name:
            query_receivers += " AND Name=?"
            params.append(receiver_name)

        df = run_query(query_receivers, params)
        st.dataframe(df)

# -----------------------------
# 4. CRUD Operations
# -----------------------------
elif choice == "🛠 CRUD Operations":
    st.subheader("🛠 Manage Records")

    crud_choice = st.selectbox("Choose Operation", ["Add Provider", "Add Receiver", "Add Food Listing", "Update Food Listing", "Delete Food Listing"])

    conn, cursor = get_connection()

    if crud_choice == "Add Provider":
        name = st.text_input("Provider Name")
        ptype = st.text_input("Provider Type")
        address = st.text_area("Address")
        city = st.text_input("City")
        contact = st.text_input("Contact")
        if st.button("Add Provider"):
            cursor.execute("INSERT INTO Providers (Name, Type, Address, City, Contact) VALUES (?,?,?,?,?)",
                           (name, ptype, address, city, contact))
            conn.commit()
            st.success("✅ Provider added successfully")

    if crud_choice == "Add Receiver":
        name = st.text_input("Receiver Name")
        rtype = st.text_input("Receiver Type")
        city = st.text_input("City")
        contact = st.text_input("Contact")
        if st.button("Add Receiver"):
            cursor.execute("INSERT INTO Receivers (Name, Type, City, Contact) VALUES (?,?,?,?)",
                           (name, rtype, city, contact))
            conn.commit()
            st.success("✅ Receiver added successfully")

    if crud_choice == "Add Food Listing":
        food_name = st.text_input("Food Name")
        qty = st.number_input("Quantity", min_value=1)
        expiry = st.date_input("Expiry Date")
        provider_id = st.number_input("Provider ID")
        provider_type = st.text_input("Provider Type")
        location = st.text_input("Location")
        food_type = st.text_input("Food Type")
        meal_type = st.text_input("Meal Type")
        if st.button("Add Listing"):
            cursor.execute("INSERT INTO Food_Listings (Food_Name, Quantity, Expiry_Date, Provider_ID, Provider_Type, Location, Food_Type, Meal_Type) VALUES (?,?,?,?,?,?,?,?)",
                           (food_name, qty, expiry, provider_id, provider_type, location, food_type, meal_type))
            conn.commit()
            st.success("✅ Food listing added successfully")

    if crud_choice == "Update Food Listing":
        fid = st.number_input("Enter Food ID")
        new_qty = st.number_input("New Quantity", min_value=1)
        if st.button("Update"):
            cursor.execute("UPDATE Food_Listings SET Quantity=? WHERE Food_ID=?", (new_qty, fid))
            conn.commit()
            st.success("✅ Food listing updated successfully")

    if crud_choice == "Delete Food Listing":
        fid = st.number_input("Enter Food ID to delete")
        if st.button("Delete"):
            cursor.execute("DELETE FROM Food_Listings WHERE Food_ID=?", (fid,))
            conn.commit()
            st.success("🗑 Food listing deleted")

    conn.close()

# -----------------------------
# 5. SQL Insights (All 15 Queries)
# -----------------------------
elif choice == "📊 SQL Insights (15 Queries)":
    st.subheader("📊 SQL Insights (15 Key Queries)")

    queries = {
        "1. How many food providers and receivers are there in each city?": """
            SELECT City, 'Provider' AS Type, COUNT(*) AS Count FROM Providers GROUP BY City
            UNION ALL
            SELECT City, 'Receiver' AS Type, COUNT(*) AS Count FROM Receivers GROUP BY City
            ORDER BY City, Type;
        """,
        "2. Which type of food provider (restaurant, grocery store, etc.) contributes the most food?": """
            SELECT p.Type AS Provider_Type, SUM(f.Quantity) AS Total_Quantity
            FROM Food_Listings f JOIN Providers p ON f.Provider_ID = p.Provider_ID
            GROUP BY p.Type ORDER BY Total_Quantity DESC LIMIT 1;
        """,
        "3. What is the contact information of food providers in a specific city?": """
            SELECT Name, Type, Address, Contact FROM Providers WHERE City='Chennai';
        """,
        "4. Which receivers have claimed the most food?": """
            SELECT r.Name AS Receiver_Name, COUNT(c.Claim_ID) AS Total_Claims
            FROM Claims c JOIN Receivers r ON c.Receiver_ID = r.Receiver_ID
            GROUP BY r.Receiver_ID, r.Name
            ORDER BY Total_Claims DESC LIMIT 1;
        """,
        "5.	What is the total quantity of food available from all providers?": """ 
            SELECT SUM(Quantity) AS Total_Food_Quantity FROM Food_Listings;
        """,
        "6.	Which city has the highest number of food listings?": """ 
            SELECT Location AS City, COUNT(Food_ID) AS Total_Listings
            FROM Food_Listings GROUP BY Location
            ORDER BY Total_Listings DESC LIMIT 1;
        """,
        "7.	What are the most commonly available food types?": """ 
            SELECT Food_Type, COUNT(Food_ID) AS Count_Available
            FROM Food_Listings GROUP BY Food_Type
            ORDER BY Count_Available DESC;
        """,
        "8. How many food claims have been made for each food item?": """ 
            SELECT f.Food_Name, COUNT(c.Claim_ID) AS Total_Claims
            FROM Claims c JOIN Food_Listings f ON c.Food_ID = f.Food_ID
            GROUP BY f.Food_Name ORDER BY Total_Claims DESC;
        """,
        "9. Which provider has had the highest number of successful food claims?": """ 
            SELECT p.Name AS Provider_Name, COUNT(c.Claim_ID) AS Successful_Claims
            FROM Claims c JOIN Food_Listings f ON c.Food_ID = f.Food_ID
            JOIN Providers p ON f.Provider_ID = p.Provider_ID WHERE c.Status = 'Completed'
            GROUP BY p.Provider_ID, p.Name ORDER BY Successful_Claims DESC LIMIT 10;
        """,
        "10. What percentage of food claims are completed vs. pending vs. canceled?": """ 
            SELECT Status, COUNT(*) AS Claim_Count, ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Claims), 2) AS Percentage
            FROM Claims GROUP BY Status;
        """,
        "11. What is the average quantity of food claimed per receiver?": """ 
            SELECT r.Name AS Receiver_Name, ROUND(AVG(f.Quantity), 2) AS Avg_Quantity_Claimed
            FROM Claims c JOIN Food_Listings f ON c.Food_ID = f.Food_ID
            JOIN Receivers r ON c.Receiver_ID = r.Receiver_ID GROUP BY r.Receiver_ID, r.Name
            ORDER BY Avg_Quantity_Claimed DESC;
        """,
        "12. Which meal type (breakfast, lunch, dinner, snacks) is claimed the most?": """ 
            SELECT f.Meal_Type, COUNT(c.Claim_ID) AS Total_Claims
            FROM Claims c JOIN Food_Listings f ON c.Food_ID = f.Food_ID
            GROUP BY f.Meal_Type ORDER BY Total_Claims DESC;
        """,
        "13. What is the total quantity of food donated by each provider?": """ 
            SELECT p.Name AS Provider_Name, SUM(f.Quantity) AS Total_Donated
            FROM Food_Listings f JOIN Providers p ON f.Provider_ID = p.Provider_ID
            GROUP BY p.Provider_ID, p.Name ORDER BY Total_Donated DESC;
        """,
        "14. Which receiver type (NGO, Shelter, Family) benefits the most from claims?": """ 
            SELECT r.Type AS Receiver_Type, COUNT(c.Claim_ID) AS Total_Claims
            FROM Claims c JOIN Receivers r ON c.Receiver_ID = r.Receiver_ID
            WHERE c.Status = 'Completed' GROUP BY r.Type ORDER BY Total_Claims DESC;
        """,
        "15. Which food type contributes most to food wastage (unclaimed items)?": """ 
            SELECT f.Food_Type, COUNT(f.Food_ID) AS Unclaimed_Listings
            FROM Food_Listings f LEFT JOIN Claims c ON f.Food_ID = c.Food_ID
            WHERE c.Claim_ID IS NULL GROUP BY f.Food_Type ORDER BY Unclaimed_Listings DESC;
        """,
        # 📝 Continue adding all 15 queries here with your existing SQL
    }

    query_choice = st.selectbox("Select Query", list(queries.keys()))
    if query_choice == "3. What is the contact information of food providers in a specific city?":
        city = st.text_input("Enter City")
        queries[query_choice] = queries[query_choice].replace("Chennai", city)
        df = run_query(queries[query_choice])
    else:
        df = run_query(queries[query_choice])
    
    st.dataframe(df)
    st.bar_chart(df.set_index(df.columns[0]))

# -----------------------------
# 6. Analytics Dashboard
# -----------------------------
elif choice == "📈 Analytics Dashboard":
    st.subheader("📈 Data Insights & Trends")

    # Example: Claim Status distribution
    st.subheader("Claim Status Distribution")
    df = run_query("""
        SELECT Status, COUNT(*) AS Count
        FROM Claims GROUP BY Status
    """)
    st.bar_chart(df.set_index("Status"))
    
    # Food Type wastage
    st.subheader("Food Type Wastage")
    df2 = run_query("""
        SELECT f.Food_Type, COUNT(f.Food_ID) AS Unclaimed_Listings
        FROM Food_Listings f
        LEFT JOIN Claims c ON f.Food_ID = c.Food_ID
        WHERE c.Claim_ID IS NULL
        GROUP BY f.Food_Type;
    """)
    st.bar_chart(df2.set_index("Food_Type"))
