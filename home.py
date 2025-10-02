import streamlit as st
from cards import (
	widgets_card,
	dataframe_card,
	layouts_card
)

st.title("Streamlit element explorer")

st.markdown(
	"This app displays most of Streamlit's built-in elements so you can "
	"conveniently explore how they look with different theming configurations "
	"applied."
)

cols = st.columns(2)
with cols[0].container(height=310):
	widgets_card()
with cols[0].container(height=310):
	dataframe_card()
with cols[1].container(height=310):
	layouts_card()
