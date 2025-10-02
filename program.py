import streamlit as st

chart_data = st.session_state.chart_data
st.header("Conference Program")

day1, day2, day3 = st.tabs(["**Friday October 10**", "**Saturday, October 11**", "**Sunday, October 12**"])
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ******************* FRIDAY SCHEDULE *******************************
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

with day1:
  st.header("Day 1: Friday October 10, 2025")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("9:00 - 10:00am")
  with col1:
    st.write("**Breakfast & Registration**")
    st.write("Outside Blue Hall, Arts Center (C3)")
    st.write("*Registration will continue past this time if needed at the Library Entrance (C2)*")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("10:00am - 12:00pm")
  with col1:
    st.write("**Opening Ceremony**")
    st.write("Outside Blue Hall, Arts Center (C3)")
  st.markdown("<hr style='width:75%;margin:auto;'>",unsafe_allow_html=True)
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.markdown('<div style="text-align: right;">10:00-10:15am</div>', unsafe_allow_html=True)
  with col1:
    st.write("Awam Amkpa")
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.markdown('<div style="text-align: right;">10:15-11:15am</div>', unsafe_allow_html=True)
  with col1:
    st.write("Keynote Speaker: Annette Vee")
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.markdown('<div style="text-align: right;">11:15-11:45am</div>', unsafe_allow_html=True)
  with col1:
    st.write("Local Speaker: Marion Wrenn")
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.markdown('<div style="text-align: right;">11:45am-12:00pm</div>', unsafe_allow_html=True)
  with col1:
    st.write("Provost's Welcome Address")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("12:00 - 2:30pm")
  with col1:
    st.write("**Lunch and Prayer Break**")
    st.write("Torch Club (D2)")
    st.write("*Prayer Rooms in C2 Ground Floor*")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("2:30 - 5:30pm")
  with col1:
    st.write("**Parallel Sessions:** ***Policy, Voice and Agency***")
    st.write("Campus Center (C2) Level 3, Library, Breakout Rooms")
  st.markdown("<hr style='width:75%;margin:auto;'>",unsafe_allow_html=True)
  with st.expander("Parallel Sessions",expanded=True):
    # *****************************************************************************************************
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write("Room")
    with col1:
      st.write("TBD") #st.error("TBD")
    with col2:
      st.write("TBD") #st.error("TBD")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    # *****************************************************************************************************
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write(" ")
    with col1:
      st.write("**Policy & AI**")
    with col2:
      st.write("**Student Voice, Agency & AI**")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write("2:30-3:10pm")
      #st.markdown('<div style="text-align: right;">2:30-3:10pm</div>', unsafe_allow_html=True)
    with col1:
      st.write("*The Right of Refusal: Embodying Writing Center Expertise in the Age of AI*")
      st.write("Kelly Wilson")
    with col2:
      st.write("*Developing Student Voice Through AI Literacy*")
      st.write("Thuraya Sulaiman")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write("3:15-3:55pm")
      #st.markdown('<div style="text-align: right;">3:15-3:55pm</div>', unsafe_allow_html=True)
    with col1:
      st.write("*Transparent Practices: Acknowledging AI in Academic Assignments* (Roundtable)")
      st.write("Owen Connor & Luleadey Worku")
    with col2:
      st.write("*Helping Students Choose Tools at AI's Jagged Edge*")
      st.write("Kate Koppy")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write("4:00-4:40pm")
      #st.markdown('<div style="text-align: right;">4:00-4:40pm</div>', unsafe_allow_html=True)
    with col1:
      st.write("*Principles and Practices for Teaching Critical AI Literacy*")
      st.write("J. Palmeri")
    with col2:
      st.write("*Text-to-Speech or Speech-to-Text? Preserving Voice and Agency in AI Co-Creation*")
      st.write("Sweta Kumari & Aieshah Arif")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write("4:45-5:25pm")
      #st.markdown('<div style="text-align: right;">4:45-5:25pm</div>', unsafe_allow_html=True)
    with col1:
      st.write(" ")
    with col2:
      st.write("*Writing with AI: Saudi Voices, Shared Dilemmas*")
      st.write("Georgios Kormpas, Abdulrahman AlHassun, & Joud Hakeem")
    
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("5:30 - 6:30pm")
  with col1:
    st.write("**Rest**")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("6:30 - 8:30pm")
  with col1:
    st.write("**Conference Dinner**")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)

  #st.table(chart_data)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ******************* SATURDAY SCHEDULE *******************************
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
with day2:
  st.header("Day 2: Saturday October 11 2025")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("9:00 - 9:30am")
  with col1:
    st.write("**Breakfast & Registration**")
    st.write("Outside Blue Hall, Arts Center (C3)")
    st.write("*Registration will continue past this time if needed at the Library Entrance (C2)*")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("9:30 - 10:30am")
  with col1:
    st.write("**Regional Speaker: Maria Eleftheriou**")
    st.write("Outside Blue Hall, Arts Center (C3)")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("10:45am - 1:00pm")
  with col1:
    st.write("**Parallel Sessions:** ***Perceptions and Motivation***")
    st.write("Campus Center (C2) Level 3, Library, Breakout Rooms")
  st.markdown("<hr style='width:75%;margin:auto;'>",unsafe_allow_html=True)
  with st.expander("Parallel Sessions",expanded=True):
    # *****************************************************************************************************
    col0, col1, col2, col3 = st.columns([1,2,2,2],gap="small")
    with col0:
      st.write("Room")
    with col1:
      st.write("TBD") #st.error("TBD")
    with col2:
      st.write("TBD") #st.error("TBD")
    with col3:
      st.write("TBD") #st.error("TBD")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    # *****************************************************************************************************
    col0, col1, col2, col3 = st.columns([1,2,2,2],gap="small")
    with col0:
      st.write(" ")
    with col1:
      st.write("**Student Motivation & Craft with AI**")
    with col2:
      st.write("**Experiences with AI**")
    with col3:
      st.write("**Perceptions of AI**")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2, col3 = st.columns([1,2,2,2],gap="small")
    with col0:
      st.write("10:45-11:25am")
    with col1:
      st.write("*Reshaping Stakeholder Collaboration for Student Success in the Age of AI* (Roundtable)")
      st.write("Naqaa Abbas & Luleadey Worku")
    with col2:
      st.write("*Centering Human Voices in a Co-Creative Approach to Writing with AI*")
      st.write("Dima Yousef & Amira El-Soussi")
    with col3:
      st.write("*Students’ Perception on GenAI in College Writing*")
      st.write("Nattaporn Luangpipat")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2, col3 = st.columns([1,2,2,2],gap="small")
    with col0:
      st.write("11:30-12:10pm")
    with col1:
      st.write("*Strategies to Enhance Student Engagement with the Writing Center*")
      st.write("Muna Al Badaai & Nawal Al Amri")
    with col2:
      st.write("*Rewriting the Future: AI and Human Collaboration in Writing Center Pedagogy*")
      st.write("Lara Hamidi")
    with col3:
      st.write("*Does Authenticity in Writing Matter?*")
      st.write("Tatiana Golechkova")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2, col3 = st.columns([1,2,2,2],gap="small")
    with col0:
      st.write("12:15-12:55pm")
    with col1:
      st.write("*On Shame and Pedagogy in an AI-Suffused World*")
      st.write("Mitchell Atkinson III")
    with col2:
      st.write(" ")
    with col3:
      st.write("*Students’ Perspectives on Hybrid AI-Human Peer Review*")
      st.write("Neslihan Bilikozen & Hoda Nada")
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("1:00 - 2:00pm")
  with col1:
    st.write("**Lunch Break**")
    st.write("Library Lobby (C2) 3rd floor")
    st.write("*Prayer Rooms in C2 Ground Floor*")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("2:00 - 5:00pm")
  with col1:
    st.write("**Parallel Sessions:** ***Using AI in Teaching and Learning***")
    st.write("Campus Center (C2) Level 3, Library, Breakout Rooms")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  with st.expander("Parallel Sessions",expanded=True):
    # *****************************************************************************************************
    col0, col1, col2, col3 = st.columns([1,2,2,2],gap="small")
    with col0:
      st.write("Room")
    with col1:
      st.write("TBD")
    with col2:
      st.write("TBD")
    with col3:
      st.write("TBD")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    # *****************************************************************************************************
    col0, col1, col2, col3 = st.columns([1,2,2,2],gap="small")
    with col0:
      st.write("2:00-2:40pm")
    with col1:
      st.write("*Policing GenAI Use: Four Approaches* (Roundtable)")
      st.write("Kate Moore, Gulbahor Amirova, & Liane Jeschull")
    with col2:
      st.write("*The GenAI Edge: Transforming Writing Center Consultations*")
      st.write("Rana R. Abuhassan")
    with col3:
      st.write("*(Re)Shaping the Writing Process with the 6-P Model: A Framework for Individualized AI-Integrated Writing Instruction*")
      st.write("Chase Anthony Brame")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2, col3 = st.columns([1,2,2,2],gap="small")
    with col0:
      st.write("2:45-3:25pm")
    with col1:
      st.write("*Reconsidering the Process Approach to Developing Writing*")
      st.write("Anna Kascheeva")
    with col2:
      st.write("*Coaching in Writing Centers: Hype or Game-Changer?*")
      st.write("Maimuna Aghliw")
    with col3:
      st.write("*Teaching STEM Students to Write with and Without AI*")
      st.write("Christopher Hill & Sana Chakroun")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2, col3 = st.columns([1,2,2,2],gap="small")
    with col0:
      st.write("3:30-4:10pm")
    with col1:
      st.write("*Engaging with GenAI in Scientific Writing: Opportunities and Caveats*")
      st.write("Hind Saddiki")
    with col2:
      st.write("*Chatbots, ESL Writing, Citation, Annotated Bibliography, WAC, Academic Writing*")
      st.write("Inas Y. Mahfouz")
    with col3:
      st.write("*Students’ Engagement with a Specialized AI Research Assistant Tool*")
      st.write("Besma Allagui")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2, col3 = st.columns([1,2,2,2],gap="small")
    with col0:
      st.write("4:15-4:55pm")
    with col1:
      st.write("*Engagement Strategies in Human-Written and AI-Generated Academic Essays: A Corpus-Based Study*")
      st.write("Sharif Alghazo")
    with col2:
      st.write("*Reflecting on Approaches to First-Year Writing Using Copilot*")
      st.write("Shauna Loej & Sahar Mari")
    with col3:
      st.write("(1) *AI in Action: Perspectives from Peer Tutors* (Pecha-Kucha)")
      st.write("Malak Elmallah, Audre Knepp, & Gaya Menon")
      st.write("(2) *Sociolinguistic Sexism and Gender-Unspecified Generative AI: Biased Linguistic Practices* (Pecha-Kucha)")
      st.write("Mariami Akopian")
      st.write("(3) *Voice and Style: A Personal Statement Writing Workshop Experiment* (Pecha-Kucha)")
      st.write("Sheren Saad")
      st.write("(4) *Co-Creating Graphic Novels with AI* (Show & Tell)")
      st.write("Bianca Arkeen & Fahad Rizwan")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("5:00 - 6:00pm")
  with col1:
    st.write("**Closing Ceremony**")
    st.write("Faculty Hub, Library, Level 3, Campus Center (C2)")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ******************* SUNDAY SCHEDULE *******************************
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
with day3:
  st.header("Day 3: Sunday October 12 2025")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("9:00 - 9:30am")
  with col1:
    st.write("**Breakfast & Registration**")
    st.write("Faculty Hub, Library, Level 3, Campus Center (C2)")
    st.write("*Registration will continue past this time if needed at the Library Entrance (C2)*")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("9:30am - 12:00pm")
  with col1:
    st.write("**Parallel Sessions:** ***Workshops***")
    st.write("Campus Center (C2) Level 3, Library, Breakout Rooms")
  st.markdown("<hr style='width:75%;margin:auto;'>",unsafe_allow_html=True)
  with st.expander("Parallel Sessions",expanded=True):
    # *****************************************************************************************************
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write("Room")
    with col1:
      st.write("TBD") #st.error("TBD")
    with col2:
      st.write("TBD") #st.error("TBD")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    # *****************************************************************************************************
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write("9:30-10:25")
    with col1:
      st.write("*Teaching AI-Enhanced Writing: A Workshop on Prompting, Research, and Revision Strategies for Student Writers*")
      st.write("Sana Chakroun, Sweta Bharadwaj, & Christopher Hill")
    with col2:
      st.write("*Natural 20: Crafting Voice Through D&D Roleplay*")
      st.write("Juan Jose Saenz")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
    col0, col1, col2 = st.columns([1,2,2],gap="small")
    with col0:
      st.write("10:30-11:25")
    with col1:
      st.write("*Research Reimagined through AI*")
      st.write("Amani Magid & Grace Adeneye")
    with col2:
      st.write("*Training Consultants to Address AI Use in Students’ Writing*")
      st.write("Avasha Rambiritch & Grace Pregent")
    st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)
  # *****************************************************************************************************
  col0, col1 = st.columns([2,5],gap="small")
  with col0:
    st.write("11:30am - 12:00pm")
  with col1:
    st.write("**Presidential Perspectives**")
    st.write("The MENAWCA Presidents: Sahar Mari, Kelly Wilson, Nicole Abiad, & Ryan McDonald")
    st.write("Faculty Hub, Library, Level 3, Campus Center (C2)")
  st.markdown("<hr style='margin:0;'>",unsafe_allow_html=True)

