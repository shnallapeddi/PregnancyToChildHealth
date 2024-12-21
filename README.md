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


### Questions and it's relevant Hypotheses

<img width="1403" alt="image" src="https://github.com/user-attachments/assets/0597654c-156f-44f2-adc0-85f783174c57" />

## Path of the Files
- **Main File for Phase 3:** `HealthFlow.py`
- **Background Image of the UI:** `5DIC.jpg`
- **MySQL Script File to Run:** `Phase 3 Script.sql`
- **File to Check the Backend MySQL Connection:** `5MySQL Connection.ipynb`
- **CSV File Imported into MySQL Database:** `phase3_processed.csv`

### Instructions to Build the App from Source Code

To set up and run the HealthFlow application, first, download and install the appropriate versions of MySQL Server, MySQL Installer, and MySQL Workbench for your OS, ensuring to set and remember a root password for MySQL Workbench. Once installed, open MySQL and connect to the local server. Then, create the required table schema and load data from the CSV file (phase3_processed.csv) into a table using the script named "Phase 3 Script.sql," which can be found in the specified file location. Next, install the latest version of Python and ensure the required libraries (streamlit, pandas, mysql-connector, sklearn, plotly, and base64) are installed. Verify the MySQL connection using the provided file "MySQL Connection.ipynb." After successful verification, launch the application using the Python file named "HealthFlow.py" and set a background image for the user interface using the file "DIC.jpg" included in the files. Finally, navigate to the application file location in the command prompt and run the application using the command `streamlit run path/to/HealthFlow.py`.

### Note: 
Please change the database connection details with your database details in the python file.



