import streamlit as st


tab1, tab2 = st.tabs(["**Keynote Speakers**", "**Presidential Perspectives**"])

with tab1:
	st.header("Keynote Speakers")
	col0, col1 = st.columns([2,5],gap="small")
	with col0:
		st.image("img/annettevee.png")
	with col1:
		st.write("**Annette Vee** ***(Keynote Speaker)*** is Associate Professor of English at University of Pittsburgh, where she recently served six years as the Director of Composition.")
		st.write("At Pitt, she’s facilitated research groups and teaching circles on AI,  an AI across the Disciplines program and advised the CIO on AI policy; outside of Pitt, she gives workshops, keynotes, and advice related to AI to faculty, students, and higher ed administrators.")
	st.markdown(''' 
	Her research is generally at the intersection of writing and computation and often includes pedagogy. 
	Her work includes: *Coding Literacy: How Computer Programming is Changing Writing* (MIT Press, 2017);
	[TextGenEd: Teaching with Text Generation Technologies](https://wac.colostate.edu/repository/collections/textgened/) (WAC Clearinghouse, 2023, 
	with [updates in 20024 and 2025](https://wac.colostate.edu/repository/collections/continuing-experiments/)); 
	Substacks [AI & How We Teach Writing](https://aiandhowweteach.substack.com/) and [Computation & Writing](https://annettevee.substack.com/). 
	With Marc Watkins and Derek Bruff, she is writing [The Norton Guide to AI-Aware Teaching](https://seagull.wwnorton.com/aiaware/guide), 
	due out in Fall 2026. Her research monograph in progress, *Androids, Spirits and Chatbots*, 
	examines why and how humans have sought to automate writing across history.''')
	with st.expander("AI Awareness, Exploration, and Responsibility",expanded=True):
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
	
	col0, col1 = st.columns([2,5],gap="small")
	with col0:
		st.image("img/mariaeleftheriou.png")
	with col1:
		st.write("**Maria Eleftheriou** ***(Regional Speaker)*** is an Assistant Professor of English at the American University of Sharjah, where she directs the Writing Center and oversees its peer tutor training program.")
		st.write("She  teaches undergraduate courses in academic writing and research and has also taught in the MATESOL program at the graduate level.")
		
	st.markdown('''
	Her scholarship explores writing center pedagogy, multilingual tutoring, online writing instruction, and the role of AI in academic writing. 
	Her publications include work in TESOL International Journal, Contemporary Educational Technology, WAC Clearinghouse, and Palgrave Macmillan, 
	with forthcoming articles in The Educational Forum and the Online Learning Journal. She remains active in MENAWCA and global writing center networks.''')
	
	with st.expander("Reimagining the Writing Center in the Age of Generative AI: A MENA Perspective on Ethics and Agency",expanded=True):
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
	
	col0, col1 = st.columns([2,5],gap="small")
	with col0:
		st.image("img/michaelpazinas.png")
	with col1:
		st.write("**Michael Pazinas** ***(Local Speaker)*** is Acting Director of the Center for Educational Innovation at Zayed University, where he leads initiatives at the intersection of pedagogy, faculty development, and AI.")
		st.write("A Senior Fellow of Advance HE and certified Quality Matters peer reviewer, he has developed programmes on learning integrity, AI-resilient assessment, and faculty development. His current work examines how educators can design for *authentic human learning* in environments shaped by generative AI.")
	st.markdown(''' 
	Michael’s approach combines academic rigour with design thinking, drawing on evidence-based learning strategies and techniques adapted from fields 
	such as UX design. Through **LX.ai**, a faculty development initiative shortlisted for a Times Higher Education award, he has explored methods like 
	persuasive and validation patterns as practical micro-experiments within the design cycle. These approaches give faculty ways to trial, refine, and 
	evaluate learning interventions in practice while keeping the learner’s experience central. Alongside this, he integrates insights on emotion, 
	creativity, and flow, recognising their importance in sustaining motivation and making learning meaningful. His initiatives, including 
	LIFE (Learning Integrity and Faculty Empowerment), position faculty as intentional designers of transformative experiences, where curiosity, 
	struggle, reflection, and dialogue remain protected as the foundations of genuine learning.''')
	with st.expander("Designing for Productive Struggle in Writing",expanded=True):
		st.markdown('''
		This session asks a set of urgent questions: How can we design for authentic human learning? What does authenticity in learning look like today? 
		What makes a learning experience feel meaningful, embodied, and worth engaging in, and how can we design for this in the age of AI?''')
		st.markdown('''
		This talk invites participants to step back and reconsider the foundations of transformative learning. Attention will be placed on curiosity, 
		struggle, reflection, and dialogue as practices that give depth to the learning process. The session will explore how educators can protect 
		space for uncertainty, discovery, and even discomfort—conditions that are often avoided but which remain essential for growth. They will explore 
		how human learning manifests in its public life through composition, argumentation and rhetoric.''')
		st.markdown('''
		By foregrounding these elements, the discussion highlights how intentional design choices can help preserve authenticity in writing. 
		The aim is to equip faculty with perspectives and practices that make learning not only effective but genuinely worth engaging in.''')

