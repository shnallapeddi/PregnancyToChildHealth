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


### I. The Questions Listed for Each Team Member


## **Anchal Daga**
### **Question 1:**
How do healthcare system factors, such as the number of healthcare professionals, hospital bed capacity, and literacy among healthcare workers, influence maternal and general mortality rates?

---
## **Keerthana Vangala**
### **Question 2:**
How do factors such as skilled health staff attendance during births and maternal health conditions (e.g., anaemia, hypertension, or tobacco use) influence neonatal and infant mortality rates?


---
## **Grace Evangelene Avula Lael**
### **Question 3:**
How does the combination of immunization coverage (BCG, HepB3, Pol3), literacy rates, and low birthweight contribute to variations in neonatal and infant health outcomes (such as neonatal mortality and stillbirth rates) across different regions?

---

## **Sharanya Nallapeddi**
### **Question 4:**
How do crude birth and death rates, life expectancy, and low-birthweight rates correlate with infant mortality and stillbirth rates across different regions and years?

---

 # Project Details

## Path of the Files
- **Main File for Phase 3:** `50609480_50604773_50595809_50593866/app/HealthFlow.py`
- **Background Image of the UI:** `50609480_50604773_50595809_50593866/app/DIC.jpg`
- **MySQL Script File to Run:** `50609480_50604773_50595809_50593866/app/Phase 3 Script.sql`
- **File to Check the Backend MySQL Connection:** `50609480_50604773_50595809_50593866/app/MySQL Connection.ipynb`
- **CSV File Imported into MySQL Database:** `50609480_50604773_50595809_50593866/app/phase3_processed.csv`

---

## Key Research Questions and Hypotheses

| S.N. | Question | Hypothesis | Algorithm | Visualization | Experiment Code Location | Analysis Location |
|------|----------|------------|-----------|---------------|---------------------------|-------------------|
| 1 | How do healthcare system factors, such as the number of healthcare professionals, hospital bed capacity, and literacy among healthcare workers, influence maternal and general mortality rates? | Increased healthcare professionals linked to lower maternal mortality rates | Random Forest Algorithm | 3D Scatter Plot | Line 653 | Line 756 |
|   |   | Hospital bed capacity linked to mortality rates | Support Vector Machine Algorithm | 3D Scatter Plot | Line 766 | Line 840 |
|   |   | Literacy among healthcare workers affects outcomes | Decision Tree Algorithm | 3D Scatter Plot | Line 850 | Line 931 |
| 2 | How do factors such as skilled health staff attendance during births and maternal health conditions (e.g., anemia, hypertension, or tobacco use) influence neonatal and infant mortality rates? | Regions with higher percentages of births attended by skilled health staff will have significantly lower neonatal and infant mortality rates | Polynomial Regression Algorithm | 3D Contour Plot | Line 950 | Line 1032 |
|   |   | Mothers with higher prevalence of anemia, hypertension, or tobacco use are more likely to experience higher rates of neonatal mortality and stillbirths | LightGBM Algorithm | 3D Line Plot | Line 1044 | Line 1129 |
| 3 | How does the combination of immunization coverage (BCG, HepB3, Pol3), literacy rates, and low birthweight contribute to variations in neonatal and infant health outcomes (such as neonatal mortality and stillbirth rates) across different regions? | Higher immunization coverage (BCG, HepB3, Pol3) is associated with lower neonatal mortality and stillbirth rates in regions with higher literacy rates, suggesting that better health education and access to vaccines contribute to improved neonatal health outcomes | XGBoost Algorithm | 3D Bubble Plot | Line 1151 | Line 1241 |
|   |   | Regions with lower prevalence of low birthweight babies will exhibit lower neonatal mortality and stillbirth rates, indicating that maternal nutrition and healthcare interventions to prevent low birthweight play a critical role in improving infant health outcomes | - | - | Line 1253 | Line 1338 |
| 4 | How do crude birth and death rates, life expectancy, and low-birthweight rates correlate with infant mortality and stillbirth rates across different regions and years? | Birth Rate Dynamics and Mortality: Regions with extremely high or low crude birth rates show higher infant mortality and stillbirth rates, indicating population stress or resource constraints | RandomForestRegressor | 3D Surface Plot | Line 1359 | Line 1451 |
|   |   | Yearly Trends: Over time, regions show a decline in infant mortality rates and neonatal mortality-to-birth rate ratios, correlating with improvements in life expectancy and a reduction in low-birthweight babies | RandomForestRegressor | 3D Line Plot | Line 1462 | Line 1546 |




### V. The Instructions to Build the App from Source Code

1. Download and install the appropriate version of MySQL Server, MySQL Installer and MySQL workbenchfor your system.(Set a root password for MySQL workbench during setup and note it)
2. Launch sql and connect to local MySQL server.
3. Create database, create schema of the table and load data from the csvfile() into a table.(Code in present in the location: "50609480_50604773_50595809_50593866/app/Phase 3 Script.sql" with name: Phase 3 Script.sql)
4. Install python
5. install streamlit in command prompt using the below code:
"pip install streamlit"
6. We have created a python file for streamlit ("HealthFlow" present at location: "50609480_50604773_50595809_50593866/app/HealthFlow.py").
7. Go to the location of the file in command prompt and run the file using command:
"streamlit run HealthFlow.py"

Note: 
1.Please change the database connection details with your database details in the python file.
2. Install additional python libraries if necessary which are not installed on the system: 
for instance: "python -m pip show plotly"


