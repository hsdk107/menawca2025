import streamlit as st
#from cards import (
#	widgets_card,
#	dataframe_card,
#	layouts_card
#)

st.title("MENAWCA 2025")
st.header("Co-creation with AI: Navigating New Horizons in Writing and Learning")


st.markdown('''
	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sed elit sed dui pulvinar tincidunt.
	Integer consequat turpis sit amet orci ullamcorper consequat. Duis volutpat sodales volutpat. 
	Morbi mattis metus at diam tempor efficitur vitae et purus. Ut sit amet justo a mauris vulputate auctor. 
	Duis hendrerit aliquet leo. Proin ut dui eget diam aliquet aliquet. Sed elementum euismod nibh at posuere. 
	Mauris malesuada tortor et congue interdum. Donec pulvinar tortor commodo tristique volutpat.''')

col0, col1, col2 = st.columns(3, border=True)

with col0:
	st.page_link("keynote.py", label="Keynote Speakers", icon=":material/podium:")
with col1:
	st.page_link("data.py", label="Data Table", icon=":material/skip_next:")
with col2:
	st.page_link("layouts.py", label="Layouts", icon=":material/info:")

with st.expander("Announcements",expanded=True,icon=":material/release_alert:"):
	st.write("No new announcements.")
		