with tab2:
	st.header("Presidential Perspectives")
	col1, col2, col3, col4 = st.columns(4, gap="small")
	with col1:
		st.image("img/saharmari.jpg")
		with st.popover("Sahar Mari"):
			st.markdown('''
			Sahar Mari collaborates with faculty to enhance teaching methods and integrate new technologies into curricula. With over a decade of experience in higher education, she is a dedicated learning engineer at Northwestern University in Qatar committed to making education accessible. Sahar is passionate about teaching and learning, and as a lifelong learner, she continually seeks to incorporate new technologies into experiential learning activities. She holds an M.F.A. in Graphic Design and Visual Experience from the Savannah College of Art and Design.''')
	with col2:
		st.image("img/kellywilson.jpg")
		with st.popover("Kelly Wilson"):
			st.markdown('''
			Kelly Wilson is in her seventh year as Writing Center Manager at Northwestern University in Qatar. She has 15 years’ experience in writing center work in Doha. She recently co-authored an article on critical peer mentoring and is working on a teacher-action research project on freewriting in L2 first year writing classrooms.''')
	with col3:
		st.image("img/nicoleabiad.jpg")
		with st.popover("Nicole Abiad"):
			st.markdown('''
			Nicole Abiad is the current President of MENAWCA and the Writing Center Coordinator at Virginia Commonwealth University in Qatar. Since moving to Qatar in 2011, she has worked extensively in writing instruction, English language teaching, and academic support. Nicole has served on the MENAWCA executive board since 2019 and is dedicated to fostering collaboration among writing centers and educators across the region. Nicole is passionate about building communities of practice that connect writing centers across the region and about exploring the role of AI, literacy, and academic integrity in higher education.''')
	with col4:
		st.image("img/ryanmcdonald.jpg")
		with st.popover("Ryan McDonald"):
			st.markdown('''
			Ryan McDonald is a teacher, writer, and ultramarathon enthusiast who has spent the past decade building writing center communities in the Middle East. After earning his BA in English Literature and History and later his Master’s in the Science of Teaching English at the State University of New York, he taught abroad before settling in Muscat, Oman, where he worked for the past eleven years as a course coordinator and director of the writing center at Sultan Qaboos University. He is currently the Director of the Writing Center and Writing Program at AUB Mediterraneo in Paphos, Cyprus. Since 2016 Ryan has been an active board member of the Middle East and North Africa Writing Center Alliance (MENAWCA), serving in roles from President to Treasurer and helping organize conferences, training sessions, and workshops throughout the region. His current research explores the ecology of writing center spaces, the role of generative AI in composition, and how feedback can actually be practical (and not just paperwork).''')
	
	with st.expander("Presidential Perspectives",expanded=True):
		st.markdown('''
		This presidential panel brings together past and present leaders of MENAWCA to reflect on the evolving landscape of writing center work in 
		the region and beyond. In conversation with one another and with the audience, the panelists will consider how shifting contexts — from 
		emerging technologies such as generative AI to questions of co-creation, collaboration, and community — shape our practices and our futures. 
		By engaging both the history of MENAWCA and its role in a rapidly changing educational ecosystem, this session invites participants to think 
		alongside the panelists about the challenges and possibilities ahead for writing centers in the MENA region.''')

