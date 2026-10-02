---
name: notebook-to-streamlit
description: Convert delivery promise optimization logic from a Jupyter Notebook into a production-ready Streamlit web application for Rosa's Pizza.
---

# notebook-to-streamlit

This skill defines the rules for converting the delivery promise notebook logic into a Streamlit web application (`app.py`).

## App Requirements
1. **Sidebar Inputs:**
   - Dropdown menus for selecting `Zone` and `Time Block`.
   - Number inputs/sliders for promise range bounds (min, max, step size).
   - Adjustable financial parameters: `Profit Margin`, `Churn Orders`, and `Refund Cost`.
2. **Core Optimization Function:**
   - Uses `delivery_times(zone, time_block, promise, seed)` from `starter`.
   - Calculates total cost per late order = `refund + (churn * margin)`.
   - Iterates through the promise range to find the promise maximizing `gross_profit - late_costs`.
3. **Execution Button:**
   - Runs the evaluation when the user clicks `"Calculate Best Delivery Promise"`.
   - Displays the recommended promise time and maximized net profit prominently.
