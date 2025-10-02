import streamlit as st

chart_data = st.session_state.chart_data
st.header("Conference Program")

day1, day2, day3 = st.tabs(["**Friday October 10**", "**Saturday, October 11**", "**Sunday, October 12**"])
with day1:
  st.header("Day 1: Friday October 10, 2025")
  col0, col1 = st.columns([2,5],gap="small")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  with col0:
    st.write("9:00 - 10:00am")
  with col1:
    st.write("**Breakfast & Registration**")
    st.write("Outside Blue Hall, Arts Center (C3)")
    st.write("*Registration will continue past this time if needed at the Library Entrance (C2)*")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  #st.divider()

  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("10:00am - 12:00pm")
  with col1:
    st.write("**Opening Ceremony**")
    st.write("Outside Blue Hall, Arts Center (C3)")
    
  st.table(chart_data)
with day2:
  st.header("Day 2: Saturday October 11 2025")
  st.table(chart_data)
with day3:
  st.header("Day 3: Sunday October 12 2025")
  st.table(chart_data)
