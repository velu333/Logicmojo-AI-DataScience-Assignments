# Assignment 03: Population Data Analysis

This assignment demonstrates **Python + Pandas** skills by analyzing the dataset [`population_by_county.csv`](./sample_data/population_by_county.csv).  
The notebook contains step-by-step solutions to explore and summarize U.S. population data at the county and state level.

---

## 📂 Project Structure
```
Assignment-3/
│
├── assignment-03-velayutham_augustheesan_pandas.ipynb   # Main notebook
├── input_utils.py                                       # Utility functions (must be in the same directory as the notebook)
└── sample_data/
    └── population_by_county.csv                         # Dataset
```
---

## 🔍 Tasks Covered
1. Import **pandas** and read `population_by_county.csv` into a dataframe called `population_df`.  
2. Display the **head** of the dataframe and the **top 8 rows** using `.head(8)`.  
3. List all **column names**.  
4. Count the number of **unique states** in the dataset.  
5. Generate a **list of all states** represented in the data.  
6. Identify the **five most common county names** in the U.S.  
7. Find the **top 5 most populated counties** (2010 Census).  
8. Find the **top 5 most populated states** (2010 Census).  
9. Count the **number of counties** with 2010 population > 1 million.  
10. Count the **number of counties** without the word “County” in their name.  
11. Add a **new column** calculating the percent population change between **2010 Census** and **2017 Population Estimate**.  
12. Identify the **states with the highest estimated percent population change** (2010 → 2017).

---

## ▶️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   ```
2. Open the notebook:  
   [assignment-03-velayutham_augustheesan_pandas.ipynb](./assignment-03-velayutham_augustheesan_pandas.ipynb)  
3. Download and ensure `input_utils.py` is in the same directory as the notebook:
   [input_utils.py](./input_utils.py)
4. Ensure the dataset is available in:  
   [sample_data/population_by_county.csv](./sample_data/population_by_county.csv)
5. Run all cells to reproduce the analysis.

---

📌 *This assignment is part of a Python and Pandas learning series.*
