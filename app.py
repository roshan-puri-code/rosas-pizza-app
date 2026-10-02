import streamlit as st
import numpy as np
from starter import ZONES, TIME_BLOCKS, COSTS, delivery_times

st.set_page_config(page_title="Rosa's Pizza - Delivery Promise Optimizer", layout="centered")

st.title("🍕 Rosa's Pizza: Delivery Promise Optimizer")
st.write("Use this tool to find the optimal promised delivery time that maximizes net profit.")

# Sidebar Controls
st.sidebar.header("1. Selection")
selected_zone = st.sidebar.selectbox("Select Zone", ZONES)
selected_block = st.sidebar.selectbox("Select Time Block", TIME_BLOCKS)

st.sidebar.header("2. Promise Range (Minutes)")
min_promise = st.sidebar.number_input("Minimum Promise", min_value=5, max_value=60, value=15, step=5)
max_promise = st.sidebar.number_input("Maximum Promise", min_value=30, max_value=120, value=75, step=5)
step_size = st.sidebar.number_input("Step Size", min_value=1, max_value=10, value=5, step=1)

st.sidebar.header("3. Financial Parameters ($)")
margin = st.sidebar.number_input("Profit Margin per Order ($)", value=float(COSTS['margin']), step=0.5)
churn_orders = st.sidebar.number_input("Churn Orders per Late Order", value=float(COSTS['churn_orders']), step=0.1)
refund = st.sidebar.number_input("Refund Cost per Late Order ($)", value=float(COSTS['refund']), step=0.5)

def calculate_cost_per_late(refund_val, churn_val, margin_val):
    return refund_val + (churn_val * margin_val)

def find_best_promise(zone, time_block, promise_list, refund_val, churn_val, margin_val, seed=42):
    cost_per_late = calculate_cost_per_late(refund_val, churn_val, margin_val)

    best_promise = None
    max_net_profit = -float('inf')

    for p in promise_list:
        times = delivery_times(zone, time_block, p, seed=seed)
        num_orders = len(times)
        num_late = np.sum(times > p)

        gross_profit = num_orders * margin_val
        late_costs = num_late * cost_per_late
        net_profit = gross_profit - late_costs

        if net_profit > max_net_profit:
            max_net_profit = net_profit
            best_promise = p

    return best_promise, max_net_profit

st.subheader("Run Optimization")
st.write(f"Click below to calculate the optimal delivery promise for **{selected_zone}** during **{selected_block}**.")

if st.button("Calculate Best Delivery Promise"):
    promise_range = list(range(int(min_promise), int(max_promise) + int(step_size), int(step_size)))

    recommended_p, best_profit = find_best_promise(
        selected_zone, 
        selected_block, 
        promise_range, 
        refund, 
        churn_orders, 
        margin
    )

    st.success(f"**Recommended Promise:** {recommended_p} minutes")
    st.metric(label="Maximized Net Profit", value=f"${best_profit:,.2f}")
