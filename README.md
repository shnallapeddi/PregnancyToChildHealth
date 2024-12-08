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


### II. The Information of Where the Experiment Code Associated with Each Question Is Located

- **Question 1 Code Location:** [File name or line number in the notebook]
- **Question 2 Code Location:** [File name or line number in the notebook]
- **Question 3 Code Location:** [File name or line number in the notebook]
- **Question 4 Code Location:** [File name or line number in the notebook]

### III. The Analysis of the Question is Located

- **Question 1 Analysis Location:** [File name or line number in the notebook]
- **Question 2 Analysis Location:** [File name or line number in the notebook]
- **Question 3 Analysis Location:** [File name or line number in the notebook]
- **Question 4 Analysis Location:** [File name or line number in the notebook]

### IV. The Folder Structure Information

- **app/** contains all the app code
- **exp/** contains final version of the previous python notebook code
- **exp/results/** contains the experiment results
- **data/** contains the raw and cleaned data files
- **docs/** contains the project documentation and additional resources

### V. The Instructions to Build the App from Source Code

1. Download and install the appropriate version of MySQL Server, MySQL Installer and MySQL workbenchfor your system.(Set a root password for MySQL workbench during setup and note it)
2. Launch sql and connect to our local MySQL server.
3. Create database, create schema of the table and load data from the csvfile() into a table.(Code in present in the location with name)
4. Install python
5. install streamlit in command prompt using the below code:
"pip install streamlit"
6. We have created a python file for streamlit ("HealthFlow" present at location).
7. Go to the location of the file in command prompt and run the file using command:
"streamlit run HealthFlow.py"

Note: 1.Please change the database connection details with your database details in the python file.
2. Install additional libraries if necessary.

