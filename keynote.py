import streamlit as st

st.header("Keynote Speakers")

st.link_button("Link button", url="https://streamlit.io", icon=":material/open_in_new:")
	
cols = st.columns([1,3])
with cols[0]:
  st.subheader("Annette Vee")
  st.markdown("*Keynote Speaker*")
with cols[1].container(border=True):
    st.markdown('''
    Annette Vee is Associate Professor of English at University of Pittsburgh, where she recently served six years as the Director of Composition. 
    At Pitt, she’s facilitated research groups and teaching circles on AI,  an AI across the Disciplines program and advised the CIO on AI policy; 
    outside of Pitt, she gives workshops, keynotes, and advice related to AI to faculty, students, and higher ed administrators. 
    Her research is generally at the intersection of writing and computation and often includes pedagogy. 
    Her work includes: *Coding Literacy: How Computer Programming is Changing Writing* (MIT Press, 2017);
    [TextGenEd: Teaching with Text Generation Technologies](https://wac.colostate.edu/repository/collections/textgened/) (WAC Clearinghouse, 2023, 
    with [updates in 20024 and 2025](https://wac.colostate.edu/repository/collections/continuing-experiments/)); 
    Substacks [AI & How We Teach Writing](https://aiandhowweteach.substack.com/) and [Computation & Writing](https://annettevee.substack.com/). 
    With Marc Watkins and Derek Bruff, she is writing [The Norton Guide to AI-Aware Teaching](https://seagull.wwnorton.com/aiaware/guide), 
    due out in Fall 2026. Her research monograph in progress, *Androids, Spirits and Chatbots*, examines why and how humans have sought to automate writing across history.
    ''')
  
st.divider()

cols = st.columns([1,3])
with cols[0]:
  st.subheader("Maria Eleftheriou")
  st.markdown("*Regional Speaker*")
with cols[1].container(border=True):
    st.markdown('''
    Maria Eleftheriou is an Assistant Professor of English at the American University of Sharjah, where she directs the Writing Center and oversees its peer tutor training program. 
    She  teaches undergraduate courses in academic writing and research and has also taught in the MATESOL program at the graduate level. 
    Her scholarship explores writing center pedagogy, multilingual tutoring, online writing instruction, and the role of AI in academic writing. 
    Her publications include work in TESOL International Journal, Contemporary Educational Technology, WAC Clearinghouse, and Palgrave Macmillan, 
    with forthcoming articles in The Educational Forum and the Online Learning Journal. She remains active in MENAWCA and global writing center networks.
    ''')

st.divider()

cols = st.columns([1,3])
with cols[0]:
  st.subheader("Marion Wrenn")
  st.markdown("*Local Speaker*")
with cols[1].container(border=True):
    st.markdown('''
    Marion Wrenn, PhD, is a poet, essayist, and the Executive Director of Writing at NYUAD, where she helped found the Writing Program and the Writing Center. 
    She has taught writing at NYU NY, Princeton University, and Parsons School of Design in her 30-year career in the field of Writing Studies. 
    Her research moves across creative writing, journalism history, and the study of media and popular culture. She co-edits *The Women’s Review of Books*, newly launched at NYUAD, 
    as well as the literary magazine *Painted Bride Quarterly*, for which she co-hosts and co-produces the literary podcast *The Slush Pile*.
    ''')
