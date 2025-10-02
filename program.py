import streamlit as st

chart_data = st.session_state.chart_data
st.header("Conference Program")

day1, day2, day3 = st.tabs(["Friday October 10", "Saturday, October 11", "Sunday, October 12"])
with day1:
  st.table(chart_data)
with day2:
  st.write("This is an expander")
  st.table(chart_data)
with day3:
  st.table(chart_data)
