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

col1, col2, col3, col4 = st.columns(4)

col1.metric("Availability", f"{availability*100:.2f}%")
col2.metric("Performance", f"{performance*100:.2f}%")
col3.metric("Quality", f"{quality*100:.2f}%")
col4.metric("OEE", f"{oee*100:.2f}%")

# Summary Table
st.markdown("### 📝 Production Summary")

st.write(
    {
        "Planned Time (min)": planned_time,
        "Downtime (min)": downtime,
        "Running Time (min)": running_time,
        "Total Units": total_units,
        "Good Units": good_units,
        "Ideal Cycle Time (min/unit)": ideal_cycle_time,
        "Availability (%)": round(availability*100, 2),
        "Performance (%)": round(performance*100, 2),
        "Quality (%)": round(quality*100, 2),
        "OEE (%)": round(oee*100, 2),
    }
)



