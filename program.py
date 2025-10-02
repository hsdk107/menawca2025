import streamlit as st

chart_data = st.session_state.chart_data
st.header("Conference Program")

st.subheader("Friday, October 10 2025")
st.table(chart_data)

st.divider()

with st.expander("Saturday, October 11 2025"):
  st.write("This is an expander")
  st.table(chart_data)

st.divider()

st.subheading("Sunday, October 12 2025")
st.table(chart_data)
