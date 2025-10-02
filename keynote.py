import streamlit as st

st.header("Keynote Speakers")

st.write("**Annette Vee** ***(Keynote Speaker)*** is Associate Professor of English at University of Pittsburgh, where she recently served six years as the Director of Composition.")
st.markdown('''
At Pitt, she’s facilitated research groups and teaching circles on AI,  an AI across the Disciplines program and advised the CIO on AI policy; 
outside of Pitt, she gives workshops, keynotes, and advice related to AI to faculty, students, and higher ed administrators. 
Her research is generally at the intersection of writing and computation and often includes pedagogy. 
Her work includes: *Coding Literacy: How Computer Programming is Changing Writing* (MIT Press, 2017);
[TextGenEd: Teaching with Text Generation Technologies](https://wac.colostate.edu/repository/collections/textgened/) (WAC Clearinghouse, 2023, 
with [updates in 20024 and 2025](https://wac.colostate.edu/repository/collections/continuing-experiments/)); 
Substacks [AI & How We Teach Writing](https://aiandhowweteach.substack.com/) and [Computation & Writing](https://annettevee.substack.com/). 
With Marc Watkins and Derek Bruff, she is writing [The Norton Guide to AI-Aware Teaching](https://seagull.wwnorton.com/aiaware/guide), 
due out in Fall 2026. Her research monograph in progress, *Androids, Spirits and Chatbots*, 
examines why and how humans have sought to automate writing across history.''')
with st.expander("Title: AI Awareness, Exploration, and Responsibility",expanded=True):
	st.markdown('''
	AI is everywhere, and the values embedded in its technology don't necessarily align with the values of writing pedagogy. 
	The quick and easy answers of AI can undermine the deliberative conversations about process in the writing center. 
	How can we guide students towards productive, co-creative uses of AI that don't sacrifice their learning, development, and thinking? 
	This challenge is particularly complex in the MENA region, where academic writing already navigates multiple linguistic and cultural contexts. 
	This talk offers a path forward for writing teachers through three interconnected approaches: 
	developing AI-awareness by learning how students actually use AI; fostering guided exploration of AI that preserves space for learning; 
	and emphasizing our responsibilities to each other when we write. Drawing on emerging practices from writing teachers, 
	I'll share specific strategies for helping students engage with AI as a collaborative partner. 
	Rather than viewing AI as a threat, we can reframe it as an opportunity to revisit our practices and deepen our commitment to empowering writers.''')
st.divider()

st.write("**Maria Eleftheriou** ***(Regional Speaker)*** is an Assistant Professor of English at the American University of Sharjah, where she directs the Writing Center and oversees its peer tutor training program.")
st.markdown('''
She  teaches undergraduate courses in academic writing and research and has also taught in the MATESOL program at the graduate level.
Her scholarship explores writing center pedagogy, multilingual tutoring, online writing instruction, and the role of AI in academic writing. 
Her publications include work in TESOL International Journal, Contemporary Educational Technology, WAC Clearinghouse, and Palgrave Macmillan, 
with forthcoming articles in The Educational Forum and the Online Learning Journal. She remains active in MENAWCA and global writing center networks.''')

with st.expander("Title: Reimagining the Writing Center in the Age of Generative AI: A MENA Perspective on Ethics and Agency",expanded=True):
	st.markdown('''
	Generative AI has reshaped the work of writing centers and created urgent questions about authorship, integrity, and student voice. 
	At the American University of Sharjah Writing Center, peer tutors began to encounter AI-generated drafts in 2022. 
	Some students disclosed their use of AI while others concealed it, and tutors faced dilemmas about whether to confront, revise, 
	or encourage students to replace AI-produced sections with their own writing. These encounters reveal the need for guidance rooted 
	not only in policy but also in pedagogy.''')
	st.markdown('''
	This keynote examines how writing centers can respond by emphasizing ethics, student agency, and the multilingual realities of the MENA region. 
	Drawing on findings from tutor focus groups and a follow-up study, I will show how tutors respond in practice. 
	They invite disclosure, move suspicion toward curiosity, and use AI as a tool for brainstorming and revision alongside students. 
	Recent scholarship supports these practices and positions tutors as mediators and innovators in AI-era writing instruction.''')
	st.markdown('''
	The keynote invites a regional dialogue on how MENA writing centers can adapt technology while preserving the human connection that 
	empowers students to think, create, and write with confidence.''')
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
