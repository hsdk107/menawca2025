import streamlit as st
#from cards import (
#	widgets_card,
#	dataframe_card,
#	layouts_card
#)

st.title("MENAWCA 2025")
st.header("Co-creation with AI: Navigating New Horizons in Writing and Learning")

st.write("[MENAWCA](https://menawca.com/)'s 9th biennial conference is a platform for instructors, tutors, peer tutors, center directors, researchers and other professionals supporting student writers in the MENA region, to share innovative practices and research.")
st.write("This year's conference is hosted at [New York University Abu Dhabi](https://nyuad.nyu.edu/en/) from **10 to 12 October, 2025**.")

st.markdown('''
	Writing centers and programs focus on the writer, encouraging agency, empowerment, 
	and self-actualization through developing not only composition but also linguistic skills. 
	Traditionally, this collaboration exists as a relationship between the writer and the reader/tutor/instructor; 
	however, as generative AI (GenAI) becomes increasingly present and pervasive in composition, 
	students are turning to it for support. While some are engaging with GenAI creatively and critically, 
	many writers often rely on these tools to generate text. As such, writing centers 
	and writing programs are now at a crossroads of praxis, determining when, where, 
	and to what extent GenAI should be part of composition moving forward.\n\n 
	These considerations add to the existing complexities and nuances of academic writing, especially in the MENA region. 
	Where it is essential to consider the ways in which writers can continue to develop their own voices, 
	it is also becoming necessary to factor in GenAI. 
	As practitioners, we can discuss methods and share stories to figure out how to use GenAI as a tool, 
	moving toward co-creation rather than dependence.''')

col0, col1, col2 = st.columns(3, border=True)

with col0:
	st.page_link("keynote.py", label="Keynote Speakers", icon=":material/podium:")
with col1:
	st.page_link("program.py", label="Program Schedule", icon=":material/calendar_clock:")
with col2:
	st.page_link("abstracts.py", label="Speaker Abstracts", icon=":material/article_person:")

with st.expander("Announcements",expanded=True,icon=":material/release_alert:"):
	st.write("No new announcements.")
		
