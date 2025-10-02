import streamlit as st

chart_data = st.session_state.chart_data
st.header("Conference Program")

day1, day2, day3 = st.tabs(["**Friday October 10**", "**Saturday, October 11**", "**Sunday, October 12**"])
with day1:
  st.header("Day 1: Friday October 10, 2025")
  st.table(chart_data)
with day2:
  st.header("Day 2: Saturday October 11 2025")
  st.table(chart_data)
with day3:
  st.header("Day 3: Sunday October 12 2025")
  st.table(chart_data)
