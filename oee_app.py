import streamlit as st

st.set_page_config(page_title="OEE Dashboard", layout="wide")

st.title("🏭 OEE Dashboard (Professional Version)")

# Inputs
st.sidebar.header("Input Values")
planned_time = st.sidebar.number_input("Planned Production Time (minutes)", min_value=1, value=480)
downtime = st.sidebar.number_input("Downtime (minutes)", min_value=0, value=60)
total_units = st.sidebar.number_input("Total Units Produced", min_value=1, value=1000)
good_units = st.sidebar.number_input("Good Units Produced", min_value=0, value=950)
ideal_cycle_time = st.sidebar.number_input("Ideal Cycle Time (minutes/unit)", min_value=0.01, value=0.5)

# Calculations
running_time = planned_time - downtime
availability = running_time / planned_time
performance = (ideal_cycle_time * total_units) / running_time
quality = good_units / total_units
oee = availability * performance * quality

# KPI Layout
st.markdown("### 📊 Key Performance Indicators")

# Function for KPI color
def kpi_color(value, green, yellow):
    if value >= green:
        return "#2ECC71"  # green
    elif value >= yellow:
        return "#F1C40F"  # yellow
    else:
        return "#E74C3C"  # red

# Calculate % values
A = availability * 100
P = performance * 100
Q = quality * 100
O = oee * 100

# KPI Row
st.markdown("### 📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div style="background-color:{kpi_color(A,90,80)};
            padding:20px;border-radius:10px;text-align:center">
            <h4>Availability</h4>
            <h2>{A:.2f}%</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div style="background-color:{kpi_color(P,95,85)};
            padding:20px;border-radius:10px;text-align:center">
            <h4>Performance</h4>
            <h2>{P:.2f}%</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <div style="background-color:{kpi_color(Q,98,92)};
            padding:20px;border-radius:10px;text-align:center">
            <h4>Quality</h4>
            <h2>{Q:.2f}%</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        f"""
        <div style="background-color:{kpi_color(O,85,70)};
            padding:20px;border-radius:10px;text-align:center">
            <h4>OEE</h4>
            <h2>{O:.2f}%</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )
