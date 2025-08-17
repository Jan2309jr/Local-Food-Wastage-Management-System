# Local Food Wastage Management System

A Streamlit + SQLite project to connect surplus food providers with receivers, reduce waste, and analyze trends.

## How to run

```bash
# 1) Create venv (optional) and install deps
pip install -r requirements.txt

# 2) Initialize DB and load CSVs (put your 4 CSVs under data/ with the exact names)
python data/database/load_data.py

# 3) Launch Streamlit
streamlit run streamlit_app/app.py
```

### File structure

- **data/database/schema.sql** – Creates tables & indexes
- **data/database/queries.sql** – 15 reference SQL queries
- **data/database/load_data.py** – Creates DB and loads CSVs
- **data/database/crud_operations.py** – CRUD functions using sqlite3
- **streamlit_app/utils/db_connection.py** – DB connection helper
- **streamlit_app/utils/query_functions.py** – Python helpers to run the 15 queries
- **streamlit_app/utils/filters.py** – Filter helpers for the main page
- **streamlit_app/utils/visualization.py** – Plotly chart helpers
- **streamlit_app/pages/** – Multi-page: EDA, CRUD UI, SQL outputs
- **streamlit_app/app.py** – Main entry (filter + overview)

### Notes
- Uses **SQLite** (`food.db`) for simplicity. Switch to PostgreSQL/MySQL by replacing the connection helpers.
- Ensure your CSV headers match the dataset description.
