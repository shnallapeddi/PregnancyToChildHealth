# Topic: Leveraging health data to predict infant survival and wellbeing from pregnancy to early childhood.
## The application empowers users to derive insights from healthcare data, run predictive analyses, and contribute new data entries. By integrating machine learning and user-friendly visualizations, the platform supports healthcare organizations, policymakers, and researchers in addressing critical maternal and infant health challenges globally.

# Team Members
| Name                        | UB Number | UB Email             | 
|:-----                       |:--------: |------:               |
| Anchal Daga                 | 50609480  | anchalda@buffalo.edu |
| Keerthana Vangala           | 50604773  | kvangala@buffalo.edu |
| Grace Evangelene Avula Lael | 50595809  | graceeva@buffalo.edu |
| Sharanya Nallapeddi         | 50593866  | snallape@buffalo.edu |

# Highlights 
1. Data-Driven Insights: Analyze trends and correlations in global health metrics.
2. User Engagement: Empower users to add, update, and explore data for continuous learning.
3. Predictive Modeling: Utilize our machine learning models to predict health outcomes based on user-provided data.
4. The application provides several machine learning models, including Random Forest Regressor, XGBoost, Polynomial Regression, and LightGBM. These models analyze various health indicators to predict outcomes such as neonatal mortality, maternal mortality, and birth-death ratios. Users can select relevant columns for analysis, and the app trains and evaluates models using metrics like Mean Squared Error (MSE) and R-squared scores.
5. Customizable Filters: Visualize and study health data by region, year, and demographic categories.

### Questions and it's relevant Hypotheses

<img width="1403" alt="image" src="https://github.com/user-attachments/assets/0597654c-156f-44f2-adc0-85f783174c57" />

## Path of the Files
- **Main File for Phase 3:** `50609480_50604773_50595809_50593866/app/HealthFlow.py`
- **Background Image of the UI:** `50609480_50604773_50595809_50593866/app/DIC.jpg`
- **MySQL Script File to Run:** `50609480_50604773_50595809_50593866/app/Phase 3 Script.sql`
- **File to Check the Backend MySQL Connection:** `50609480_50604773_50595809_50593866/app/MySQL Connection.ipynb`
- **CSV File Imported into MySQL Database:** `50609480_50604773_50595809_50593866/app/phase3_processed.csv`

### Instructions to Build the App from Source Code

1. Download and install the correct version of MySQL Server, MySQL Installer, and MySQL Workbench for your operating system. During setup, set a root password for MySQL Workbench and make a note of it.
2. Open MySQL and connect to the local MySQL server.
3. Create the table schema and load data from the CSV file (phase3_processed.csv) into a table. The file can be found at: CSV File Imported into MySQL Database:. Use the script provided in the following location: "50609480_50604773_50595809_50593866/app/Phase 3 Script.sql", named Phase 3 Script.sql.
4. Install the latest version of Python if possible, and install all the required libraries mentioned below:
  a. streamlit
  b. pandas
  c. mysql-connector
  d. sklearn
  e. plotly
  f.base64 
5. Verify the MySQL connection by using the provided file: MySQL Connection.ipynb.
6. After verification, launch the application using the Python file compatible with the backend named "HealthFlow.py".
7. To set a background image for the user interface, use the file "DIC.jpg" in the HealthFlow.py file.
8. Navigate to the file location in the command prompt and run the application using the command:
   streamlit run path/to/HealthFlow.py

### Note: 
Please change the database connection details with your database details in the python file.



