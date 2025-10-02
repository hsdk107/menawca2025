import streamlit as st
import pandas as pd
import numpy as np
#from cards import (
#	widgets_card,
#	dataframe_card,
#	layouts_card
#)

if "init" not in st.session_state:
	st.session_state.chart_data = pd.DataFrame(
		np.random.randn(20, 3), columns=["a", "b", "c"]
	)
	st.session_state.init = True

pages = [
	st.Page(
		"home.py",
		title="Home",
		icon=":material/home:"
	),
	st.Page(
		"keynote.py",
		title="Keynote Speakers",
		icon=":material/podium:"
	),
	st.Page(
		"program.py",
		title="Program Schedule",
		icon=":material/calendar_clock:"
	),
	st.Page(
		"layouts.py",
		title="Layouts",
		icon=":material/dashboard:"
	),
]

page = st.navigation(pages)
page.run()

with st.sidebar.container(height=310):
	with st.expander("Announcements",expanded=True,icon=":material/release_alert:"):
		st.write("No new announcements.")
#	if page.title == "Widgets":
#		widgets_card()
#	elif page.title == "Data":
#		dataframe_card()
#	elif page.title == "Layouts":
#		layouts_card()
#	else:
#		st.page_link("home.py", label="Home", icon=":material/home:")
#		st.write("Welcome to the home page!")
#		st.write(
#			"Select a page from above. This sidebar thumbnail shows a subset of "
#			"elements from each page so you can see the sidebar theme."
#		)

st.sidebar.caption(
	"This app uses the [Anthropic](https://docs.anthropic.com/en/home)-inspired light theme, [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) "
	"and [Space Mono](https://fonts.google.com/specimen/Space+Mono) fonts."
)
