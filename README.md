## Topic: Leveraging health data to predict infant survival and wellbeing from pregnancy to early childhood.
### The application empowers users to derive insights from healthcare data, run predictive analyses, and contribute new data entries. By integrating machine learning and user-friendly visualizations, the platform supports healthcare organizations, policymakers, and researchers in addressing critical maternal and infant health challenges globally.

### Team Members
| Name                        | UB Number | UB Email             | 
|:-----                       |:--------: |------:               |
| Anchal Daga                 | 50609480  | anchalda@buffalo.edu |
| Keerthana Vangala           | 50604773  | kvangala@buffalo.edu |
| Grace Evangelene Avula Lael | 50595809  | graceeva@buffalo.edu |
| Sharanya Nallapeddi         | 50593866  | snallape@buffalo.edu |

### Highlights 
1. We started with extensive data collection from opensource platforms like https://www.healthdata.org/, https://databank.worldbank.org/. Later, transforming unstructured data into structured format in this code involved several steps. The code demonstrates advanced feature engineering by creating new columns based on domain-specific logic and inter-variable relationships. Derived metrics, such as the Birth-Death Ratio and Infant Mortality Rate to Birth Rate Ratio, are constructed using arithmetic operations on related columns, leveraging domain knowledge for meaningful insights. Aggregates like Immunization Efficacy are computed as the mean of immunization rates from multiple columns, while differences such as Life Expectancy Difference between genders highlight inter-variable comparisons. Outliers are handled using IQR-based capping, ensuring that extreme values do not distort analysis, while anomalies like negative or invalid values are systematically replaced or coerced into usable formats using conditions (>=0) and custom imputation strategies. Unique to this implementation is the region-aware imputation logic, where invalid values (..) are replaced based on region-specific averages or similar regions with matching metrics, ensuring contextual accuracy. These targeted transformations, combined with deterministic truncation for numerical stability, make the feature engineering process highly tailored and robust.    
2. For the structured data, we conducted exploratory data analysis by formulating specific questions and hypotheses. Based on the relevance of columns associated with these questions, we selected various machine learning algorithms to evaluate the effectiveness of the questions and validate how well our hypotheses align with them.
3. 


### Questions and it's relevant Hypotheses

<img width="1403" alt="image" src="https://github.com/user-attachments/assets/0597654c-156f-44f2-adc0-85f783174c57" />

### File Paths
<img width="779" alt="image" src="https://github.com/user-attachments/assets/9fd90150-a001-428a-9783-ce13a7ce63f9" />

### Instructions to Build the App from Source Code

To set up and run the HealthFlow application, first, download and install the appropriate versions of MySQL Server, MySQL Installer, and MySQL Workbench for your OS, ensuring to set and remember a root password for MySQL Workbench. Once installed, open MySQL and connect to the local server. Then, create the required table schema and load data from the CSV file (phase3_processed.csv) into a table using the script named "Phase 3 Script.sql," which can be found in the specified file location. Next, install the latest version of Python and ensure the required libraries (streamlit, pandas, mysql-connector, sklearn, plotly, and base64) are installed. Verify the MySQL connection using the provided file "MySQL Connection.ipynb." After successful verification, launch the application using the Python file named "HealthFlow.py" and set a background image for the user interface using the file "DIC.jpg" included in the files. Finally, navigate to the application file location in the command prompt and run the application using the command `streamlit run path/to/HealthFlow.py`.

### Note: 
Please change the database connection details with your database details in the python file.



