## From Bump to Baby: Maternal & Infant Health Insights

**Leveraging health data to predict infant survival and well-being from pregnancy to early childhood.**
A Streamlit app that turns global maternal–infant health data into interactive insights, forecasts, and explainable visuals. It includes filterable dashboards, CRUD-style data editing, and a “behind the algorithms” section that explains the ML you run in the app. The Space is published on Hugging Face.

### Live demo
Hugging Face Space: https://huggingface.co/spaces/snallapeddi/PregnancyToChildHealth
If the Space is sleeping, click Restart this Space; it will wake and load the app.

### What’s inside to explore
### Tabs / Navigation
1. Insights Hub – landing page with quick links and short video teasers for explore/predict/visualize actions. Buttons jump to the working tabs.
2. Global Health at a Glance – filter by Year, Region, and Health Category (Health Resources, Maternal Data, Infant Health) and view/adjust data via a CRUD menu (Lookup / Add / Modify / Remove).
3. Hypotheses in Action – run ML models (Random Forest, Decision Tree, plus other options described) and see predictions, feature importances, and metrics (R², MAE, RMSE) with interactive Plotly charts.
4. Behind the Algorithms – readable explainers for the algorithms, with formulas and short references.

### Data
The app loads processed.csv (cached) as its primary dataset.

### How to use the live demo
Open the Space and let it wake if sleeping; you’ll land on Insights Hub. Use the large Explore / Predict / Contribute / Visualize buttons to jump to the working tabs.
1. In Global Health at a Glance, set Year, Region, and Health Category in the sidebar to slice the data. Use the CRUD Operations dropdown for Lookup, Add Entry, Modify Entry, or Remove Entry; follow the on-screen forms and confirmations. (Edits in the public demo are session-level and not meant as permanent writes.)
2. Switch to Hypotheses in Action, choose a target (e.g., Neonatal Mortality Rate), select a model (e.g., Random Forest or Decision Tree), and click Run Prediction. Inspect metrics (R², MAE, RMSE), feature importances, and interactive charts.
3. Visit Behind the Algorithms for short explanations, formulas, and links if you want the math story behind the models.

### Run locally
#### 1) Clone
git clone https://huggingface.co/spaces/snallapeddi/PregnancyToChildHealth
cd PregnancyToChildHealth
#### 2) Create env (Python 3.10+ recommended)
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activat
#### 3) Install
pip install -r requirements.txt
#### 4) Run
streamlit run app.py

Notes & tips
a. If filters appear empty, first choose All in “Filter by Category,” then refine.
b. Some CRUD actions are UI-level for exploration; the public Space does not provide persistent writes to a database.
c. For best performance, let the app finish loading cached data before running models.



