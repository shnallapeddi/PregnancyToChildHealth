#### Leveraging health data to predict infant survival and wellbeing from pregnancy to early childhood.
##### The application empowers users to derive insights from healthcare data, run predictive analyses, and contribute new data entries. By integrating machine learning and user-friendly visualizations, the platform supports healthcare organizations, policymakers, and researchers in addressing critical maternal and infant health challenges globally.

##### Questions and it's relevant Hypotheses

| S.N. | Question | Hypothesis | Algorithm | Visualization |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|-----------------|
| 1 | How do healthcare system factors, such as the number of healthcare professionals, hospital bed capacity, and literacy among healthcare workers, influence maternal and general mortality rates? | Increased healthcare professionals linked to lower maternal mortality rates. <br> Hospital bed capacity linked to mortality rates. <br> Literacy among healthcare workers affects outcomes. | Random Forest <br> Support Vector Machine <br> Decision Tree Algorithm | 3D Scatter Plot <br> 3D Scatter Plot <br> 3D Scatter Plot |
| 2 | Do factors such as skilled health staff attendance during births and maternal health conditions (e.g., anemia, hypertension, or tobacco use) influence neonatal and infant mortality rates? | Regions with higher percentages of births attended by skilled health staff will have significantly lower neonatal and infant mortality rates. <br> Mothers with higher prevalence of anemia, hypertension, or tobacco use are more likely to experience higher rates of neonatal mortality and stillbirths. | Polynomial Regression Algorithm <br> LightGBM Algorithm | 3D Contour Plot <br> 3D Line Plot |
| 3 | How does the combination of immunization coverage (BCG, HepB3, Pol3), literacy rates, and low birthweight contribute to variations in neonatal and infant health outcomes (such as neonatal mortality and stillbirth rates) across different regions? | Higher immunization coverage (BCG, HepB3, Pol3) is associated with lower neonatal mortality and stillbirth rates in regions with higher literacy rates, suggesting that better health education and access to vaccines contribute to improved neonatal health outcomes. <br> Regions with lower prevalence of low birthweight babies will exhibit lower neonatal mortality and stillbirth rates, indicating that maternal nutrition and healthcare interventions to prevent low birthweight play a critical role in improving infant health outcomes. | XGBoost Algorithm | 3D Bubble Plot |
| 4 | How do crude birth and death rates, life expectancy, and low birthweight rates correlate with infant mortality and stillbirth rates across different regions and years? | **Birth Rate Dynamics and Mortality Regions:** Regions with extremely high or low crude birth rates show higher infant mortality and stillbirth rates, indicating population stress or resource constraints. <br> **Yearly Trends:** Over time, regions show a decline in infant mortality rates and neonatal mortality-to-birth rate ratios, correlating with improvements in life expectancy and a reduction in low birthweight babies. | Random Forest Regressor | 3D Surface Plot <br> 3D Line Plot |


##### File Paths

| File Number | Description | File Name |
|------------|--------------------------------------------------------------|----------------------------|
| **File 1** | Notebook containing EDA and Machine Learning models for Phases 1 & 2 | `Phase 1 & 2.ipynb` |
| **File 2** | Dataset used for analysis and modeling in File 1 | `Raw_Data_Updated.csv` |
| **File 3** | Processed CSV file imported into the MySQL database for Phase 3 | `phase3_processed.csv` |
| **File 4** | SQL script used for database operations in Phase 3 | `Phase 3 Script.sql` |
| **File 5** | Notebook to verify MySQL backend connectivity for Phase 3 | `MySQL_Connection.ipynb` |
| **File 6** | Background image for the UI designed in Phase 3 | `DIC.jpg` |
| **File 7** | **Main Python script for Phase 3, compatible with Streamlit** | `HealthFlow.py` |


