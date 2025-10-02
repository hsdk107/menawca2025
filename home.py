import streamlit as st
from cards import (
	widgets_card,
	dataframe_card,
	layouts_card
)

st.title("MENAWCA 2025")
st.header("Co-creation with AI: Navigating New Horizons in Writing and Learning")


st.markdown('''
	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sed elit sed dui pulvinar tincidunt.
	Integer consequat turpis sit amet orci ullamcorper consequat. Duis volutpat sodales volutpat. 
	Morbi mattis metus at diam tempor efficitur vitae et purus. Ut sit amet justo a mauris vulputate auctor. 
	Duis hendrerit aliquet leo. Proin ut dui eget diam aliquet aliquet. Sed elementum euismod nibh at posuere. 
	Mauris malesuada tortor et congue interdum. Donec pulvinar tortor commodo tristique volutpat.''')

with st.expander("Announcements",expanded=False,icon=":material/release_alert:"):
	st.write("No new announcements.")
cols = st.columns(2)
with cols[0].container(height=310):
	widgets_card()
with cols[0].container(height=310):
	dataframe_card()
with cols[1].container(height=310):
	layouts_card()
