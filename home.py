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

st.page_link("widgets.py", label="Page link (this page)", icon=":material/my_location:")
	#st.page_link("text.py", label="Page link (next page)", icon=":material/skip_next:")

cols = st.columns(3)
with cols[0]:
	st.page_link("widgets.py", label="The Widgets", icon=":material/my_location:")
with cols[1]:
	st.page_link("data.py", label="Data Table", icon=":material/skip_next:")
with cols[3]:
	st.page_link("layouts.py", label="Layouts", icon=":material/info:")
		
