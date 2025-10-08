import streamlit as st

st.header("Speakers and Abstracts")

with st.expander("**Centering Human Voices in a Co-Creative Approach to Writing with AI**",expanded=True):
 col0,col1,col2 = st.columns(3)
 with col0:
  with st.popover("Dima Yousef"):
   st.markdown('''
   Dima Yousef is a Senior Learning Designer at MBZUAI. She holds an MA in English Literary Research from the University of Leicester and is pursuing a PhD in E-Research and Technology-Enhanced Learning at Lancaster University. Throughout her career, she has specialised in teaching, curriculum design, assessment development, and teacher training, with a strong focus on creating inclusive and meaningful learning experiences. Her research focuses on student engagement and technology-enhanced learning.''')
 with col1:
  with st.popover("Amira El-Soussi"):
   st.markdown('''
   Amira El-Soussi holds an EdD in TESOL from the University of Exeter, UK. She has extensive experience teaching ESL and Academic Writing courses, having previously worked as an English instructor at the American University in Dubai (AUD) and the University of Balamand Dubai (UOBD). Since 2021, she has been teaching Academic Writing and TESOL at the American University of Sharjah (AUS). Her research focuses on TESOL, writing motivation and pedagogy, project-based learning, teacher education, AI in education, and online teaching and learning.''')
 with col2:
  st.write(" ")
 st.markdown('''
 This presentation introduces a flexible framework that shifts assessment from a content-focused approach to a skill-based, process-oriented learning, empowering students to co-create rather than rely on AI tools. The framework promotes writing as a process of inquiry, collaboration, and critical engagement, encouraging students to reflect on their use of AI while developing academic and professional competencies. Through practical examples, we will demonstrate how instructors can design assignments that cultivate transferable skills essential for success in an AI-integrated world. Educators will gain tools to foster meaningful co-creation in writing classrooms that balance innovation with intention.''')

with st.expander("**Chatbots, ESL Writing, Citation, Annotated Bibliography, WAC, Academic Writing**",expanded=True):
 col0,col1,col2 = st.columns(3)
 with col0:
  with st.popover("Inas Y. Mahfouz"):
   st.markdown('''
   Inas Mahfouz is an associate professor of language and linguistics at the American University of Kuwait. She is also chair of the English Department where she teaches a variety of language courses and academic writing. Her current research projects include: (1) meta-discourse markers in academic writing: a cross-cultural study which she started during her fellowship at the Writing center at Dartmouth College in Summer 2017 and (2) the Arab Learner English Corpus (ALEC): a corpus of Freshman writing hosted by the Learner Corpus Association. Teaching second language writing and examining learners' corpora have made her realize multilingual writers bring diverse cultural background to their writing classes which shape how they adopt and apply the guidelines of academic writing.''')
 with col1:
  st.write(" ")
 with col2:
  st.write(" ")
 st.markdown('''
 Did the chatbot get it right?
 The extensive use of chatbots, fueled by their easy accessibility, has transformed instructors' approach to academic writing. This transformation is particularly significant in English Second Language (ESL) writing, where linguistic proficiency poses challenges for students who often struggle to articulate their thoughts and construct meaningful sentences.
 This case study explores how AI can enhance the teaching process. Students enrolled in a second-level college writing course are required to utilize two different chatbots to generate content for various writing tasks. Using rubrics provided by their instructor, students audit the AI-generated content, decide how far it fulfills the requirements of the tasks to determine whether to proceed with a submission, develop, or edit certain sections.
 Students reflect on the process and what they gained and their reflections are analyzed using Geisler and Swarts (2019) frame for qualitative data analysis.''')
 
with st.expander("**Title**",expanded=True):
 col0,col1,col2 = st.columns(3)
 with col0:
  with st.popover("Name1"):
   st.markdown('''
   Bio 1''')
 with col1:
  with st.popover("Name2"):
   st.markdown('''
   Bio 2''')
 with col2:
  st.write(" ")
 st.markdown('''
 Abstract of the presentation.''')
