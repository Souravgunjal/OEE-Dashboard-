import streamlit as st

st.set_page_config(page_title="OEE Calculator", layout="wide")

st.title("🏭 OEE Calculator (Simple & Error-Free Version)")

# Inputs
st.subheader("Input Values")

planned_time = st.number_input("Planned Production Time (minutes)", min_value=1, value=480)
downtime = st.number_input("Downtime (minutes)", min_value=0, value=60)
total_units = st.number_input("Total Units Produced", min_value=1, value=1000)
good_units = st.number_input("Good Units Produced", min_value=0, value=950)
ideal_cycle_time = st.number_input("Ideal Cycle Time (minutes/unit)", min_value=0.01, value=0.5)

# Calculations
running_time = planned_time - downtime
availability = running_time / planned_time
performance = (ideal_cycle_time * total_units) / running_time
quality = good_units / total_units
oee = availability * performance * quality

# Display results
st.subheader("Results")

st.metric("Availability", f"{availability * 100:.2f}%")
st.metric("Performance", f"{performance * 100:.2f}%")
st.metric("Quality", f"{quality * 100:.2f}%")
st.metric("OEE", f"{oee * 100:.2f}%")
