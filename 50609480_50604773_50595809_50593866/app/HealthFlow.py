import streamlit as st
import pandas as pd
import mysql.connector
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import plotly.express as px
import base64
import plotly.graph_objects as go


# Set Streamlit page configuration
st.set_page_config(
    page_title="🌟 Insights on Health and Well-Being 🌟",
    layout="wide",
)

# Custom CSS to hide Streamlit menu and footer, and adjust padding to remove white bar
st.markdown(
    """
    <style>
    /* Hide the Streamlit header, footer, and menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

with open("/Users/sharanya/Downloads/DIC.jpg", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode()

# Streamlit app with a custom background
st.markdown(
    f"""
    <style>
    /* Apply a background image to the entire app */
    .stApp {{
        background-image: url("data:image/jpeg;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    /* Optional Styling for Sidebar and Content */
    .stSidebar {{
        background-color: rgba(255, 255, 255, 0.8); /* Transparent white */
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}
    .stSidebar h1, .stSidebar h2, .stSidebar h3 {{
        color: #34495E;
    }}

    h1, h2, h3 {{
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

#For Black Fonts
st.markdown(
    """
    <style>
    /* Set all text fonts to black */
    h1, h2, h3, h4, h5, h6, p, li, span, div, a {
        color: black !important; /* Override all text colors to black */
    }

    /* Optional: Add a shadow for better readability */
    h1, h2, h3, h4, h5, h6, p {
        text-shadow: none !important; /* Remove any existing shadows */
    }

    /* Sidebar styling for black font */
    .stSidebar, .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar p, .stSidebar li {
        color: black !important; /* Black fonts in sidebar */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Database connection function
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dharmaraju98",  # Replace with your password
            database="HealthFlow"   # Replace with your database name
        )
        return connection
    except mysql.connector.Error as e:
        st.error(f"Database connection failed: {e}")
        return None


# Function to fetch data from the database
def fetch_data(query):
    try:
        connection = create_connection()
        if not connection:
            return pd.DataFrame()  # Return empty DataFrame if connection fails
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        data = cursor.fetchall()
        connection.close()

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Clean rows where Region_Name starts with "
        if 'Region_Name' in df.columns:
            df = df[~df['Region_Name'].str.startswith('"')]

        return df
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()

# Function to execute write queries (INSERT, UPDATE, DELETE)
def execute_query(query, params=None):
    try:
        connection = create_connection()
        if not connection:
            return
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()
    except Exception as e:
        st.error(f"Error executing query: {e}")

# Map column names to user-friendly titles
column_mapping = {
    "Physicians_per_1000_people": "Physicians Per 1000 People",
    "Nurses_and_midwives_per_1000_people": "Nurses and Midwives Per 1000 People",
    "Maternal_mortality_ratio": "Maternal Mortality Ratio - Modeled Estimate",
    "Maternal_mortality_ratio_1": "Maternal Mortality Ratio - National Estimate",
    "Number_of_maternal_deaths": "Number of Maternal Deaths",
}

# Fetch unique values dynamically for dropdowns
def get_unique_values(column_name, table_name="LifeBegins"):
    query = f"SELECT DISTINCT {column_name} FROM {table_name}"
    data = fetch_data(query)
    if column_name in data.columns:
        column = data[column_name].dropna()
        if column_name == "Year_num":
            return column.sort_values().tolist()  # Skip string operations for numeric columns
        return column.astype(str).str.strip().sort_values().tolist()
    return []


# Sidebar content for Table tab only
def render_table_sidebar():
    st.markdown(
        """
        <style>
        /* Adjust the width of the sidebar */
        [data-testid="stSidebar"] {
            width: 200px; /* Set the width of the sidebar */
            min-width: 200px; /* Set the minimum width */
        }

        /* Adjust the font size of the sidebar for a more compact appearance */
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] h4, 
        [data-testid="stSidebar"] h5, 
        [data-testid="stSidebar"] h6, 
        [data-testid="stSidebar"] p, 
        [data-testid="stSidebar"] li, 
        [data-testid="stSidebar"] select {
            font-size: 14px !important; /* Reduce font size */
        }

        /* Optional: Adjust padding inside the sidebar */
        [data-testid="stSidebar"] .block-container {
            padding: 10px; /* Compact padding */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.sidebar.header("Filters")

    # Dynamically populate the Year filter
    def clean_and_sort_years(year_list):
        """Remove invalid years and sort the list."""
        valid_years = [year for year in year_list if year > 0]  # Remove invalid years like 0
        return sorted(valid_years)

    year_options = ["All"] + [str(year) for year in clean_and_sort_years(get_unique_values("Year_num"))]
    year_filter = st.sidebar.selectbox("📅 Select Year", options=year_options)


    # Dynamically populate the Region filter with cleaned and sorted data
    def clean_and_sort_regions(region_list):
        """Clean region names by removing quotes, normalizing case, and sorting alphabetically."""
        cleaned_regions = []
        for region in region_list:
            # Remove quotes, normalize case, and clean prefixes
            cleaned_region = region.replace('"', '').strip()  # Remove quotes
            cleaned_region = cleaned_region.title()  # Normalize to title case
            if ", The" in cleaned_region:
                cleaned_region = "The " + cleaned_region.replace(", The", "")  # Fix "Bahamas, The"
            cleaned_regions.append(cleaned_region)
        return sorted(cleaned_regions)  # Alphabetical sorting

    region_options = ["All"] + clean_and_sort_regions(get_unique_values("Region_Name"))
    region_filter = st.sidebar.selectbox("🌎 Select Region", options=region_options)

    st.sidebar.markdown(
    "⚠️ **Note:** CRUD operations will only work if you select 'All' from the 'Filter by Category' tab."
    )

    st.sidebar.header("Filter by Category")
    category_filter = st.sidebar.selectbox(
        "📂 Select Data Category",
        options=["All", "Health Resources", "Maternal Data", "Infant Health"],
    )

    st.sidebar.header("CRUD Operations")
    operation = st.sidebar.selectbox(
        "⚙️ Select Operation",
        options=["Lookup", "Add Entry", "Modify Entry", "Remove Entry"],
    )

    return year_filter, region_filter, category_filter, operation
    
# Initialize session state for tab selection
if "selected_tab" not in st.session_state:
    st.session_state["selected_tab"] = "Home"

st.markdown(
    """
    <style>
    /* General adjustments for container padding */
    .block-container {
        padding-top: 0rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    header, footer {visibility: hidden;} /* Hide Streamlit header/footer */

    /* Modern Button Styling */
    div.stButton > button {
        background: #f5f5f5; 
        border: 1 px solid #e0e0e0
        color: #333; /* Dark gray text for readability */
        font-size: 15px; /* Balanced font size */
        font-weight: 600; /* Semi-bold for modern text */
        padding: 8px 16px; /* Larger padding for spacious buttons */
        cursor: pointer; /* Pointer for interactivity */
        transition: all 0.2s ease-in-out; /* Smooth transitions */
    }

    /* Hover Effect */
    div.stButton > button:hover {
        background: #e0e0e0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transform: translateY(-1px); /* Lift effect */
    }

    /* Active (Pressed) Effect */
    div.stButton > button:active {
        background: #d6d6d6;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
        transform: translateY(0px); /* Reset lift on press */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Render the navigation bar using Streamlit buttons
col1, col2, col3, empty_col1 = st.columns([1, 1, 1, 11])  # Empty column pushes buttons to the right

# Add buttons to the right-aligned columns
with col1:
    if st.button("Home"):
        st.session_state["selected_tab"] = "Home"

with col2:
    if st.button("Table"):
        st.session_state["selected_tab"] = "Table"

with col3:
    if st.button("Model"):
        st.session_state["selected_tab"] = "Model"


# Update the selected tab based on session state
selected_tab = st.session_state["selected_tab"]

# Render Tabs
# Home Tab Content
if selected_tab == "Home":
    st.markdown(
        """
        <style>
        /* Adjust font sizes for headings */
        h1 {
            font-size: 48px !important; /* Increase h1 size */
        }
        h2 {
            font-size: 36px !important; /* Increase h2 size */
        }
        h3 {
            font-size: 28px !important; /* Increase h3 size */
        }
        p {
            font-size: 18px !important; /* Increase paragraph size */
            line-height: 1.6; /* Improve readability with increased line height */
        }
        li {
            font-size: 18px !important; /* Increase list item size */
        }

        /* Optional: Adjust spacing for sections */
        .stMarkdown {
            margin-top: 20px;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.header("🌟 Empowering Health Insights: Understanding Maternal and Infant Well-being 🌟")
    
    st.markdown("""
    ### Objective
    *The application empowers users to derive insights from healthcare data, run predictive analyses, and contribute new data entries. By integrating machine learning and user-friendly visualizations, the platform supports healthcare organizations, policymakers, and researchers in addressing critical maternal and infant health challenges globally. The interactive design ensures accessibility and engagement for users with varying levels of technical expertise.*
    """)
    
    st.markdown("""
    ### Driving Insights and Impact
    Our goal is to provide actionable insights that drive meaningful discussions and policies for maternal and infant health improvements. Here's what we offer:
    - **📊 Data-Driven Insights:** Analyze trends and correlations in global health metrics.
    - **🤝 User Engagement:** Empower users to add, update, and explore data for continuous learning.
    - **🤖 Predictive Modeling:** Utilize our machine learning models to predict health outcomes based on user-provided data.
    - **🎯 Customizable Filters:** Visualize and study health data by region, year, and demographic categories.
    """)

    st.markdown("""
    ### Your Role in the Journey
    - **🔍 Explore Existing Data:** Use interactive filters to view trends and patterns.
    - **📈 Run Predictions:** Input data and get model-generated health predictions.
    - **📝 Contribute Data:** Add or modify entries to expand and refine the dataset.
    - **📊 Analyze Trends:** Discover how factors like healthcare resources, literacy, and immunization impact outcomes.
    """)

    st.markdown("""
    ### Making a Difference
    - **🌍 Policy Influence:** Equip policymakers with insights to make informed decisions.
    - **💪 Health Advocacy:** Support organizations and communities in addressing maternal and infant health challenges.
    - **📢 Global Awareness:** Highlight disparities and promote equitable healthcare access.
    """)

    st.markdown("""
    ---
    ### Understanding the Initiative : Project Overview
    **Leveraging Health Data to Predict Infant Survival and Wellbeing from Pregnancy to Early Childhood**

    This project is designed to bridge the gap between available data and actionable insights, ensuring better healthcare outcomes for mothers and infants. Key aspects include:

    - **Analyzing Health Data:** By leveraging global datasets, we aim to identify patterns and correlations in maternal and infant health.
    - **Predicting Health Outcomes:** Our predictive models use machine learning to forecast infant survival rates and maternal well-being metrics.
    - **Interactive Platform:** Users can explore data by regions, years, and specific health categories, making the platform user-friendly and adaptable.
    - **Advocating for Change:** The insights generated empower healthcare organizations and policymakers to take data-driven decisions, improving resource allocation and accessibility.
    
    Together, we aim to create a platform that not only informs but also inspires meaningful change in global health outcomes.
    """)

#Tables Tab
elif selected_tab == "Table":
    st.markdown(
        """
        <style>
        /* Overlay behind the content */
        .overlay {
            background: rgba(0, 0, 0, 0.5); /* Black with 50% opacity */
            padding: 20px;
            border-radius: 8px;
        }

        /* Adjust text color and shadow */
        .overlay h1, .overlay h2, .overlay p, .overlay li {
            color: white !important; /* Make text white */
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8); /* Add text shadow for clarity */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <style>
        /* Adjust font sizes for headings */
        h1 {
            font-size: 48px !important; /* Increase h1 size */
        }
        h2 {
            font-size: 36px !important; /* Increase h2 size */
        }
        h3 {
            font-size: 28px !important; /* Increase h3 size */
        }
        p {
            font-size: 18px !important; /* Increase paragraph size */
            line-height: 1.6; /* Improve readability with increased line height */
        }
        li {
            font-size: 18px !important; /* Increase list item size */
        }

        /* Optional: Adjust spacing for sections */
        .stMarkdown {
            margin-top: 20px;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.header("📋 Insights on Infant Health and Well-Being")
    st.write("We aim to provide users with a comprehensive and interactive view of healthcare data. The page allows users to filter, explore, and analyze data using various dimensions such as year, region, and data categories. The primary purpose is to enable users to identify trends and correlations in global health metrics related to maternal and infant well-being. This feature facilitates informed decision-making by presenting data in an organized and user-friendly format. The tab includes dynamic filtering options and CRUD (Create, Read, Update, Delete) operations for enhancing or refining the dataset. Users can choose to filter data based on specific years or regions, as well as explore data across different health categories, such as Health Resources, Maternal Data and Infant Health. The seamless integration of filters and CRUD operations ensures that users can focus on specific areas of interest, modify data for personalized analysis, and derive actionable insights for research, policymaking, or educational purposes.")
    

    year_filter, region_filter, category_filter, operation = render_table_sidebar()

    query = "SELECT DISTINCT * FROM LifeBegins"
    data = fetch_data(query)

    # Ensure only unique rows are included
    if not data.empty:
        data = data.drop_duplicates(inplace=False)  # Create a new DataFrame without duplicates


    

    if not data.empty:
        if year_filter != "All":
            data = data[data["Year_num"] == int(year_filter)]
        if region_filter != "All":
            data = data[data["Region_Name"] == region_filter]
        category_columns = {
            "Health Resources": [
                "Births_attended_by_skilled_health_staff_percent_of_total",
                "Hospital_beds_per_1000_people",
                "Immunization_BCG_percent_of_one_year_old_children",
                "Immunization_HepB3_percent_of_one_year_old_children",
                "Immunization_Pol3_percent_of_one_year_old_children",
                "Newborns_protected_against_tetanus",
                "Nurses_and_midwives_per_1000_people",
                "Physicians_per_1000_people",
                "Pregnant_women_receiving_prenatal_care_percent",
                "Vitamin_A_supplementation_coverage_rate"
            ],
            "Maternal Data": [
                "Life_expectancy_at_birth_female_years",
                "Literacy_rate_Pregnant_Women",
                "Maternal_mortality_ratio",
                "Pregnant_women_receiving_prenatal_care_percent",
                "Prevalence_of_anemia_among_pregnant_women_percent",
                "Prevalence_of_current_tobacco_use_pregnant_women",
                "Prevalence_of_hypertension_pregnant_women"
            ],
            "Infant Health": [
                "Birth_rate_crude_per_1000_people",
                "Births_attended_by_skilled_health_staff_percent_of_total",
                "Mortality_rate_infant_per_1000_live_births",
                "Mortality_rate_neonatal_per_1000_live_births",
                "Number_of_infant_deaths",
                "Stillbirth_rate_per_1000_total_births",
                "Neonatal_Mortality_Rate_to_Birth_Rate_Ratio",
                "Vitamin_A_supplementation_coverage_rate"
            ]
        }

        if category_filter != "All":
            selected_columns = category_columns.get(category_filter, [])
            data = data[selected_columns]

        if operation == "Lookup":
            st.subheader("Lookup Data")
            st.dataframe(data)
        elif operation == "Add Entry":
            st.subheader("🆕 Add New Data Entry")
            new_data = {}
            for column in data.columns:
        
                if "int" in str(data[column].dtype):
                    value = st.text_input(f"Enter an integer value for {column}")
                    if value and not value.isdigit():
                        st.error(f"{column} must be an integer. Please enter a valid value.")
                        new_data[column] = None
                    else:
                        new_data[column] = int(value) if value else None
                elif "float" in str(data[column].dtype):
                    value = st.text_input(f"Enter a float value for {column}")
                    try:
                        new_data[column] = float(value) if value else None
                    except ValueError:
                        st.error(f"{column} must be a float. Please enter a valid value.")
                        new_data[column] = None
                else:
                    new_data[column] = st.text_input(f"Enter a value for {column}")
            if st.button("✅ Add Entry"):
        # Ensure all required fields are filled
                if None in new_data.values():
                    st.error("Please fill all fields with valid data before submitting.")
                else:
                     try:
                         query = f"INSERT INTO LifeBegins ({', '.join(new_data.keys())}) VALUES ({', '.join(['%s'] * len(new_data))})"
                         execute_query(query, tuple(new_data.values()))
                         st.success("✅ Entry added successfully!")
                     except Exception as e:
                         st.error(f"Error adding entry: {e}")

        
        elif operation == "Modify Entry":
            st.subheader("✏️ Modify Existing Entry")
            region_code = st.text_input("Enter the Region Code of the row to modify")
            year_num = st.text_input("Enter the Year_Num of the row to modify")
            if region_code and year_num:
                if not year_num:
                    st.error("year num is required")
                if not year_num.isdigit():
                    st.error("Year_Num must be an integer. Please enter a valid value.")
                elif not region_code:
                    st.error("Region Code is required. Please enter a valid value.")
                else:
                    year_num = int(year_num)
                    row_data = fetch_data(f"SELECT * FROM LifeBegins WHERE Region_Code = '{region_code}' AND Year_Num = {year_num}")
                    if row_data.empty:
                        st.warning("⚠️ No matching data found. Please verify your inputs.")
                    else:
                        updated_data = {}
                        for column in row_data.columns:
                            updated_data[column] = st.text_input(f"Update {column}", row_data[column].iloc[0])
                        if st.button("🔄 Modify Entry"):
                            try:
                                set_clause = ", ".join([f"{col} = %s" for col in updated_data.keys()])
                                query = f"UPDATE LifeBegins SET {set_clause} WHERE Region_Code = %s AND Year_Num = %s"
                                execute_query(query, tuple(updated_data.values()) + (region_code, year_num))
                                st.success("✅ Entry updated successfully!")
                            except Exception:
                                st.error(" Please try again with valid data.")

                
        elif operation == "Remove Entry":
            st.subheader("🗑️ Remove Data Entry")
            region_code = st.text_input("Enter the Region Code of the row to modify")
            year_num = st.text_input("Enter the Year_Num of the row to modify")

            if region_code and year_num:
                if not year_num:
                    st.error("enter year")
                if not year_num.isdigit():
                    st.error("Year_Num must be an integer. Please enter a valid value.")
                elif not region_code:
                    st.error("Region Code is required. Please enter a valid value.")
                else:
                    year_num = int(year_num)
                    row_data = fetch_data(f"SELECT * FROM LifeBegins WHERE Region_Code = '{region_code}' AND Year_Num = {year_num}")
                    row_data = fetch_data(f"""
                        SELECT DISTINCT * 
                        FROM LifeBegins
                        WHERE Region_Code = '{region_code}' AND Year_Num = {year_num}
                    """)

                    # Ensure only unique rows (as an additional safeguard)
                    row_data = row_data.drop_duplicates()

                    if row_data.empty:
                        st.warning("⚠️ Row not found. Please verify your inputs.")
                    else:
                        if st.button("🗑️ Remove Entry"):
                            try:
                                query = "DELETE FROM LifeBegins WHERE Region_Code = %s AND Year_Num = %s"
                                execute_query(query, (region_code, year_num))
                                st.success("✅ Entry removed successfully!")
                            except Exception:
                                st.error("An error occurred while removing the entry. Please try again.")


#Machine Learning Models Page
elif selected_tab == "Model":
    st.header("🤖 Machine Learning Models")
    
    st.write("📊 Have fun explore interactive visualizations using various Machine Learning algorithms like Logistic Regression, Polynomial Regression, Random Forest Regressor, XGBoost and many more.")

    st.markdown("""
    *Machine Learning Models : 
    The application provides several machine learning models, including Random Forest Regressor, XGBoost, Polynomial Regression, and LightGBM. These models analyze various health indicators to predict outcomes such as neonatal mortality, maternal mortality, and birth-death ratios. Users can select relevant columns for analysis, and the app trains and evaluates models using metrics like Mean Squared Error (MSE) and R-squared scores.*
    """)

    st.write(
    "Interactive visualizations are a core feature of the app, with tools like Plotly used to render 3D scatter plots, surface plots, and contour maps. These visualizations help users explore relationships between variables, such as the impact of skilled birth attendance on neonatal mortality rates. The app also explains the underlying algorithms and the significance of the generated insights."
    )

    st.markdown("""
    ### Hypotheses and Questions
    Below is a table summarizing key research questions and corresponding hypotheses for the project.
    """)

    st.markdown("""
    | S.N. | Question                                                                                                                       | Hypothesis                                                                                                  | Algorithm                          | Visualization      |
    |------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------|--------------------|
    | 1    | How do healthcare system factors, such as the number of healthcare professionals, hospital bed capacity, and literacy among healthcare workers, influence maternal and general mortality rates? | Increased healthcare professionals linked to lower maternal mortality rates.                                | Random Forest Algorithm            | 3D Scatter Plot    |
    |      |                                                                                                                               | Hospital bed capacity linked to mortality rates.                                                            | Support Vector Machine Algorithm   | 3D Scatter Plot    |
    |      |                                                                                                                               | Literacy among healthcare workers affects outcomes.                                                         | Decision Tree Algorithm            | 3D Scatter Plot    |
    | 2    | How do factors such as skilled health staff attendance during births and maternal health conditions (e.g., anemia, hypertension, or tobacco use) influence neonatal and infant mortality rates? | Regions with higher percentages of births attended by skilled health staff will have significantly lower neonatal and infant mortality rates. | Polynomial Regression Algorithm    | 3D Contour Plot    |
    |      |                                                                                                                               | Mothers with higher prevalence of anemia, hypertension, or tobacco use are more likely to experience higher rates of neonatal mortality and stillbirths. | LightGBM Algorithm                 | 3D Line Plot       |
    | 3    | How does the combination of immunization coverage (BCG, HepB3, Pol3), literacy rates, and low birthweight contribute to variations in neonatal and infant health outcomes (such as neonatal mortality and stillbirth rates) across different regions? | Higher immunization coverage (BCG, HepB3, Pol3) is associated with lower neonatal mortality and stillbirth rates in regions with higher literacy rates, suggesting that better health education and access to vaccines contribute to improved neonatal health outcomes. | XGBoost Algorithm                  | 3D Bubble Plot     |
    |      |                                                                                                                               | Regions with lower prevalence of low birthweight babies will exhibit lower neonatal mortality and stillbirth rates, indicating that maternal nutrition and healthcare interventions to prevent low birthweight play a critical role in improving infant health outcomes. |                                    |                    |
    | 4    | How do crude birth and death rates, life expectancy, and low-birthweight rates correlate with infant mortality and stillbirth rates across different regions and years? | Birth Rate Dynamics and Mortality Regions with extremely high or low crude birth rates show higher infant mortality and stillbirth rates, indicating population stress or resource constraints. | Random Forest Regressor            | 3D Surface Plot    |
    |      |                                                                                                                               | Yearly Trends: Over time, regions show a decline in infant mortality rates and neonatal mortality-to-birth rate ratios, correlating with improvements in life expectancy and a reduction in low-birthweight babies. | Random Forest Regressor            | 3D Line Plot       |
    """)

    question = st.selectbox(
        "Select Question:",
        [
            "Select a question...",
            "Question 1: Healthcare Resources",
            "Question 2: Maternal Health",
            "Question 3: Immunization Effects",
            "Question 4: Birth and Death Rates",
        ],
    )

#Question 1
    if question == "Question 1: Healthcare Resources":
        hypothesis = st.selectbox(
            "Select Hypothesis:",
            [
                "Select a hypothesis...",
                "Hypothesis 1: Increased healthcare professionals linked to lower maternal mortality rates",
                "Hypothesis 2: Hospital bed capacity linked to mortality rates",
                "Hypothesis 3: Literacy among healthcare workers affects outcomes",
            ],
        )
#Question 1 - Hypothesis 1
        if hypothesis == "Hypothesis 1: Increased healthcare professionals linked to lower maternal mortality rates":
            st.markdown("### Select Columns for Analysis")
            options = st.multiselect(
                "Choose at least 3 columns:",
                list(column_mapping.values()),
            )

            if len(options) >= 3:
                # Reverse map the column names for querying
                selected_columns = [
                    key for key, value in column_mapping.items() if value in options
                ]
                query = f"SELECT {', '.join(selected_columns)} FROM LifeBegins"
                data = fetch_data(query)

                if not data.empty:
                    # Rename columns for display
                    display_data = data.rename(columns=column_mapping)
                    st.dataframe(display_data)

                    # Preprocess data
                    X = data[selected_columns[:-1]]
                    y = data[selected_columns[-1]]

                    # Train-test split
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                    # Fit the Random Forest model
                    model = RandomForestRegressor(n_estimators=100, random_state=42)
                    model.fit(X_train, y_train)

                    # Predict and evaluate
                    y_pred = model.predict(X_test)
                    mse = mean_squared_error(y_test, y_pred)

                    # Display Mean Squared Error Explanation
                    st.markdown("### Mean Squared Error (MSE)")
                    st.write(
                        "The **Mean Squared Error (MSE)** measures the average squared difference between the actual and predicted values. "
                        "It is calculated as follows:"
                    )
                    st.latex(r"MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2")
                    st.write(
                        f"In this case, the calculated MSE is **{mse:.2f}**, which indicates the average squared error of the model's predictions."
                    )

                    # Enhanced 3D Visualization using Plotly Express
                    st.markdown("### 3D Visualization")
                    fig = px.scatter_3d(
                        data,
                        x=selected_columns[0],
                        y=selected_columns[1],
                        z=selected_columns[2],
                        color=selected_columns[2],
                        color_continuous_scale="Viridis",
                        title="3D Scatter Plot",
                        labels={
                            selected_columns[0]: column_mapping[selected_columns[0]],
                            selected_columns[1]: column_mapping[selected_columns[1]],
                            selected_columns[2]: column_mapping[selected_columns[2]],
                        },
                    )
                    fig.update_traces(marker=dict(size=8))  # Increase marker size
                    fig.update_layout(
                        scene=dict(
                            xaxis=dict(
                                title=dict(
                                    text=column_mapping[selected_columns[0]],
                                    font=dict(size=14, style="italic"),
                                ),
                                tickfont=dict(size=12),
                            ),
                            yaxis=dict(
                                title=dict(
                                    text=column_mapping[selected_columns[1]],
                                    font=dict(size=14, style="italic"),
                                ),
                                tickfont=dict(size=12),
                            ),
                            zaxis=dict(
                                title=dict(
                                    text=column_mapping[selected_columns[2]],
                                    font=dict(size=14, style="italic"),
                                ),
                                tickfont=dict(size=12),
                            ),
                        ),
                        margin=dict(l=0, r=0, b=0, t=50),  # Adjust margins for cleaner layout
                        title=dict(
                            text="3D Scatter Plot",
                            font=dict(size=18),
                            x=0.5,
                        ),
                        width=1200,  # Increased graph width
                        height=800,  # Increased graph height
                    )

                    # Display the interactive plot
                    st.plotly_chart(fig, use_container_width=False)

                    # Add Summary after Visualization
                    st.markdown("### Summary")
                    st.write(
                        "This visualization provides an interactive 3D scatter plot of healthcare data, showing the relationships between physicians, "
                        "nurses, and maternal mortality. The data highlights how increased access to healthcare professionals correlates with "
                        "lower maternal mortality rates."
                    )
                    st.write(
                        "We used the **Random Forest Regression** algorithm to model these relationships and calculate the predictive accuracy, "
                        "demonstrated through the Mean Squared Error (MSE). The visualization complements the statistical analysis, "
                        "helping us understand the key factors influencing maternal health outcomes."
                    )
#Question 1 - Hypothesis 2
        elif hypothesis == "Hypothesis 2: Hospital bed capacity linked to mortality rates":
            st.markdown("### Select Columns for Analysis")

            # Column mapping for user-friendly names
            column_mapping = {
                "Hospital_beds_per_1000_people": "Hospital Beds Per 1000 People",
                "Mortality_rate_infant_per_1000_live_births": "Infant Mortality Rate (Per 1000 Live Births)",
                "Mortality_rate_infant_male_per_1000_live_births": "Male Infant Mortality Rate (Per 1000 Live Births)",
                "Mortality_rate_infant_female_per_1000_live_births": "Female Infant Mortality Rate (Per 1000 Live Births)",
                "Mortality_rate_neonatal_per_1000_live_births": "Neonatal Mortality Rate (Per 1000 Live Births)",
                "Death_rate_crude_per_1000_people": "Crude Death Rate (Per 1000 People)",
                "Maternal_mortality_ratio": "Maternal Mortality Ratio",
                "Birth_rate_crude_per_1000_people": "Crude Birth Rate (Per 1000 People)",
                "Physicians_per_1000_people": "Physicians Per 1000 People",
                "Nurses_and_midwives_per_1000_people": "Nurses and Midwives Per 1000 People",
            }

            # Display user-friendly column names
            options = st.multiselect(
                "Choose at least 3 columns (including Hospital Beds Per 1000 People):",
                list(column_mapping.values()),  # Use mapped names
            )

            # Reverse map the user-friendly names to original column names
            selected_columns = [
                key for key, value in column_mapping.items() if value in options
            ]

            if len(selected_columns) >= 3 and "Hospital_beds_per_1000_people" in selected_columns:
                query = f"SELECT {', '.join(selected_columns)} FROM LifeBegins"
                data = fetch_data(query)

                if not data.empty:
                    # Rename columns for display
                    display_data = data.rename(columns=column_mapping)
                    st.dataframe(display_data)

                    # SVM Model Implementation
                    st.markdown("### Support Vector Machine (SVM) Algorithm")
                    st.write("The SVM algorithm is used for classification and regression tasks. The formula for the decision function in SVM is:")
                    st.latex(r"f(x) = \sum_{i=1}^{n} \alpha_i y_i K(x_i, x) + b")
                    st.write("Where `K(x_i, x)` represents the kernel function, and `\\alpha_i` are Lagrange multipliers.")

                    # Preprocess data
                    X = data[selected_columns[:-1]]
                    y = data[selected_columns[-1]]

                    from sklearn.svm import SVR
                    from sklearn.model_selection import train_test_split
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                    model = SVR(kernel='linear')
                    model.fit(X_train, y_train)

                    y_pred = model.predict(X_test)

                    # 3D Visualization
                    st.markdown("### 3D Visualization")
                    fig = px.scatter_3d(
                        data,
                        x=selected_columns[0],
                        y=selected_columns[1],
                        z=selected_columns[2],
                        color=selected_columns[1],
                        title="3D Scatter Plot of Hospital Beds and Mortality Rates",
                        labels={
                            selected_columns[0]: column_mapping[selected_columns[0]],
                            selected_columns[1]: column_mapping[selected_columns[1]],
                            selected_columns[2]: column_mapping[selected_columns[2]],
                        },
                    )
                    st.plotly_chart(fig, use_container_width=True)

                    # Summary
                    st.markdown("### Summary of the Visualization")
                    st.write(
                        "The 3D scatter plot visualizes the relationships between hospital bed capacity, mortality rates, and additional healthcare metrics. "
                        "It highlights the potential correlation between increased hospital bed availability and lower mortality rates across different categories."
                    )
                    st.write(
                        "This analysis demonstrates that hospital bed capacity plays a critical role in improving healthcare outcomes, especially in reducing infant and maternal mortality rates."
                    )
            else:
                st.error("Please select at least 3 columns, including 'Hospital Beds Per 1000 People'.")
#Question 1 - Hypothesis 3
        elif hypothesis == "Hypothesis 3: Literacy among healthcare workers affects outcomes":
            st.markdown("### Select Columns for Analysis")

            options = st.multiselect(
                "Choose all the columns:",
                [
                    "Literacy_rate_adult_total_percent_of_people_ages_15_and_above",
                    "Nurses_and_midwives_per_1000_people",
                    "Physicians_per_1000_people",
                    "Maternal_mortality_ratio",
                    "Mortality_rate_infant_per_1000_live_births",
                    "Mortality_rate_neonatal_per_1000_live_births",
                    "Life_expectancy_at_birth_female_years",
                    "Life_expectancy_at_birth_male_years",
                    "Life_expectancy_at_birth_total_years",
                ],
            )

            # Ensure the mandatory columns are selected and at least 5 columns in total
            mandatory_columns = [
                "Literacy_rate_adult_total_percent_of_people_ages_15_and_above",
                "Nurses_and_midwives_per_1000_people",
                "Physicians_per_1000_people",
            ]
            if len(options) >= 5 and all(col in options for col in mandatory_columns):
                query = f"SELECT {', '.join(options)} FROM LifeBegins"
                data = fetch_data(query)

                if not data.empty:
                    st.dataframe(data)

                    # Preprocess data
                    X = data[options[:-1]]
                    y = data[options[-1]]

                    # Train-test split
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                    # Decision Tree Algorithm
                    st.markdown("### Decision Tree Algorithm")
                    st.write("A decision tree is a flowchart-like structure used for classification and regression. The algorithm splits the dataset into smaller subsets while at the same time incrementally developing an associated decision tree.")

                    st.latex(r"f(x) = \text{argmax}k\ \frac{1}{|S|} \sum{x_i \in S} I(y_i = k)")
                    st.write("Here, k represents the possible outcomes, S is the subset of data at a node, and I is the indicator function.")

                    from sklearn.tree import DecisionTreeRegressor
                    model = DecisionTreeRegressor(random_state=42)
                    model.fit(X_train, y_train)

                    y_pred = model.predict(X_test)
                    mse = mean_squared_error(y_test, y_pred)
                    st.write(f"Mean Squared Error (MSE): {mse:.2f}")

                    # 3D Scatter Plot Visualization (as histogram cannot have 'z')
                    st.markdown("### 3D Visualization")
                    fig = px.scatter_3d(
                        data,
                        x=options[0],  # First selected column for x-axis
                        y=options[1],  # Second selected column for y-axis
                        z=options[2],  # Third selected column for z-axis
                        color=options[1],  # Color based on the second selected column
                        title="3D Scatter Plot",
                        labels={
                            options[0]: "Literacy Rate",
                            options[1]: "Healthcare Workers",
                            options[2]: "Health Outcomes",
                        }
                    )
                    fig.update_traces(marker=dict(size=5))  # Adjust marker size for better visibility
                    fig.update_layout(
                        scene=dict(
                            xaxis_title=options[0],
                            yaxis_title=options[1],
                            zaxis_title=options[2],
                        )
                    )
                    st.plotly_chart(fig, use_container_width=True)


                    # Summary
                    st.markdown("### Summary of the Visualization")
                    st.write(
                        "The 3D scatter plot visualizes the relationship between literacy rates, healthcare staffing, and outcomes such as "
                        "maternal mortality and life expectancy. The data indicates that higher literacy levels and better access to trained healthcare workers "
                        "are correlated with improved health outcomes."
                    )
                    st.write(
                        "This analysis highlights the critical role of literacy among healthcare workers in improving maternal and neonatal health metrics."
                    )
#Question 2   
    elif question == "Question 2: Maternal Health":
        hypothesis = st.selectbox(
            "Select Hypothesis:",
            [
                "Select a hypothesis...",
                "Hypothesis 1: Regions with higher percentages of births attended by skilled health staff will have significantly lower neonatal and infant mortality rates.",
                "Hypothesis 2: Mothers with higher prevalence of anemia, hypertension, or tobacco use are more likely to experience higher rates of neonatal mortality and stillbirths.",
            ],
        )
#Question 2 - Hypothesis 1
        if hypothesis == "Hypothesis 1: Regions with higher percentages of births attended by skilled health staff will have significantly lower neonatal and infant mortality rates.":
            st.markdown("### Select Relevant Columns for Analysis")
            column_mapping = {
                "Births_attended_by_skilled_health_staff_percent_of_total": "Births attended by Skilled health staff",
                "Mortality_rate_neonatal_per_1000_live_births": "Neonatal Mortality Rate (Per 1000 live births)",
                "Mortality_rate_infant_per_1000_live_births": "Infant Mortality Rate (Per 1000 live births)",
                "Region_Name": "Region Name",
                "Year_num": "Year",
            }
            
            # Display user-friendly column names
            options = st.multiselect(
                "Choose at least 4 columns (including Hospital Beds Per 1000 People):",
                list(column_mapping.values()),  # Use mapped names
            )

            # Multiselect options
            selected_columns = [
                key for key, value in column_mapping.items() if value in options
            ]

            # Ensure mandatory column is selected and at least 4 columns are chosen
            if len(selected_columns) >= 4 and "Births_attended_by_skilled_health_staff_percent_of_total" in selected_columns:
                query = f"SELECT {', '.join(selected_columns)} FROM LifeBegins"
                data = fetch_data(query)

                if not data.empty:
                    st.dataframe(data)

                    # Preprocess data
                    X = data[["Births_attended_by_skilled_health_staff_percent_of_total"]]
                    y = data["Mortality_rate_neonatal_per_1000_live_births"]

                    # Polynomial Regression
                    st.markdown("### Polynomial Regression Algorithm")
                    st.write(
                        "Polynomial regression is an extension of linear regression where the relationship between the independent variable (x) "
                        "and the dependent variable (y) is modeled as an nth-degree polynomial."
                    )
                    st.latex(r"y = \beta_0 + \beta_1x + \beta_2x^2 + ... + \beta_nx^n + \epsilon")

                    from sklearn.preprocessing import PolynomialFeatures
                    from sklearn.linear_model import LinearRegression
                    from sklearn.metrics import mean_squared_error, r2_score

                    # Transform features to polynomial features
                    poly = PolynomialFeatures(degree=2)  # Degree of the polynomial
                    X_poly = poly.fit_transform(X)

                    # Fit Polynomial Regression Model
                    model = LinearRegression()
                    model.fit(X_poly, y)

                    # Make Predictions
                    y_pred = model.predict(X_poly)

                    # Evaluate the model
                    mse = mean_squared_error(y, y_pred)
                    r2 = r2_score(y, y_pred)
                    st.write(f"Mean Squared Error (MSE): {mse:.2f}")
                    st.write(f"R-squared (R²) Score: {r2:.2f}")

                    # 3D Contour Plot Visualization
                    st.markdown("### 3D Visualization")
                    fig = px.density_contour(
                        data,
                        x="Births_attended_by_skilled_health_staff_percent_of_total",
                        y="Mortality_rate_neonatal_per_1000_live_births",
                        z="Mortality_rate_infant_per_1000_live_births",
                        title="3D Contour Plot of Skilled Birth Attendance vs Mortality Rates",
                        labels={
                            "Births_attended_by_skilled_health_staff_percent_of_total": "Skilled Birth Attendance (%)",
                            "Mortality_rate_neonatal_per_1000_live_births": "Neonatal Mortality Rate",
                            "Mortality_rate_infant_per_1000_live_births": "Infant Mortality Rate",
                        },
                    )
                    fig.update_traces(contours_coloring="fill", contours_showlines=True)
                    st.plotly_chart(fig, use_container_width=True)

                    # Summary
                    st.markdown("### Summary of the Visualization")
                    st.write(
                        "The 3D contour plot demonstrates the relationship between the percentage of births attended by skilled health staff "
                        "and neonatal and infant mortality rates. Regions with higher skilled birth attendance percentages generally show "
                        "lower neonatal and infant mortality rates."
                    )
                    st.write(
                        "This analysis underscores the critical importance of skilled birth attendance in improving neonatal and infant health outcomes."
                    )
                else:
                    st.error("No data available for the selected hypothesis.")
            else:
                st.error("Please select at least 4 columns, including 'Births Attended by Skilled Health Staff'.")
#Question 2 - Hypothesis 2       
        elif hypothesis == "Hypothesis 2: Mothers with higher prevalence of anemia, hypertension, or tobacco use are more likely to experience higher rates of neonatal mortality and stillbirths.":
 
            st.markdown("### Select Relevant Columns for Analysis")
            column_mapping = {
                "Prevalence_of_anemia_among_pregnant_women_percent": "Prevalence of Anemia Among Pregnant Women (%)",
                "Prevalence_of_hypertension_pregnant_women": "Prevalence of Hypertension Among Pregnant Women",
                "Prevalence_of_current_tobacco_use_pregnant_women": "Prevalence of Current Tobacco Use Among Pregnant Women",
                "Mortality_rate_neonatal_per_1000_live_births": "Neonatal Mortality Rate (Per 1000 Live Births)",
                "Number_of_stillbirths": "Number of Stillbirths"
            }

            # Multiselect options
            options = st.multiselect(
                "Choose at least 4 columns for analysis:",
                list(column_mapping.values()),
            )

             #Reverse map the user-friendly names to original column names
            selected_columns = [
                key for key, value in column_mapping.items() if value in options
            ]

            # Ensure at least 4 columns are chosen
            if len(selected_columns) >= 4:
                query = f"SELECT {', '.join(selected_columns)} FROM LifeBegins"
                data = fetch_data(query)

                if not data.empty:
                    st.dataframe(data)

                    # Preprocess data
                    X = data[selected_columns[:-1]]  # Exclude the last column as target
                    y = data[selected_columns[-1]]  # Use the last column as the target variable

                    # LightGBM Algorithm
                    st.markdown("### LightGBM Algorithm")
                    st.write(
                        "LightGBM (Light Gradient Boosting Machine) is a gradient boosting framework that uses tree-based learning algorithms. "
                        "It is known for its efficiency and fast training."
                    )
                    st.latex(
                        r"y = \sum_{m=1}^{M} \gamma_m T_m(x) + \epsilon"
                    )
                    st.write(
                        "Here, $T_m(x)$ represents the decision trees, $M$ is the total number of trees, "
                        "and $\\gamma_m$ represents the weight of each tree."
                    )

                    import lightgbm as lgb
                    from sklearn.model_selection import train_test_split
                    from sklearn.metrics import mean_squared_error, r2_score

                    X_train, X_test, y_train, y_test = train_test_split(
                        X, y, test_size=0.2, random_state=42
                    )

                    model = lgb.LGBMRegressor()
                    model.fit(X_train, y_train)
                    y_pred = model.predict(X_test)

                    mse = mean_squared_error(y_test, y_pred)
                    r2 = r2_score(y_test, y_pred)

                    st.write(f"Mean Squared Error (MSE): {mse:.2f}")
                    st.write(f"R-squared (R²) Score: {r2:.2f}")

                    # 3D Line Plot Visualization
                    st.markdown("### 3D Visualization")
                    fig = px.line_3d(
                        data,
                        x=selected_columns[0],  # First selected column
                        y=selected_columns[1],  # Second selected column
                        z=selected_columns[2],  # Third selected column
                        title="3D Line Plot",
                        labels={
                            selected_columns[0]: "Anemia Prevalence",
                            selected_columns[1]: "Hypertension Prevalence",
                            selected_columns[2]: "Tobacco Use Prevalence",
                        },
                    )
                    st.plotly_chart(fig, use_container_width=True)

                    # Summary
                    st.markdown("### Summary of the Visualization")
                    st.write(
                        "The 3D line plot visualizes the relationship between maternal health conditions (anemia, hypertension, and tobacco use) "
                        "and neonatal and stillbirth mortality rates. The trends show that higher prevalence of these maternal health conditions "
                        "is associated with increased neonatal mortality and stillbirths."
                    )
                    st.write(
                        "This analysis highlights the importance of managing maternal health conditions to reduce adverse birth outcomes."
                    )
                else:
                    st.error("No data available for the selected hypothesis.")
            else:
                st.error("Please select at least 4 columns for analysis.")
#Question 3
    elif question == "Question 3: Immunization Effects":
        hypothesis = st.selectbox(
            "Select Hypothesis:",
            [
                "Select a hypothesis...",
                "Hypothesis 1: Increased healthcare professionals linked to lower maternal mortality rates",
                "Hypothesis 2: Hospital bed capacity linked to mortality rates",
            ],
        )
#Question 3 - Hypothesis 1 
        if hypothesis == "Hypothesis 1: Increased healthcare professionals linked to lower maternal mortality rates":
            st.markdown("### Select Relevant Columns for Analysis")
            column_mapping = {
                "Immunization_BCG_percent_of_one_year_old_children": "BCG Immunization (% of One-Year-Old Children)",
                "Immunization_HepB3_percent_of_one_year_old_children": "HepB3 Immunization (% of One-Year-Old Children)",
                "Immunization_measles_second_dose": "Measles Immunization (Second Dose)",
                "Immunization_Pol3_percent_of_one_year_old_children": "Polio Immunization (% of One-Year-Old Children)",
                "Newborns_protected_against_tetanus": "Newborns Protected Against Tetanus",
                "Literacy_rate_Pregnant_Women": "Literacy Rate (Pregnant Women)",
                "Literacy_rate_adult_total_percent_of_people_ages_15_and_above": "Adult Literacy Rate (% of People Aged 15 and Above)",
                "Mortality_rate_neonatal_per_1000_live_births": "Neonatal Mortality Rate (Per 1000 Live Births)",
                "Number_of_neonatal_deaths": "Number of Neonatal Deaths",
                "Number_of_stillbirths": "Number of Stillbirths"
            }

            # Allow user to select 6 columns
            options = st.multiselect(
                "Ensure more than 6 columns are selected",
                list(column_mapping.values()),
            )

            # Reverse map the user-friendly names to original column names
            selected_columns = [
                key for key, value in column_mapping.items() if value in options
            ]

            # Ensure more than 6 columns are selected
            if len(selected_columns) > 6:
                query = f"SELECT {', '.join(selected_columns)} FROM LifeBegins"
                data = fetch_data(query)

                if not data.empty:
                    st.write("Preview of Selected Data:")
                    st.write(data.describe())

                    # Preprocess data
                    X = data[selected_columns[:-1]]
                    y = data[selected_columns[-1]]

                    # Implement XGBoost Algorithm
                    st.markdown("### XGBoost Algorithm")
                    st.write(
                        "XGBoost (Extreme Gradient Boosting) is an efficient and scalable implementation of gradient boosting framework."
                    )
                    st.latex(r"y = \sum_{m=1}^{M} \gamma_m T_m(x) + \epsilon")
                    st.write(
                        "Here, $T_m(x)$ represents the decision trees, $M$ is the total number of trees, "
                        "and $\\gamma_m$ represents the weight of each tree."
                    )

                    from xgboost import XGBRegressor
                    from sklearn.model_selection import train_test_split
                    from sklearn.metrics import mean_squared_error, r2_score

                    X_train, X_test, y_train, y_test = train_test_split(
                        X, y, test_size=0.2, random_state=42
                    )

                    model = XGBRegressor()
                    model.fit(X_train, y_train)
                    y_pred = model.predict(X_test)

                    mse = mean_squared_error(y_test, y_pred)
                    r2 = r2_score(y_test, y_pred)

                    st.write(f"Mean Squared Error (MSE): {mse:.2f}")
                    st.write(f"R-squared (R²) Score: {r2:.2f}")

                    # 3D Bubble Plot Visualization
                    st.markdown("### 3D Visualization")
                    import plotly.express as px

                    fig = px.scatter_3d(
                        data,
                        x=selected_columns[0],
                        y=selected_columns[1],
                        z=selected_columns[2],
                        size=selected_columns[3],
                        color=selected_columns[4],
                        title="3D Bubble Plot",
                        labels={
                            selected_columns[0]: selected_columns[0],
                            selected_columns[1]: selected_columns[1],
                            selected_columns[2]: selected_columns[2],
                        },
                    )
                    st.plotly_chart(fig, use_container_width=True)

                    # Summary
                    st.markdown("### Summary of the Visualization")
                    st.write(
                        "The 3D bubble plot visually demonstrates a relationship between immunization rates and literacy rates, with data points clustering in regions where both variables are high. This suggests a possible correlation between maternal literacy and increased immunization coverage."
                    )
                    st.write(
                        "The varying bubble sizes and color gradients highlight regions where immunization rates are most impacted by maternal literacy, making it easy to identify clusters of high or low immunization coverage."

                    )
                else:
                    st.error("No data available for the selected hypothesis.")
            else:
                st.error("Please select more than 6 columns for analysis.")
#Question 3 - Hypothesis 2 
        if hypothesis == "Hypothesis 2: Hospital bed capacity linked to mortality rates":
            st.markdown("### Select Relevant Columns for Analysis")
            column_mapping = {
                "Low_birthweight_babies_percent_of_births": "Low-Birthweight Babies (% of Births)",
                "Mortality_rate_neonatal_per_1000_live_births": "Neonatal Mortality Rate (Per 1000 Live Births)",
                "Number_of_neonatal_deaths": "Number of Neonatal Deaths",
                "Number_of_stillbirths": "Number of Stillbirths"
            }

            # Allow user to select all 4 columns
            options = st.multiselect(
                "You must select all 4 columns for analysis:",
                list(column_mapping.values()),
            )

            # Reverse map the user-friendly names to original column names
            selected_columns = [
                key for key, value in column_mapping.items() if value in options
            ]

            # Ensure exactly 4 columns are selected
            if len(selected_columns) == 4:
                query = f"SELECT {', '.join(selected_columns)} FROM LifeBegins"
                data = fetch_data(query)

                if not data.empty:
                    st.write("Preview of Selected Data:")
                    st.write(data.describe())

                    # Preprocess data
                    X = data[selected_columns[:-1]]  # All columns except the last one
                    y = data[selected_columns[-1]]  # Use the last column as the target

                    # Implement XGBoost Algorithm
                    st.markdown("### XGBoost Algorithm")
                    st.write(
                        "XGBoost (Extreme Gradient Boosting) is an efficient and scalable implementation of the gradient boosting framework. "
                        "It uses decision trees as weak learners to minimize a loss function."
                    )
                    st.latex(r"y = \sum_{m=1}^{M} \gamma_m T_m(x) + \epsilon")
                    st.write(
                        "Here, $T_m(x)$ represents the decision trees, $M$ is the total number of trees, "
                        "and $\\gamma_m$ represents the weight of each tree."
                    )

                    from xgboost import XGBRegressor
                    from sklearn.model_selection import train_test_split
                    from sklearn.metrics import mean_squared_error, r2_score

                    X_train, X_test, y_train, y_test = train_test_split(
                        X, y, test_size=0.2, random_state=42
                    )

                    model = XGBRegressor()
                    model.fit(X_train, y_train)
                    y_pred = model.predict(X_test)

                    mse = mean_squared_error(y_test, y_pred)
                    r2 = r2_score(y_test, y_pred)

                    st.write(f"Mean Squared Error (MSE): {mse:.2f}")
                    st.write(f"R-squared (R²) Score: {r2:.2f}")

                    # 3D Bar Plot Visualization (Using scatter_3d)
                    st.markdown("### 3D Visualization")
                    import plotly.express as px

                    fig = px.scatter_3d(
                        data,
                        x=selected_columns[0],
                        y=selected_columns[1],
                        z=selected_columns[2],
                        size=selected_columns[3],
                        color=selected_columns[3],
                        title="3D Bar Plot",
                        labels={
                            selected_columns[0]: selected_columns[0],
                            selected_columns[1]: selected_columns[1],
                            selected_columns[2]: selected_columns[2],
                        },
                    )
                    st.plotly_chart(fig, use_container_width=True)

                    # Summary
                    st.markdown("### Summary of the Visualization")
                    st.write(
                        "The 3D scatter plot effectively shows the relationship between low birthweight, neonatal mortality, and stillbirths, with colors representing the intensity of stillbirth rates."
                    )
                    st.write(
                        "The visualization makes it easy to spot areas with high rates of neonatal mortality and stillbirths, offering valuable insights into the impact of low birthweight on these outcomes."
                    )
                else:
                    st.error("No data available for the selected hypothesis.")
            else:
                st.error("You must select exactly 4 columns for analysis.")       
#Question 4
    elif question == "Question 4: Birth and Death Rates":
        hypothesis = st.selectbox(
        "Select Hypothesis:",
        [
            "Select a hypothesis...",
            "Hypothesis 1: Impact of immunization and literacy on neonatal health outcomes",
            "Hypothesis 2: Low birthweight's effect on neonatal mortality and stillbirths",
        ],
    )
#Question 4 - Hypothesis 1
        if hypothesis == "Hypothesis 1: Impact of immunization and literacy on neonatal health outcomes":
            st.markdown("### Select Relevant Columns for Analysis")
            column_mapping = {
                "Birth_rate_crude_per_1000_people": "Crude Birth Rate (Per 1000 People)",
                "Mortality_rate_infant_per_1000_live_births": "Infant Mortality Rate (Per 1000 Live Births)",
                "Number_of_infant_deaths": "Number of Infant Deaths",
                "Number_of_stillbirths": "Number of Stillbirths",
                "Death_rate_crude_per_1000_people": "Crude Death Rate (Per 1000 People)"
            }

            options = st.multiselect(
                "You must select all 5 columns for analysis:",
                list(column_mapping.values()),
            )

            selected_columns = [
                key for key, value in column_mapping.items() if value in options
            ]

            if len(selected_columns) == 5:
                query = f"SELECT {', '.join(selected_columns)} FROM LifeBegins"
                data = fetch_data(query)

                if not data.empty:
                    st.write("Preview of Selected Data:")
                    st.write(data.describe())

                    # Preprocess data
                    X = data[selected_columns[:-1]]  # All columns except the last one
                    y = data[selected_columns[-1]]  # Use the last column as the target

                    # RandomForestRegressor Implementation
                    st.markdown("### Random Forest Regressor Algorithm")
                    st.write(
                        "Random Forest Regressor is an ensemble learning algorithm that builds multiple decision trees "
                        "and averages their outputs to achieve better accuracy and avoid overfitting."
                    )
                    st.latex(r"f(X) = \frac{1}{N} \sum_{i=1}^{N} T_i(X)")

                    from sklearn.ensemble import RandomForestRegressor
                    from sklearn.model_selection import train_test_split
                    from sklearn.metrics import mean_squared_error, r2_score

                    X_train, X_test, y_train, y_test = train_test_split(
                        X, y, test_size=0.2, random_state=42
                    )

                    model = RandomForestRegressor(random_state=42)
                    model.fit(X_train, y_train)
                    y_pred = model.predict(X_test)

                    mse = mean_squared_error(y_test, y_pred)
                    r2 = r2_score(y_test, y_pred)

                    st.write(f"Mean Squared Error (MSE): {mse:.2f}")
                    st.write(f"R-squared (R²) Score: {r2:.2f}")

                    # 3D Surface Plot Visualization
                    st.markdown("### 3D Visualization")
                    import numpy as np
                    import plotly.graph_objects as go

                    # Create a grid for 3D surface plot
                    grid_x = np.linspace(data[selected_columns[0]].min(), data[selected_columns[0]].max(), 50)
                    grid_y = np.linspace(data[selected_columns[1]].min(), data[selected_columns[1]].max(), 50)
                    grid_x, grid_y = np.meshgrid(grid_x, grid_y)

                    # Generate placeholders for all features
                    grid_data = np.column_stack([
                        grid_x.ravel(),
                        grid_y.ravel(),
                        np.full(grid_x.ravel().shape, data[selected_columns[2]].mean()),  # Mean of 3rd column
                        np.full(grid_x.ravel().shape, data[selected_columns[3]].mean())   # Mean of 4th column
                    ])

                    # Predict z-values for the grid
                    grid_z = model.predict(grid_data).reshape(grid_x.shape)

                    fig = go.Figure(data=[go.Surface(z=grid_z, x=grid_x, y=grid_y, colorscale="Viridis")])
                    fig.update_layout(
                        scene=dict(
                            xaxis_title=selected_columns[0],
                            yaxis_title=selected_columns[1],
                            zaxis_title="Predicted Death Rate",
                        ),
                        title="3D Surface Plot",
                    )

                    st.plotly_chart(fig, use_container_width=True)

                    # Summary
                    st.markdown("### Summary of the Visualization")
                    st.write(
                        "The 3D surface plot shows how the birth rate, mortality rate, and infant mortality rate interact. A clear trend is observed where higher birth rates are associated with an increase in mortality rates. "
                    )
                    st.write(
                        "The interpolation technique used in the plot smoothens the data, helping to highlight the relationship between the birth rate and mortality rate across the surface."
                    )
                else:
                    st.error("No data available for the selected hypothesis.")
            else:
                st.error("You must select all 5 columns for analysis.")
#Question 4 - Hypothesis 2
        elif hypothesis == "Hypothesis 2: Low birthweight's effect on neonatal mortality and stillbirths":
            st.markdown("### Select Relevant Columns for Analysis")
            # Rename columns to match screenshot
            column_mapping = {
                "Life_expectancy_at_birth_female_years": "Life Expectancy at Birth (Female, Years)",
                "Life_expectancy_at_birth_male_years": "Life Expectancy at Birth (Male, Years)",
                "Life_expectancy_at_birth_total_years": "Life Expectancy at Birth (Total, Years)",
                "Low_birthweight_babies_percent_of_births": "Low-Birthweight Babies (% of Births)",
                "Mortality_rate_infant_per_1000_live_births": "Infant Mortality Rate (Per 1000 Live Births)"
            }

            # Ensure the user selects all relevant columns
            options = st.multiselect(
                "You must select all 5 columns for analysis:",
                list(column_mapping.values()),
            )

            selected_columns = [
                key for key, value in column_mapping.items() if value in options
            ]


            if len(selected_columns) == 5:
                query = f"SELECT {', '.join(selected_columns)} FROM LifeBegins"
                data = fetch_data(query)

                if not data.empty:
                    st.write("Preview of Selected Data:")
                    st.write(data.describe())

                    # Preprocess data
                    X = data[selected_columns[:-1]]  # All columns except the last one
                    y = data[selected_columns[-1]]  # Use the last column as the target

                    # RandomForestRegressor Implementation
                    st.markdown("### Random Forest Regressor Algorithm")
                    st.write(
                        "Random Forest Regressor is an ensemble learning algorithm that builds multiple decision trees "
                        "and averages their outputs to achieve better accuracy and avoid overfitting."
                    )
                    st.latex(r"f(X) = \frac{1}{N} \sum_{i=1}^{N} T_i(X)")
                    st.write(
                        "Here, $N$ is the number of decision trees, $T_i(X)$ is the prediction of the $i$th tree, "
                        "and $f(X)$ is the final prediction by averaging all the trees."
                    )

                    from sklearn.ensemble import RandomForestRegressor
                    from sklearn.model_selection import train_test_split
                    from sklearn.metrics import mean_squared_error, r2_score

                    X_train, X_test, y_train, y_test = train_test_split(
                        X, y, test_size=0.2, random_state=42
                    )

                    model = RandomForestRegressor(random_state=42)
                    model.fit(X_train, y_train)
                    y_pred = model.predict(X_test)

                    mse = mean_squared_error(y_test, y_pred)
                    r2 = r2_score(y_test, y_pred)

                    st.write(f"Mean Squared Error (MSE): {mse:.2f}")
                    st.write(f"R-squared (R²) Score: {r2:.2f}")

                    # 3D Line Plot Visualization
                    st.markdown("### 3D Visualization")
                    import plotly.express as px

                    fig = px.line_3d(
                        data,
                        x=selected_columns[0],
                        y=selected_columns[1],
                        z=selected_columns[2],
                        title="3D Line Plot",
                        labels={
                            selected_columns[0]: selected_columns[0],
                            selected_columns[1]: selected_columns[1],
                            selected_columns[2]: selected_columns[2],
                        },
                    )
                    st.plotly_chart(fig, use_container_width=True)

                    # Summary
                    st.markdown("### Summary of the Visualization")
                    st.write(
                        "The 3D line plot highlights how life expectancy and mortality rates are related. It visually demonstrates that higher mortality rates tend to correspond with lower life expectancy, especially in certain regions."
                    )
                    st.write(
                        "The markers and lines in the plot make it easy to track changes over time and visually identify regions where significant shifts in the trends occur."
                    )
                else:
                    st.error("No data available for the selected hypothesis.")
            else:
                st.error("You must select all 5 columns for analysis.")