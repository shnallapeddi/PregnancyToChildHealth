# From Bump to Baby: Maternal & Infant Health Insights

**Leveraging health data to predict infant survival and well-being from pregnancy to early childhood.**

This interactive dashboard empowers researchers, policymakers, and healthcare professionals to explore global maternal and infant health data, run predictive analyses, and contribute new entries. By combining rigorous machine-learning models with intuitive visualizations, we illuminate the factors that drive outcomes from the first heartbeat through those critical early years—so every mother’s journey and every child’s first steps are guided by data-driven insight.

---

## Key Features

- **Interactive Filters & CRUD**  
  Select by year, region, and health category; perform lookup, add, modify, or remove data entries.

- **Predictive Modeling**  
  Random Forest • SVM • Decision Tree • Polynomial Regression • LightGBM • XGBoost

- **3D Visualizations**  
  Scatter • Contour • Line • Bubble • Surface plots for comprehensive insights

- **User Contributions**  
  Seamlessly add or refine records to keep the dataset up to date

---

## Research Questions & Approaches

1. **Healthcare System Impact**  
   We examine how the availability of healthcare professionals, hospital bed capacity, and staff literacy levels influence maternal and overall mortality rates. By applying ensemble methods (Random Forest, SVM, Decision Tree) and visualizing relationships in 3D scatter plots, we uncover which system‐level factors most strongly predict better maternal outcomes.

2. **Maternal Health & Birth Attendance**  
   Focusing on skilled attendance at birth and maternal conditions—such as anemia, hypertension, and tobacco use—we model their effect on neonatal and infant mortality using Polynomial Regression and LightGBM. Contour and line‐style 3D plots reveal critical thresholds where health interventions yield the greatest benefit.

3. **Immunization, Education & Low Birthweight**  
   We explore the combined influence of vaccine coverage (BCG, HepB3, Pol3), health literacy, and low‐birthweight prevalence on neonatal survival. XGBoost models quantify these interactions, while 3D bubble charts highlight regions where integrated public‐health strategies can drive the largest improvements.

4. **Birth/Death Dynamics Over Time**  
   Analyzing crude birth and death rates alongside life expectancy trends and low‐birthweight metrics, we assess how demographic shifts correlate with infant mortality and stillbirth rates. Using Random Forest regression and 3D surface/line plots, we trace progress over years and identify regions that would benefit most from targeted resource allocation.  
 
---

## Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/shnallapeddi/PregnancyToChildHealth.git
   cd PregnancyToChildHealth
2. **Install dependencies**
   pip install -r requirements.txt
3. **Run the application**
   streamlit run HealthFlow.py

 ---

## Live Demo
Access the live application here:
https://huggingface.co/spaces/snallapeddi/PregnancyToChildHealth
