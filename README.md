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

### 1. Healthcare System Factors  
- **Hypothesis:** More physicians, nurses, beds, and higher literacy among healthcare workers correlate with lower maternal mortality  
- **Models:** Random Forest, SVM, Decision Tree  
- **Visualization:** 3D Scatter Plots  

### 2. Maternal Health & Birth Attendance  
- **Hypothesis:** Skilled birth attendance and maternal conditions (anemia, hypertension, tobacco use) drive neonatal and infant mortality  
- **Models:** Polynomial Regression, LightGBM  
- **Visualization:** 3D Contour & Line Plots  

### 3. Immunization, Literacy & Low Birthweight  
- **Hypothesis:** Higher vaccine coverage and literacy reduce neonatal mortality; low birthweight prevalence increases risk  
- **Model:** XGBoost  
- **Visualization:** 3D Bubble Plots  

### 4. Birth/Death Rates & Life Expectancy Trends  
- **Hypothesis:** Extreme crude birth rates and low life expectancy correlate with higher infant mortality; trends improve over time  
- **Model:** Random Forest Regressor  
- **Visualization:** 3D Surface & Line Plots  

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
