import streamlit as st

chart_data = st.session_state.chart_data
st.header("Conference Program")

day1, day2, day3 = st.tabs(["**Friday October 10**", "**Saturday, October 11**", "**Sunday, October 12**"])
with day1:
  st.header("Day 1: Friday October 10, 2025")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("9:00 - 10:00am")
  with col1:
    st.write("**Breakfast & Registration**")
    st.write("Outside Blue Hall, Arts Center (C3)")
    st.write("*Registration will continue past this time if needed at the Library Entrance (C2)*")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("10:00am - 12:00pm")
  with col1:
    st.write("**Opening Ceremony**")
    st.write("Outside Blue Hall, Arts Center (C3)")
  st.markdown("<hr style='width:75%;margin:auto;'>",unsafe_allow_html=True)
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.markdown('<div style="text-align: right;">10:00-10:15am</div>', unsafe_allow_html=True)
  with col1:
    st.write("Awam Amkpa")
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.markdown('<div style="text-align: right;">10:15-11:15am</div>', unsafe_allow_html=True)
  with col1:
    st.write("Keynote Speaker: Annette Vee")
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.markdown('<div style="text-align: right;">11:15-11:45am</div>', unsafe_allow_html=True)
  with col1:
    st.write("Local Speaker: Marion Wrenn")
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.markdown('<div style="text-align: right;">11:45am-12:00pm</div>', unsafe_allow_html=True)
  with col1:
    st.write("Provost's Welcome Address")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("12:00 - 2:30pm")
  with col1:
    st.write("**Lunch and Prayer Break**")
    st.write("Torch Club (D2)")
    st.write("*Prayer Rooms in C2 Ground Floor*")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  st.table(chart_data)
with day2:
  st.header("Day 2: Saturday October 11 2025")
  st.table(chart_data)
with day3:
  st.header("Day 3: Sunday October 12 2025")
  st.table(chart_data)
