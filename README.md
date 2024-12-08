Team Members

| Name                        | UB Number | UB Email             | 
|:-----                       |:--------: |------:               |
| Anchal Daga                 | 50609480  | anchalda@buffalo.edu |
| Keerthana Vangala           | 50604773  | kvangala@buffalo.edu |
| Grace Evangelene Avula Lael | 50595809  | graceeva@buffalo.edu |
| Sharanya Nallapeddi         | 50593866  | snallape@buffalo.edu |

<!--
Topic of Project: Leveraging health data to predict infant survival and wellbeing from pregnancy to early childhood.

Note: To distinguish between phases 1, 2, and 3, we have renamed the files accordingly. The file titled "Raw_Data_Updated" is our initial dataset which is used across all the phases. 

Phase 1:
Main File: Main_phase1.ipynb
We conducted exploratory data analysis (EDA) separately using the "feature_engineering" CSV and XLS files. These files represent the Excel sheet created after all data cleaning steps were completed.

Phase 2:
The data cleaning process was refined in Phase 2 to enhance accuracy and improve the dataset quality.
The file cleaned_dataset_rounded_off.csv is used as the input for data loading.
Individual .ipynb files labeled with "phase2" have been uploaded.
-->

# Project Details

## Path of the Files
- **Main File for Phase 3:** `50609480_50604773_50595809_50593866/app/HealthFlow.py`
- **Background Image of the UI:** `50609480_50604773_50595809_50593866/app/DIC.jpg`
- **MySQL Script File to Run:** `50609480_50604773_50595809_50593866/app/Phase 3 Script.sql`
- **File to Check the Backend MySQL Connection:** `50609480_50604773_50595809_50593866/app/MySQL Connection.ipynb`
- **CSV File Imported into MySQL Database:** `50609480_50604773_50595809_50593866/app/phase3_processed.csv`

---

## Key Research Questions and Hypotheses

| S.N. | Question    | Name of the Student Who Worked on the Questions | Hypothesis       | Algorithm                  | Visualization    | Experiment Code Location | Analysis Location |
|------|-------------|-----------------------------------------------|------------------|---------------------------|------------------|--------------------------|-------------------|
| 1    | Question 1  | Anchal Daga                                   | Hypothesis 1     | Random Forest Algorithm    | 3D Scatter Plot  | Line 653                 | Line 756          |
|      |             |                                               | Hypothesis 2     | Support Vector Machine Algorithm | 3D Scatter Plot  | Line 766                 | Line 840          |
|      |             |                                               | Hypothesis 3     | Decision Tree Algorithm    | 3D Scatter Plot  | Line 850                 | Line 931          |
| 2    | Question 2  | Keerthana Vangala                             | Hypothesis 1     | Polynomial Regression Algorithm | 3D Contour Plot  | Line 950                 | Line 1032         |
|      |             |                                               | Hypothesis 2     | LightGBM Algorithm         | 3D Line Plot      | Line 1044                | Line 1129         |
| 3    | Question 3  | Grace Evangelene                              | Hypothesis 1     | XGBoost Algorithm          | 3D Bubble Plot   | Line 1151                | Line 1241         |
|      |             |                                               | Hypothesis 2     | -                         | -                | Line 1253                | Line 1338         |
| 4    | Question 4  | Sharanya Nallapeddi                           | Hypothesis 1     | RandomForestRegressor      | 3D Surface Plot  | Line 1359                | Line 1451         |
|      |             |                                               | Hypothesis 2     | RandomForestRegressor      | 3D Line Plot      | Line 1462                | Line 1546         |




### V. The Instructions to Build the App from Source Code

1. Download and install the appropriate version of MySQL Server, MySQL Installer and MySQL workbench for your system.(Set a root password for MySQL workbench during setup and note it down)
2. Launch sql and connect to local MySQL server.
3. Create schema of the table and load data from the csvfile(phase3_processed.csv, location: CSV File Imported into MySQL Database:) into a table.(Code is present in the location: "50609480_50604773_50595809_50593866/app/Phase 3 Script.sql" with name: Phase 3 Script.sql)
4. Install python
5. install streamlit in command prompt using the below code:
"pip install streamlit"
6. We have created a python file for hosting on streamlit.(File name: "HealthFlow" is present at location: "50609480_50604773_50595809_50593866/app/HealthFlow.py").
7. 
8. Go to the location of the file in command prompt and run the file using command:
"streamlit run HealthFlow.py"

Note: 

1.Please change the database connection details with your database details in the python file.
2. Install additional python libraries if necessary which are not installed on the system: 
for instance: "python -m pip show plotly"


