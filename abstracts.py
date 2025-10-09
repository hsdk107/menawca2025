import streamlit as st

st.header("Speakers and Abstracts")
list1, list2, list3, list4 = st.tabs(["**Presentations**", "**Roundtables**", "**Workshops**","**Short-Form Presentations**"])

# **************************************************************
# ********************* PRESENTATIONS **************************
# **************************************************************
with list1:
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
  
 with st.expander("**Coaching in Writing Centers: Hype or Game-Changer?**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Maimuna Aghliw"):
    st.markdown('''
    Maimuna Aghliw is a Libyan Canadian based in Qatar. She holds a Master of Arts in Applied Linguistics and Discourse Studies from Carleton University in Ottawa, Canada, and has over 10 years of English teaching experience in Libya, Canada, and Qatar. She currently works as a Teaching Assistant at Qatar University’s Success Zone, tutoring students in the Foundation Program’s Department of English. In addition to publishing articles with Al Jazeera, her academic interests include sociolinguistics, learner motivation, and critical thinking.''')
  with col1:
   st.write(" ")
  with col2:
   st.write(" ")
  st.markdown('''
  Nowadays, it seems like everything is “coached”—athletes, executives and now even writing center specialists. But what does coaching actually mean in an academic setting? A team of writing specialists from Qatar University’s English Foundation Program recently completed an intensive coaching training program. In this session, we will explore some of the coaching strategies that may enhance writing center pedagogy. Participants will have the opportunity to try out practical coaching techniques that can be applied in tutoring sessions. Additionally, the presenter will share insights on whether coaching tool have successfully improved interactions with students and colleagues in her daily operations. The session will conclude with an open discussion and Q & A, inviting attendees to reflect on the role of coaching in writing center practices.''')
 
 with st.expander("**Does Authenticity in Writing Matter?**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Tatiana Golechkova"):
    st.markdown('''
    Tatiana Golechkova is an EFL teacher and teacher trainer. She is Assistant Professor at the Department of Humanities and Languages, New Economic School, Moscow, Russia. She holds a PhD in Cognitive Linguistics and full Cambridge DELTA. She has broad experience in teaching English for Academic Purposes, Business English, Soft Skills in English to a range of students and academics. Her areas of special interest are strategies for effective communication, genre features of English texts and developing learner autonomy. She has presented and run workshops at several national and international conferences, including NATE, BKC TT, IATEFL, BALEAP and MISIS ESP conference.''')
  with col1:
   st.write(" ")
  with col2:
   st.write(" ")
  st.markdown('''
  In this talk, we will discuss what constitutes an authentic writing style as opposed to formulaic and standardized. We will compare and contrast authentic student-produced and AI-generated texts in order to single out key language features that account for the differences. It is these linguistic differences that usually give away AI-generated writing by making it sound formulaic, “too polished”, and therefore lacking in voice and authenticity. We will compare these features with students’ views based on the findings of a survey on students’ perceptions of quality writing. The similarities and differences in features and perceptions can inform our classroom practices and policies, as well as become a starting point for a conversation with our students about the value of an authentic voice in writing.''')
 
 
 with st.expander("**Helping Students Choose Tools at AI's Jagged Edge**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Kate Koppy"):
    st.markdown('''
    Kate Koppy is the Director of the Writing and Communications Center and an Assistant Professor of English at the New Economic School in Moscow. Her research focuses on the intersection of narrative and community. Specifically, she studies the ways in which the stories we tell foster and maintain individual and community identities. Her current research explores student agency and its interaction with generative AI and plagiarism in "Exploring Generative AI in the Writing Classroom and the Writing Center” (Journal für Schreiberwissenschaft, Vol. 26) and an in-progress article titled "Orientation and Authority in the First-Year Writing Classroom." She holds a Ph.D. in Comparative Literature from Purdue University. She has also written extensively about fairy tales.''')
  with col1:
   st.write(" ")
  with col2:
   st.write(" ")
  st.markdown('''
  Student writers, especially those working in foreign languages, tend to cede authority to external tools—websites, AI chatbots, library books, paper mills--because of the disorientation they experience in higher education. Using Stegmaier’s (2019) theory of orientation and Bartholomae's (1986) idea of students “inventing the university”, this paper first theorizes the adjustments students need to make as they move from novice to proficient writers, a process which happens in the communities shaped by their general education classes, in their fields of study, and in the broader scholarly conversation. During this transition, professors and tutors can foster student agency by bringing generative AI and other digital tools into the classroom. This presentation will conclude with some models for using cooperative learning to explore AI's jagged frontier in structured classroom activities followed by metacognitive reflection.''')
 
 
 with st.expander("**On Shame and Pedagogy in an AI-Suffused World**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Mitchell Atkinson III"):
    st.markdown('''
    Mitchell Atkinson teaches the construction of academic and philosophical texts at the undergraduate and graduate levels, helping young researchers read across discursive divisions. He is an instructor and organizer for the genetic phenomenology network and works periodically with the Husserl Archive. He also has several years of experience tutoring language learners, especially young people writing in their second language. In his work, Alterity and the Flint Water Crisis, Atkinson returned to his home city to understand the lived experience of the residents of Flint and the ways in which the crisis has informed their expectations for the future. This required a new analysis of the phenomenology of social invisibility as partially constituting the contemporary exercise of power. Atkinson is also a writer of fiction and a moderately skilled manipulator of the electric fretted bass guitar.''')
  with col1:
   st.write(" ")
  with col2:
   st.write(" ")
  st.markdown('''
  The following paper attempts to involve three until now disparate lines in my research. The first is the phenomenology of emotional experience. The second is internalized forms of marginalization (self-othering). The third is writing pedagogy. Taking examples from my own work as a teacher of writing, I attempt to analyze the tendency among some students to “over-use” digital tools of all kinds to “polish” the life, and often the meaning content, out of their writing. A phenomenology of shame can alert us to one of the most pressing dangers faced by educators—especially in the humanities—today. Shame, as Husserlian phenomenology can show us, is a self-directed axiological emotion which takes as its object not the act but the person. If the aim of pedagogical work is to enrich the person, to give the person the intellectual, social, and cultural tools concomitant with a full and elevated adult life, then combatting and preempting certain forms of shame experience should be central to the teacher’s work. The flight into digitally-mediated experience, into chatbots and ersatz online worlds, can be partially motivated by a constituted self-valuation which prevents the subject (the student) from expecting certain forms of achievement. This recoiling from expectations relative to growth and personal development is anti-pedagogical. The acts which contribute to it form an antipedagogy. The ways in which AI-mediated experiences contribute to such recoiling should be urgently studied. I offer the structure of play experience as a form of mediation which may encourage self-transvaluation for some students in some cases. ''')
 
 
 with st.expander("**Principles and Practices for Teaching Critical AI Literacy**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("J Palmeri"):
    st.markdown('''
    J Palmeri is Professor of English and Director of the Writing Program at Georgetown University in Washington, DC. Palmeri has published two books about the technologically-mediated history of writing and literacy instruction: Remixing Composition: A History of Multimodal Writing Pedagogy (Southern Illinois UP, 2012) and 100 Years of New Media Pedagogy (University of Michigan Press, 2021). As a scholar, Palmeri focuses on the history and theory of writing pedagogy, multimodal rhetorics, and digital humanities. At Georgetown, Palmeri coordinates first-year writing seminars and also supports faculty across the university in integrating writing instruction into their majors and graduate programs.''')
  with col1:
   st.write(" ")
  with col2:
   st.write(" ")
  st.markdown('''
  In this presentation, a writing program director discusses the collaborative development of a statement of 'Principles of Teaching Critical AI Literacy' that has guided our critical engagement with AI technologies in undergraduate writing seminars and writing center tutorials. In particular the presenter share survey data about AI use among first-year students at our U.S.-based university and also detail practical activities and assignments to engage students in critically and ethically using AI to generate ideas, analyze audiences, and conduct research for writing. The presenter will also share examples of our programmatic effort to bring more student voices into the AI conversation in higher education by developing a collaborative class project across multiple sections in which students created original multimedia web content about AI use in writing, learning, and creative arts.''')
 
 
 with st.expander("**Reconsidering the Process Approach to Developing Writing**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Anna Kashcheeva"):
    st.markdown('''
    Anna Kashcheeva is a Senior Instructor at Humanities and Languages Department of the New Economic School. Anna delivers General English and Introduction to College Writing courses. She holds a pedagogical degree and MSc in Educational Management from University of Portsmouth, UK. She previously worked as a full-time teacher trainer and an Assistant Director of Studies at a private language school in Moscow. Being a CELTA and DELTA trainer, Anna also develops and delivers various training and methodological programmes for such educational establishments as Academic Writing Centre at Higher School of Economics, Cambridge English, Language Link, Thimar Teacher Training Centre etc.''')
  with col1:
   st.write(" ")
  with col2:
   st.write(" ")
  st.markdown('''
  Helping learners improve their academic essays using the process approach to developing writing skills is preferable as it promotes creativity and individuality in writing. What is more, many of our learners are keen to be flexible and less dependent on certain styles, clichés and recommended structures. However, as they are trained to rely on model texts and overloaded with home assignments, our learners tend to cut corners by simply copying and pasting AI generated texts. This session is aimed at clarifying some strategies to motivate our learners to shift from the product writing and equip them with useful content, resources and language for their academic essays. We will discuss some reasons, focus on potential pitfalls and look at student generated texts to work out how to help them change their habits and make significant progress.''')
 
 
 with st.expander("**Reflecting on Approaches to First-Year Writing Using Copilot**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Shauna Loej"):
    st.markdown('''
    Shauna Loej is a Writing Specialist and Adjunct Lecturer in First-Year Writing at Northwestern University in Qatar. She began her career in communications before transitioning to education almost a decade ago, finding tutoring and teaching writing a natural fit for her passion for writing. She was honored as the MENAWCA Professional Tutor of the Year in 2021 and has actively contributed to MENAWCA and IWCA conferences. Shauna holds a CELTA and an MA in Communication.''')
  with col1:
   with st.popover("Sahar Mari"):
    st.markdown('''
    Sahar Mari collaborates with faculty to enhance teaching methods and integrate new technologies into curricula. With over a decade of experience in higher education, she is a dedicated learning engineer at Northwestern University in Qatar committed to making education accessible. Sahar is passionate about teaching and learning, and as a lifelong learner, she continually seeks to incorporate new technologies into experiential learning activities. She holds an M.F.A. in Graphic Design and Visual Experience from the Savannah College of Art and Design.''')
  with col2:
   st.write(" ")
  st.markdown('''
  This session presents insights derived from the collaboration between a first-year writing instructor and a learning engineer in incorporating AI tools into writing instruction. It specifically addresses the distinct needs and challenges faced by first-year students at an international branch campus in the MENA region. The session will cover methodologies for partnering with faculty to enhance AI literacy and examine the impact of AI on first-year English courses. We will discuss the strategies employed and provide contextual evidence demonstrating how we fostered critical thinking and promoted the development of healthy writing habits. We invite participants to join us in reflecting, conversing, and gaining collective knowledge about the role of AI in first-year writing instruction.''')
 
 
 with st.expander("**(Re)Shaping the Writing Process with the 6-P Model: A Framework for Individualized AI-Integrated Writing Instruction**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Chase Brame"):
    st.markdown('''
    Chase Brame is an Instructor in the NYUAD Writing Program, where he specializes in academic writing and multilingual writer support. He has taught at institutes of higher education in North America, Europe, and the Middle East. He is currently pursuing an EdD in Curriculum and Instruction at the University of Virginia, where his research focuses on writing pedagogy in the age of AI.''')
  with col1:
   st.write(" ")
  with col2:
   st.write(" ")
  st.markdown('''
  Technological innovations have upended traditional models of writing pedagogy, compelling writing centers to adjust their praxis in response. This presentation proposes that writing centers adopt a consultation framework aligned with the 6-P model – plan, prompt, preview, produce, peer-review, and portfolio tracking – to integrate AI tools into individualized writing instruction. Drawing on Selber’s (2004) multiliteracies framework of functional, critical, and rhetorical literacies, this session demonstrates how each stage of the 6-P model offers the potential for targeted AI-literacy instruction. Additionally, the presentation highlights how an incremental, AI-conscious consultation approach can promote critical thinking, purposefulness, thoughtful design, and authentic authorship over mere promptsmanship – foundational goals in writing instruction. The session concludes by showcasing how the 6-P model can be practically applied in writing center consultations to meet diverse student needs, support writers at any stage, and offer a flexible approach to ethically integrating generative AI tools in individualized writing instruction.''')
 
 
 with st.expander("**Strategies to Enhance Student Engagement with the Writing Center**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Muna Al-Badaai"):
    st.markdown('''
    Muna Al-Badaai is an assistant professor and the coordinator of the Student Academic Support Unit at Sohar University. She is interested particularly in the Writing Centers and the academic support centers in general. Dr. Al-Badaai participated in the Student Writing: Innovations and Transformations Symposium at UAEU in 2018 and attended MENAWCA 2021 and 2023 Conferences.''')
  with col1:
   with st.popover("Nawal Al Amri"):
    st.markdown('''
    Nawal Al Amri is an administrative officer at Student Academic Support Unit in Sohar University. She graduated from the same University in 2024. Ms. Al-Amri has been interested in peer tutoring since she was a BA student.''')
  with col2:
   st.write(" ")
  st.markdown('''
  Student Academic Support Unit is the designated entity at Sohar University under which the Tutorial Center and the Writing Center operate. Student engagement with the Tutorial Center’s services has been significantly higher compared with those of the Writing Center. To investigate the reasons and increase participation, the researchers conducted a questionnaire in May 2025. They found out that the main reason was that majority of participants were unaware about the Writing Center and its services. Accordingly, the researchers set an action plan including; a) recording a promotional video and b) modifying the currently used strategies to be more interactive, like hand-on workshops, writing games and competitions, and AI tools integration. The researchers have started a pilot study implemented with General Foundation Program students. It will continue for a month. This presentation discusses the impact of the newly implemented strategies on student participation.''')
 
 
 with st.expander("**Students' Engagement with a Specialized AI Research Assistant Tool**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Besma Allagui"):
    st.markdown('''
    Dr. Basma Allagui is an Assistant Professor at Rabdan Academy in Abu Dhabi. She holds a PhD in Applied Linguistics with a minor in teaching academic writing and research. She has developed and taught a considerable number of face-to-face and distance learning courses and modules. She is a member of the Middle East-North Africa Writing Centers Alliance (MENAWCA). She acted as a research coordinator at Rabdan Academy in 2020-2021. She served as an International referee at the First International Student Competition in Smart Education and e-Learning (SEEL 2019).''')
  with col1:
   st.write(" ")
  with col2:
   st.write(" ")
  st.markdown('''
  Although many are concerned about students using general-purpose Artificial Intelligence (AI) tools like ChatGPT to cheat on exams and assignments, specialized research assistant tools like Elicit can be powerful tools to improve efficiency, perform repetitive tasks, and assist with research. This study examines undergraduate students’ prior experiences of AI use in academic research and how they used Elicit to complete a literature review assignment. Before interacting with the tool, a survey was administered to 50 participants to examine familiarity with AI tools for academic research writing, frequency of using AI tools in academic research writing, comfort in integrating AI-generated content into academic research writing, understanding of the capabilities and limitations of AI tools in academic research writing, and awareness of the ethical considerations surrounding the use of AI tools in academic research writing. After interacting with the research assistant, a stimulated recall protocol and an interview with 8 participants documented students’ engagement at the cognitive, behavioural, and affective levels. Survey responses suggested a diverse range of prior experiences regarding the use of AI in academic research writing. Qualitative data from the stimulated recall protocols and interviews demonstrated that interacting with the AI research assistant can be useful for completing the literature review assignment despite moderate and limited engagement.''')
 
 
 with st.expander("**Students' Perception on GenAI in College Writing**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Nattaporn Luangpipat"):
    st.markdown('''
    Nattaporn Luangpipat is an assistant professor in residence in the Liberal Arts Program. She received her PhD in English (Composition and Rhetoric) from the University of Wisconsin-Madison. Her research interests encompass intergenerational literacies, composition pedagogy, writing and well-being, multimodal writing, and second/foreign language acquisition. Her current work investigates the impact of government language policies on Chinese literacy across three generations of Thai Chinese families in Thailand, focusing particularly on how they have navigated linguistic suppression and how these experiences have shaped their language beliefs and practices. Prior to joining Northwestern University in Qatar, Nattaporn was a journalist and English instructor in Thailand, and served as a writing instructor in the English Department and the Writing Center at the University of Wisconsin-Madison.''')
  with col1:
   st.write(" ")
  with col2:
   st.write(" ")
  st.markdown('''
  This presentation highlights student reflections on their use of Generative AI (GenAI) in writing. Students respond to a journal prompt about when they started using AI, how they use it, why they use it, and their thoughts on its pros and cons. The reflections reveal students' perceptions and engagement in co-creation with AI, challenging the boundaries of this co-creation and emphasizing the need for critical AI literacy among college students. The students’ journals demonstrate thoughts and practices influenced by language ideology, the preference for standardized academic language, and educational motivations that prioritize grades over learning. These reflections provide a nuanced understanding of students' experiences and perspectives on GenAI, helping writing instructors better address students' needs and concerns, and potentially fostering more effective and relevant conversations about AI in the classroom.''')
 
 
 with st.expander("**Students' Perspectives on Hybrid AI-Human Peer Review**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Neslihan Bilikozen"):
    st.markdown('''
    Neslihan Bilikozen is an Assistant Professor in the Department of English at the American University of Sharjah. She holds a Doctorate in Education from the University of Exeter and an MA in English Language Teaching from Bogazici University and Georgia State University. At AUS, she teaches undergraduate and graduate courses, supervises MA theses, and mentors student-teachers in their research and professional development. Her research focuses on critical English for Academic Purposes (EAP), with particular attention to the interrelations of academic literacy and identity, as well as critical AI literacy in English-medium contexts.''')
  with col1:
   with st.popover("Hoda Nada"):
    st.markdown('''
    Hoda Nada is a Research and Teaching Assistant at the American University of Sharjah, where she supports instruction in English language teaching and conducts research on the integration of artificial intelligence in higher education. With a background in English literature, translation, and TESOL, and a CELTA certification from Cambridge English, she looks into combining rigorous with practical teaching experience to explore how technology can enhance language learning and student engagement.''')
  with col2:
   st.write(" ")
  st.markdown('''
  This action research study, conducted in three sections of an academic writing course at an American university in the UAE, evaluated a hybrid peer-review model combining traditional student feedback with AI-generated feedback via ChatGPT. Students first conducted rubric-based peer reviews on a causal analysis essay, followed by a lab session where they prompted ChatGPT to provide feedback using the same rubric. A survey and reflection questions compared the utility of human and AI feedback. Results showed a preference for human feedback’s nuanced, context-specific insights, though students valued AI’s speed and grammatical precision, especially in combination with peer input. These findings suggest that a hybrid peer-review model optimizes feedback quality and supports revision. The presentation explores pedagogical implications, emphasizing how AI can complement human feedback in writing instruction, and offers strategies for implementing hybrid peer review in diverse classrooms.''')
  
 with st.expander("**Teaching STEM Students to Write with and Without AI**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Sana Chakroun"):
    st.markdown('''
    Dr. Sana Chakroun is a lecturer in Academic Communication at the University of Doha for Science and Technology and holds a Ph.D. in Applied Linguistics. She has taught a wide range of modules—including Composition, ESP, Soft Skills, Business English, and Research Methods—in Qatar, Germany, and Tunisia. Her research explores political discourse, UN resolution rhetoric, academic writing pedagogy, AI integration in higher education, and the challenges multilingual learners face in academic and research communication. She has led workshops on qualitative methods, thematic analysis, and NVivo. Dr. Sana Chakroun has held academic posts at Lusail University, Oryx Universal College, and Philipps University Marburg.''')
  with col1:
   with st.popover("Christopher Hill"):
    st.markdown('''
    Christopher Hill is Head of the Department of Communications & Humanities at the University of Doha for Science & Technology. With 20 years of experience teaching academic communication and research writing, his work focuses on experiential learning, learning transfer, and student–faculty partnerships. He has published on ethical reasoning, academic integrity, and AI-enhanced pedagogy, and is active in advancing the Scholarship of Teaching and Learning (SoTL) across the MENA region.''')
  with col2:
   st.write(" ")
  st.markdown('''
  This presentation outlines a dual-approach writing model developed for an academic communication report writing course for STEM students at the University of Doha for Science and Technology. The redesign responded to increased reliance on Generative AI (GenAI) tools and declining student engagement with academic writing. Students complete two key assignments: a timed, in-class report using pre-approved sources, and a partially AI-assisted report paired with a written reflection and short presentation. The in-class task reinforces critical reading and synthesis in a supervised environment. The AI-supported report includes guided instruction in prompt design, source evaluation, and ethical use. Rather than taking a position for or against AI, this model treats GenAI as a space of negotiation—where students practise both independent composition and co-creation. It offers a pragmatic response to evolving writing practices in the MENA STEM context, helping students build dual literacy with and without AI.''')

 with st.expander("**Text-to-Speech or Speech-to-Text? Preserving Voice and Agency in AI Co-Creation**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Sweta Kumari"):
    st.markdown('''
    Sweta Kumari is a Writing Instructor at NYU Abu Dhabi for the past 8 years. She holds a BA in Politics, Philosophy and Economics (PPE) and a Post Graduate Diploma in Social Sciences and Liberal Studies. Her recent adventure is the Master’s Degree program she enrolled in this semester in Applied Sociological Research at the Sorbonne University, Abu Dhabi. Her academic interests are in writing studies, gender and women’s studies, linguistics, aging and social gerontology. She co-led a research project under the Writing, Languages and Pedagogy Research Kitchen titled “Perceptions and Positions of Postcolonial Englishes”. One of the outcomes of this ongoing research project is a podcast titled English or Englishes? that can be accessed on Spotify.''')
  with col1:
   with st.popover("Aieshah Arif"):
    st.markdown('''
    Aieshah Arif is serving as a Writing Instructor at NYU Abu Dhabi, with a background in journalism, public relations and marketing. She has worked closely with students and professionals on academic and personal writing instruction for over 10 years at Yale-NUS College, the National University of Singapore, and presently NYU Abu Dhabi. Her professional experience and interest in AI, multilingualism and pedagogy have led to co-heading the research project, “Perceptions and Positions of Postcolonial Englishes” (PPPE). She is also one of the founders, editors and hosts of the podcast English or Englishes? on Spotify.''')
  with col2:
   st.write(" ")
  st.markdown('''
  In the present context where Generative Artificial Intelligence and its integration in student writing are so rapidly evolving, concerns about the loss of voice and individuality have similarly evolved into concerns about the loss of agency in critical thinking. How do we increase and evaluate levels of meaningful engagement with learning? Writing Centers, as spaces of communication and embodied learning, serve as an ideal platform for re-examining how the physical voice can be used to develop the academic voice. In this presentation, we apply the framework of World Englishes to understand motives of AI use, and share reflections, practical strategies and tools highlighting how consideration of multiple Englishes can drive student engagement and agency. Participants will also be invited to share their perspectives, particularly in relation to the multilingual realities of MENA classrooms. This session is an extension of ongoing research by NYU Abu Dhabi’s Writing, Language and Pedagogy Research Kitchen, under the project Perceptions and Positions of Postcolonial Englishes.''')
  
 with st.expander("**The GenAI Edge: Transforming Writing Center Consultations**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Rana R. Abuhassan"):
    st.markdown('''
    Rana R. Abuhassan is Director of the Writing and Speaking Center at King Saud University and a newly appointed Transformation Ambassador through the OUR KSU preparation program. She has seven years of experience as a consultant and administrator at the Center for Writing in English. She participated in the Transformation Hackathon and was equipped with practical AI tools.''')
  with col1:
   st.write(" ")
  with col2:
   st.write(" ")
  st.markdown('''
  Generative AI (GenAI) offers writing centers new opportunities to enrich one-on-one writing sessions by fostering creativity and critical thinking. Moving beyond simple text generation, GenAI can serve as a collaborative tool to develop ideas, refine arguments, and explore diverse perspectives. Writing tutors can leverage these capabilities to guide students in enhancing their rhetorical effectiveness, analyzing their work critically, and considering multiple viewpoints. By transforming writing consultations into dynamic, creative, and intellectually stimulating experiences, GenAI positions itself as a partner in developing not just better writing, but more thoughtful writers.''')

 with st.expander("**The Right of Refusal: Embodying Writing Center Expertise in the Age of AI**",expanded=True):
  col0,col1,col2 = st.columns(3)
  with col0:
   with st.popover("Kelly Wilson"):
    st.markdown('''
    Kelly Wilson is in her seventh year as Writing Center Manager at Northwestern University in Qatar. She has 15 years’ experience in writing center work in Doha. She recently co-authored an article on critical peer mentoring and is working on a teacher-action research project on freewriting in L2 first year writing classrooms.''')
  with col1:
   st.write(" ")
  with col2:
   st.write(" ")
  st.markdown('''
  In Refusing Generative AI in Writing Studies, Sano-Franchini, et. al. propose refusal as “a disciplinary and principled response” to GenAI (2024, para. 1). Refusal as a stance toward these technologies should be expanded to include writing centers and first-year writing classrooms in the MENA region. In this presentation, we situate refusal as a viable and reasonable option for writing center administrators in addressing the frustrations that have arisen from students’ reliance on GenAI tools rather than their seeking out customized and contextualized writing center expertise. We will share the highs and lows of our ongoing journey, including the existential dilemma of being expected to respond and give feedback on what we suspect is AI generated texts. In reclaiming the writing center and the first-year writing classroom as GenAI-free spaces, we hope to recover the relationships lost between students, tutors, and teachers - a cornerstone of writing center pedagogy.''')

 with st.expander("**Writing with AI: Saudi Voices, Shared Dilemmas**",expanded=True):
  col0,col1,col2 = st.columns([3,3,2],gap="small")
  with col0:
   with st.popover("Georgios Kormpas"):
    st.markdown('''
    Georgios Kormpas is a faculty member at the Humanities Department, at the Arts and Sciences Deanship at Al Yamamah University, Saudi Arabia, and a PhD candidate at Lancaster University (UK). His research focuses on English Language Teacher Associations, professional development, and the ethical use of AI in education. He has published several volumes with Routledge and Springer on various topics and presented internationally with UNESCO, TESOL, and other organizations. A leader in teaching innovation, curriculum design, and youth empowerment, he integrates AI, SDGs, and digital literacy into higher education and professional practice.''')
  with col1:
   with st.popover("Abdulrahman AlHassun"):
    st.markdown('''
    Abdulrahman Alhassun is a Management Information Systems student at Al Yamamah University. He is a certified trainer and a Toastmasters Humorous Speech Champion, representing his University Club and district at the 2025 Toastmasters International Convention in Philadelphia, USA. Passionate about communication, technology, and leadership, he is also engaged in research on AI in education, exploring how students balance creativity, integrity, and innovation in the age of generative tools.''')
  with col2:
   with st.popover("Joud Hakeem"):
    st.markdown('''
    Joud Hakeem is a Marketing student at Al Yamamah University and a Toastmasters International Speech Champion. She represented her district and university at the 2025 Toastmasters International Convention in Philadelphia, USA, and recently completed an international internship in Spain. Her interests lie at the intersection of marketing, communication, and AI in higher education, with a focus on how young learners navigate trust, originality, and opportunity in the digital era.''')
  st.markdown('''
  As artificial intelligence becomes increasingly integrated into higher education, questions of trust, authorship, and academic integrity have grown more complex. This study—conducted by students under faculty supervision—investigates the extent to which students at a Saudi university rely on AI tools for academic writing, ranging from minor edits to full paper generation. Using mixed methods, the research explores student attitudes toward AI as both a writing aid and a potential source of academic dishonesty. Key themes include perceptions of bias, authenticity, and the repetitive nature of AI-generated content compared to human creativity. The study also examines the specific types of AI platforms students use and how frequently they rely on them. Faculty perspectives on originality, learning outcomes, and ethical implications are compared with student views on convenience and support. The findings aim to inform institutional policies on responsible AI integration while fostering a balanced, ethical approach to innovation in academic writing.''')
  
# **************************************************************
# ********************* ROUNDTABLES ****************************
# **************************************************************

with list2:
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

# **************************************************************
# ********************* WORKSHOPS ******************************
# **************************************************************
with list3:
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

# **************************************************************
# ********************* SHORT-FORM PRESENTATIONS ***************
# **************************************************************
with list4:
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
